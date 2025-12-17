"""FAISS-based vector store for similarity search."""
import logging
import numpy as np
from pathlib import Path
import faiss
from config import Config

logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(__name__)


class VectorStore:
    """Vector store using FAISS for similarity search."""
    
    def __init__(self, dimension=None):
        """
        Initialize vector store.
        
        Args:
            dimension: Embedding dimension (defaults to Config.EMBEDDING_DIMENSION)
        """
        self.dimension = dimension or Config.EMBEDDING_DIMENSION
        self.index = None
        self.metadata = []
        self._initialize_index()
    
    def _initialize_index(self):
        """Initialize FAISS index."""
        # Use IndexFlatL2 for exact L2 distance search
        self.index = faiss.IndexFlatL2(self.dimension)
        logger.info(f"Initialized FAISS index with dimension {self.dimension}")
    
    def add_vectors(self, embeddings, metadata):
        """
        Add vectors to the index.
        
        Args:
            embeddings: numpy array of shape (n, dimension)
            metadata: list of metadata dictionaries (length n)
        """
        if len(embeddings) != len(metadata):
            raise ValueError(
                f"Embeddings ({len(embeddings)}) and metadata ({len(metadata)}) length mismatch"
            )
        
        # Ensure embeddings are float32
        embeddings = embeddings.astype('float32')
        
        # Verify dimension
        if embeddings.shape[1] != self.dimension:
            raise ValueError(
                f"Embedding dimension {embeddings.shape[1]} doesn't match index dimension {self.dimension}"
            )
        
        # Add to index
        self.index.add(embeddings)
        self.metadata.extend(metadata)
        
        logger.info(f"Added {len(embeddings)} vectors to index (total: {self.index.ntotal})")
    
    def search(self, query_embedding, k=5):
        """
        Search for top-k most similar vectors.
        
        Args:
            query_embedding: numpy array of shape (dimension,) or (1, dimension)
            k: number of results to return
        
        Returns:
            list: List of tuples (index, distance, metadata)
        """
        if self.index.ntotal == 0:
            logger.warning("Index is empty")
            return []
        
        # Ensure query is 2D and float32
        if query_embedding.ndim == 1:
            query_embedding = query_embedding.reshape(1, -1)
        query_embedding = query_embedding.astype('float32')
        
        # Limit k to available vectors
        k = min(k, self.index.ntotal)
        
        # Search
        distances, indices = self.index.search(query_embedding, k)
        
        # Prepare results
        results = []
        for i, (idx, dist) in enumerate(zip(indices[0], distances[0])):
            if idx < len(self.metadata):
                # Convert L2 distance to similarity score (inverse)
                # Lower distance = higher similarity
                similarity_score = 1.0 / (1.0 + dist)
                
                results.append({
                    'rank': i + 1,
                    'index': int(idx),
                    'distance': float(dist),
                    'similarity_score': float(similarity_score),
                    'metadata': self.metadata[idx]
                })
        
        return results
    
    def save(self, path=None):
        """
        Save index and metadata to disk.
        
        Args:
            path: Directory path (defaults to Config.VECTOR_STORE_DIR)
        """
        if path is None:
            path = Config.VECTOR_STORE_DIR
        else:
            path = Path(path)
        
        path.mkdir(parents=True, exist_ok=True)
        
        # Save FAISS index
        index_path = path / "index.faiss"
        faiss.write_index(self.index, str(index_path))
        logger.info(f"Saved FAISS index to {index_path}")
        
        # Save metadata using embeddings module
        from embeddings.load_embeddings import save_embeddings
        
        # Get embeddings from index
        embeddings = np.zeros((self.index.ntotal, self.dimension), dtype='float32')
        for i in range(self.index.ntotal):
            embeddings[i] = self.index.reconstruct(int(i))
        
        save_embeddings(embeddings, self.metadata, path)
    
    def load(self, path=None):
        """
        Load index and metadata from disk.
        
        Args:
            path: Directory path (defaults to Config.VECTOR_STORE_DIR)
        """
        if path is None:
            path = Config.VECTOR_STORE_DIR
        else:
            path = Path(path)
        
        # Load FAISS index
        index_path = path / "index.faiss"
        if not index_path.exists():
            raise FileNotFoundError(f"FAISS index not found at {index_path}")
        
        self.index = faiss.read_index(str(index_path))
        self.dimension = self.index.d
        logger.info(f"Loaded FAISS index from {index_path} ({self.index.ntotal} vectors)")
        
        # Load metadata
        from embeddings.load_embeddings import load_embeddings
        _, self.metadata = load_embeddings(path)
        
        # Verify consistency
        if self.index.ntotal != len(self.metadata):
            logger.warning(
                f"Index has {self.index.ntotal} vectors but {len(self.metadata)} metadata items"
            )
    
    def get_stats(self):
        """Get statistics about the vector store."""
        return {
            'total_vectors': self.index.ntotal if self.index else 0,
            'dimension': self.dimension,
            'metadata_count': len(self.metadata)
        }


def build_vector_store_from_embeddings(embeddings_path=None):
    """
    Build vector store from saved embeddings.
    
    Args:
        embeddings_path: Path to embeddings directory
    
    Returns:
        VectorStore: Initialized vector store
    """
    from embeddings.load_embeddings import load_embeddings, load_embedding_info
    
    # Load embeddings and metadata
    embeddings, metadata = load_embeddings(embeddings_path)
    
    # Get embedding dimension
    info = load_embedding_info(embeddings_path)
    dimension = info.get('embedding_dimension', embeddings.shape[1])
    
    # Create vector store
    vector_store = VectorStore(dimension=dimension)
    vector_store.add_vectors(embeddings, metadata)
    
    # Save as FAISS index
    vector_store.save(embeddings_path)
    
    logger.info("Vector store built successfully")
    return vector_store


if __name__ == "__main__":
    # Test vector store
    from embeddings.load_embeddings import embeddings_exist
    
    if embeddings_exist():
        logger.info("Building vector store from embeddings...")
        vector_store = build_vector_store_from_embeddings()
        
        stats = vector_store.get_stats()
        print(f"\nVector Store Stats:")
        print(f"  Total vectors: {stats['total_vectors']}")
        print(f"  Dimension: {stats['dimension']}")
        print(f"  Metadata count: {stats['metadata_count']}")
        
        # Test search with first embedding
        if stats['total_vectors'] > 0:
            from embeddings.load_embeddings import load_embeddings
            embeddings, _ = load_embeddings()
            
            print(f"\nTesting search with first embedding...")
            results = vector_store.search(embeddings[0], k=3)
            
            for result in results:
                print(f"\n  Rank {result['rank']}:")
                print(f"    Product: {result['metadata'].get('name', 'N/A')}")
                print(f"    Similarity: {result['similarity_score']:.4f}")
    else:
        logger.info("No embeddings found. Run build_embeddings.py first.")

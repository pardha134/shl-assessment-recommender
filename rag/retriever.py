"""Retriever for RAG-based recommendation system."""
import logging
from config import Config
from vector_store.vector_store import VectorStore
from vector_store.query_processor import QueryProcessor

logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(__name__)


class Retriever:
    """Retrieve relevant products using vector similarity search."""
    
    def __init__(self, vector_store=None):
        """
        Initialize retriever.
        
        Args:
            vector_store: VectorStore instance (will load from disk if None)
        """
        self.vector_store = vector_store
        self.query_processor = QueryProcessor()
        
        if self.vector_store is None:
            self._load_vector_store()
    
    def _load_vector_store(self):
        """Load vector store from disk."""
        try:
            self.vector_store = VectorStore()
            self.vector_store.load()
            logger.info("Loaded vector store successfully")
        except Exception as e:
            logger.error(f"Failed to load vector store: {e}")
            raise RuntimeError(
                "Vector store not found. Please run build_embeddings.py first."
            )
    
    def retrieve(self, query, k=None):
        """
        Retrieve top-k relevant products for a query.
        
        Args:
            query: Query string
            k: Number of results to return (defaults to Config.TOP_K_RESULTS)
        
        Returns:
            list: List of retrieved product dictionaries with scores
        """
        if k is None:
            k = Config.TOP_K_RESULTS
        
        logger.info(f"Retrieving top-{k} results for query: '{query}'")
        
        # Generate query embedding
        try:
            query_embedding = self.query_processor.generate_query_embedding(query)
        except Exception as e:
            logger.error(f"Failed to generate query embedding: {e}")
            raise
        
        # Search vector store
        try:
            results = self.vector_store.search(query_embedding, k=k)
        except Exception as e:
            logger.error(f"Failed to search vector store: {e}")
            raise
        
        # Check if results are empty
        if not results:
            logger.warning("No results found for query")
            return []
        
        # Format results
        retrieved_docs = []
        for result in results:
            doc = {
                'rank': result['rank'],
                'product_id': result['metadata'].get('id'),
                'product_name': result['metadata'].get('name'),
                'description': result['metadata'].get('description'),
                'category': result['metadata'].get('category'),
                'test_type': result['metadata'].get('test_type', ''),
                'url': result['metadata'].get('url', ''),
                'assessment_url': result['metadata'].get('assessment_url', ''),
                'target_roles': result['metadata'].get('target_roles', []),
                'skills_assessed': result['metadata'].get('skills_assessed', []),
                'duration': result['metadata'].get('duration'),
                'similarity_score': result['similarity_score'],
                'distance': result['distance']
            }
            retrieved_docs.append(doc)
        
        logger.info(f"Retrieved {len(retrieved_docs)} documents")
        return retrieved_docs
    
    def retrieve_with_filter(self, query, k=None, category=None, min_score=0.0):
        """
        Retrieve products with optional filtering.
        
        Args:
            query: Query string
            k: Number of results
            category: Filter by category (optional)
            min_score: Minimum similarity score threshold
        
        Returns:
            list: Filtered retrieved products
        """
        # Get initial results
        results = self.retrieve(query, k=k*2 if category or min_score > 0 else k)
        
        # Apply filters
        filtered_results = []
        for doc in results:
            # Category filter
            if category and doc.get('category', '').lower() != category.lower():
                continue
            
            # Score filter
            if doc.get('similarity_score', 0) < min_score:
                continue
            
            filtered_results.append(doc)
        
        # Limit to k results
        filtered_results = filtered_results[:k or Config.TOP_K_RESULTS]
        
        logger.info(f"Filtered to {len(filtered_results)} results")
        return filtered_results
    
    def format_context_for_llm(self, retrieved_docs):
        """
        Format retrieved documents as context for LLM.
        
        Args:
            retrieved_docs: List of retrieved product dictionaries
        
        Returns:
            str: Formatted context string
        """
        if not retrieved_docs:
            return "No relevant assessments found."
        
        context_parts = []
        
        for i, doc in enumerate(retrieved_docs, 1):
            context = f"{i}. {doc['product_name']}\n"
            context += f"   Category: {doc['category']}\n"
            context += f"   Description: {doc['description']}\n"
            
            if doc.get('target_roles'):
                roles = ', '.join(doc['target_roles'])
                context += f"   Target Roles: {roles}\n"
            
            if doc.get('skills_assessed'):
                skills = ', '.join(doc['skills_assessed'])
                context += f"   Skills Assessed: {skills}\n"
            
            if doc.get('duration'):
                context += f"   Duration: {doc['duration']}\n"
            
            context += f"   Relevance Score: {doc['similarity_score']:.3f}\n"
            
            context_parts.append(context)
        
        return "\n".join(context_parts)


def test_retriever():
    """Test retriever functionality."""
    from embeddings.load_embeddings import embeddings_exist
    
    if not embeddings_exist():
        print("No embeddings found. Please run build_embeddings.py first.")
        return
    
    # Initialize retriever
    retriever = Retriever()
    
    # Test queries
    test_queries = [
        "Hire fresh graduates for software engineering roles",
        "Assessment for senior leadership positions",
        "Customer service skills evaluation",
        "Technical coding test for Python developers"
    ]
    
    print("Testing Retriever\n")
    print("=" * 80)
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        print("-" * 80)
        
        try:
            results = retriever.retrieve(query, k=3)
            
            if results:
                for doc in results:
                    print(f"\n{doc['rank']}. {doc['product_name']}")
                    print(f"   Category: {doc['category']}")
                    print(f"   Similarity: {doc['similarity_score']:.4f}")
                    print(f"   Description: {doc['description'][:100]}...")
            else:
                print("No results found")
        
        except Exception as e:
            print(f"Error: {e}")
        
        print()


if __name__ == "__main__":
    test_retriever()

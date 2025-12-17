"""Generate embeddings for product catalogue."""
import json
import time
import logging
import numpy as np
from pathlib import Path
from config import Config

logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(__name__)


class EmbeddingGenerator:
    """Generate embeddings using OpenAI or HuggingFace models."""
    
    def __init__(self, model_name=None):
        self.model_name = model_name or Config.EMBEDDING_MODEL
        self.client = None
        self.model = None
        
        # Initialize the appropriate model
        # Use HuggingFace by default due to API quota issues
        if model_name and 'text-embedding' in model_name:
            self._init_openai()
        else:
            # Default to HuggingFace
            self.model_name = "sentence-transformers/all-MiniLM-L6-v2"
            self._init_huggingface()
    
    def _init_openai(self):
        """Initialize OpenAI client."""
        try:
            from openai import OpenAI
            
            if not Config.OPENAI_API_KEY:
                raise ValueError("OPENAI_API_KEY not found in environment")
            
            self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
            logger.info(f"Initialized OpenAI embeddings with model: {self.model_name}")
        
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI: {e}")
            logger.info("Falling back to HuggingFace model")
            self.model_name = "sentence-transformers/all-MiniLM-L6-v2"
            self._init_huggingface()
    
    def _init_huggingface(self):
        """Initialize HuggingFace model."""
        try:
            from sentence_transformers import SentenceTransformer
            
            self.model = SentenceTransformer(self.model_name)
            logger.info(f"Initialized HuggingFace embeddings with model: {self.model_name}")
        
        except Exception as e:
            logger.error(f"Failed to initialize HuggingFace model: {e}")
            raise
    
    def generate_embedding(self, text):
        """
        Generate embedding for a single text.
        
        Args:
            text: Text string
        
        Returns:
            np.ndarray: Embedding vector
        """
        if self.client:
            # OpenAI
            response = self.client.embeddings.create(
                input=text,
                model=self.model_name
            )
            embedding = response.data[0].embedding
            return np.array(embedding)
        else:
            # HuggingFace
            embedding = self.model.encode(text, convert_to_numpy=True)
            return embedding
    
    def generate_embeddings_batch(self, texts, batch_size=100):
        """
        Generate embeddings for multiple texts in batches.
        
        Args:
            texts: List of text strings
            batch_size: Number of texts to process per batch
        
        Returns:
            np.ndarray: Array of embeddings
        """
        embeddings = []
        total_batches = (len(texts) + batch_size - 1) // batch_size
        
        logger.info(f"Generating embeddings for {len(texts)} texts in {total_batches} batches")
        
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            batch_num = i // batch_size + 1
            
            logger.info(f"Processing batch {batch_num}/{total_batches}")
            
            try:
                if self.client:
                    # OpenAI - process batch
                    response = self.client.embeddings.create(
                        input=batch,
                        model=self.model_name
                    )
                    batch_embeddings = [np.array(item.embedding) for item in response.data]
                else:
                    # HuggingFace - process batch
                    batch_embeddings = self.model.encode(batch, convert_to_numpy=True)
                
                embeddings.extend(batch_embeddings)
                
                # Rate limiting for API calls
                if self.client and i + batch_size < len(texts):
                    time.sleep(0.5)  # Small delay between batches
            
            except Exception as e:
                logger.error(f"Error processing batch {batch_num}: {e}")
                # Add zero vectors for failed batch
                embedding_dim = len(embeddings[0]) if embeddings else Config.EMBEDDING_DIMENSION
                for _ in range(len(batch)):
                    embeddings.append(np.zeros(embedding_dim))
        
        return np.array(embeddings)
    
    def get_embedding_dimension(self):
        """Get the dimension of embeddings from this model."""
        if self.client:
            # OpenAI dimensions
            if 'ada-002' in self.model_name:
                return 1536
            elif 'ada-003' in self.model_name:
                return 3072
            else:
                return 1536  # Default
        else:
            # HuggingFace - get from model
            return self.model.get_sentence_embedding_dimension()


def load_products(filename="shl_products.json"):
    """Load products from JSON file."""
    filepath = Config.PROCESSED_DATA_DIR / filename
    
    with open(filepath, 'r', encoding='utf-8') as f:
        products = json.load(f)
    
    logger.info(f"Loaded {len(products)} products from {filepath}")
    return products


def prepare_texts_for_embedding(products):
    """
    Prepare product texts for embedding generation.
    
    Args:
        products: List of product dictionaries
    
    Returns:
        list: List of text strings ready for embedding
    """
    from preprocessing.clean_text import create_embedding_text
    
    texts = []
    for product in products:
        text = create_embedding_text(product)
        texts.append(text)
    
    return texts


def main():
    """Main execution function."""
    # Load products
    products = load_products()
    
    # Clean and prepare texts
    logger.info("Preparing texts for embedding...")
    from preprocessing.clean_text import clean_products
    products = clean_products(products)
    
    # Chunk if necessary
    from preprocessing.chunk_products import chunk_products
    products = chunk_products(products, max_tokens=512, overlap_tokens=50)
    
    # Prepare embedding texts
    texts = prepare_texts_for_embedding(products)
    
    # Generate embeddings
    logger.info("Generating embeddings...")
    generator = EmbeddingGenerator()
    embeddings = generator.generate_embeddings_batch(texts, batch_size=100)
    
    logger.info(f"Generated embeddings with shape: {embeddings.shape}")
    
    # Save embeddings and metadata
    from embeddings.load_embeddings import save_embeddings
    save_embeddings(embeddings, products)
    
    logger.info("Embedding generation completed successfully")


if __name__ == "__main__":
    main()

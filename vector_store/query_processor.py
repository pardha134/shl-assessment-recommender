"""Query processing and embedding generation."""
import logging
import numpy as np
from config import Config
from embeddings.build_embeddings import EmbeddingGenerator
from preprocessing.clean_text import normalize_text_for_embedding

logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(__name__)


class QueryProcessor:
    """Process queries and generate embeddings."""
    
    def __init__(self, model_name=None):
        """
        Initialize query processor.
        
        Args:
            model_name: Embedding model name (defaults to HuggingFace)
        """
        # Use HuggingFace by default due to API quota issues
        self.model_name = model_name or "sentence-transformers/all-MiniLM-L6-v2"
        self.generator = None
        # Lazy initialization - only create generator when needed
    
    def _initialize_generator(self):
        """Initialize embedding generator (lazy initialization)."""
        if self.generator is None:
            try:
                self.generator = EmbeddingGenerator(self.model_name)
                logger.info(f"Initialized query processor with model: {self.model_name}")
            except Exception as e:
                logger.error(f"Failed to initialize embedding generator: {e}")
                raise
    
    def process_query(self, query_text):
        """
        Process and clean query text.
        
        Args:
            query_text: Raw query string
        
        Returns:
            str: Cleaned and normalized query text
        """
        if not query_text or not query_text.strip():
            raise ValueError("Query text cannot be empty")
        
        # Normalize text for embedding
        processed_query = normalize_text_for_embedding(query_text)
        
        logger.debug(f"Processed query: '{processed_query}'")
        return processed_query
    
    def generate_query_embedding(self, query_text):
        """
        Generate embedding for a query.
        
        Args:
            query_text: Query string
        
        Returns:
            np.ndarray: Query embedding vector
        """
        # Initialize generator if not already done (lazy initialization)
        self._initialize_generator()
        
        # Process query
        processed_query = self.process_query(query_text)
        
        # Generate embedding
        try:
            embedding = self.generator.generate_embedding(processed_query)
            logger.debug(f"Generated query embedding with shape: {embedding.shape}")
            return embedding
        
        except Exception as e:
            logger.error(f"Failed to generate query embedding: {e}")
            raise
    
    def expand_query(self, query_text):
        """
        Expand query with synonyms and related terms (optional enhancement).
        
        Args:
            query_text: Original query
        
        Returns:
            str: Expanded query
        """
        # Basic expansion - can be enhanced with NLP techniques
        expansions = {
            'software engineer': 'software engineer developer programmer coder',
            'fresh graduate': 'fresh graduate entry level junior new grad',
            'manager': 'manager supervisor team lead leadership',
            'sales': 'sales business development account manager',
            'customer service': 'customer service support client relations',
            'data': 'data analytics analysis scientist',
        }
        
        query_lower = query_text.lower()
        
        for key, expansion in expansions.items():
            if key in query_lower:
                query_text = query_text + ' ' + expansion
        
        return query_text


def test_query_processor():
    """Test query processor functionality."""
    processor = QueryProcessor()
    
    # Test queries
    test_queries = [
        "Hire fresh graduates for software engineering roles",
        "Need assessment for senior managers",
        "Customer service position evaluation",
        "Technical skills test for data analysts"
    ]
    
    print("Testing Query Processor\n")
    
    for query in test_queries:
        print(f"Original query: {query}")
        
        # Process query
        processed = processor.process_query(query)
        print(f"Processed: {processed}")
        
        # Generate embedding
        try:
            embedding = processor.generate_query_embedding(query)
            print(f"Embedding shape: {embedding.shape}")
            print(f"Embedding sample: {embedding[:5]}")
        except Exception as e:
            print(f"Error: {e}")
        
        print()


if __name__ == "__main__":
    test_query_processor()

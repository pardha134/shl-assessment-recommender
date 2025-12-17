"""LLM-based recommendation engine using RAG."""
import logging
import time
from config import Config
from rag.retriever import Retriever
from rag.prompt import create_recommendation_prompt, extract_recommendations_from_response

logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(__name__)


class Recommender:
    """Generate assessment recommendations using LLM and RAG."""
    
    def __init__(self, retriever=None):
        """
        Initialize recommender.
        
        Args:
            retriever: Retriever instance (will create new if None)
        """
        self.retriever = retriever or Retriever()
        self.llm = None
        self._initialize_llm()
    
    def _initialize_llm(self):
        """Initialize LangChain LLM."""
        try:
            from langchain_openai import ChatOpenAI
            
            if not Config.OPENAI_API_KEY:
                raise ValueError("OPENAI_API_KEY not found in environment")
            
            self.llm = ChatOpenAI(
                model=Config.LLM_MODEL,
                temperature=Config.LLM_TEMPERATURE,
                max_tokens=1000,
                api_key=Config.OPENAI_API_KEY
            )
            
            logger.info(f"Initialized LLM: {Config.LLM_MODEL}")
        
        except Exception as e:
            logger.error(f"Failed to initialize LLM: {e}")
            raise
    
    def recommend(self, query, top_k=None, template_type="default"):
        """
        Generate recommendations for a query.
        
        Args:
            query: User's hiring requirement query
            top_k: Number of products to retrieve (defaults to Config.TOP_K_RESULTS)
            template_type: Prompt template type
        
        Returns:
            dict: Recommendation results
        """
        start_time = time.time()
        
        logger.info(f"Generating recommendations for query: '{query}'")
        
        # Retrieve relevant products
        try:
            retrieved_docs = self.retriever.retrieve(query, k=top_k)
        except Exception as e:
            logger.error(f"Retrieval failed: {e}")
            return {
                'query': query,
                'error': f"Retrieval failed: {str(e)}",
                'recommendations': [],
                'processing_time': time.time() - start_time
            }
        
        # Check if any documents were retrieved
        if not retrieved_docs:
            logger.warning("No relevant documents found")
            return {
                'query': query,
                'message': 'No suitable assessments found for this query',
                'recommendations': [],
                'processing_time': time.time() - start_time
            }
        
        # Format context for LLM
        context = self.retriever.format_context_for_llm(retrieved_docs)
        
        # Create prompt
        prompt = create_recommendation_prompt(query, context, template_type)
        
        # Generate recommendations using LLM
        try:
            response = self.llm.invoke(prompt)
            response_text = response.content
            logger.debug(f"LLM response: {response_text[:200]}...")
        
        except Exception as e:
            logger.error(f"LLM generation failed: {e}")
            # Fallback to retrieval-only results
            return self._create_fallback_response(query, retrieved_docs, start_time)
        
        # Parse response
        recommendations = extract_recommendations_from_response(response_text)
        
        # Enrich recommendations with retrieved data
        recommendations = self._enrich_recommendations(recommendations, retrieved_docs)
        
        # Limit to requested count
        if top_k:
            recommendations = recommendations[:top_k]
        
        processing_time = time.time() - start_time
        
        result = {
            'query': query,
            'recommendations': recommendations,
            'raw_response': response_text,
            'retrieved_count': len(retrieved_docs),
            'processing_time': processing_time
        }
        
        logger.info(f"Generated {len(recommendations)} balanced recommendations in {processing_time:.2f}s")
        
        return result
    
    def _enrich_recommendations(self, recommendations, retrieved_docs):
        """
        Enrich parsed recommendations with full product data.
        
        Args:
            recommendations: Parsed recommendations from LLM
            retrieved_docs: Retrieved product documents
        
        Returns:
            list: Enriched recommendations
        """
        # Create lookup by product name
        product_lookup = {
            doc['product_name'].lower(): doc
            for doc in retrieved_docs
        }
        
        enriched = []
        
        for rec in recommendations:
            assessment_name = rec.get('assessment_name', '')
            
            # Find matching product
            product_data = None
            for name, data in product_lookup.items():
                if name in assessment_name.lower() or assessment_name.lower() in name:
                    product_data = data
                    break
            
            # Enrich recommendation
            enriched_rec = {
                'assessment_name': assessment_name,
                'relevance_score': rec.get('relevance_score', 0),
                'reasoning': rec.get('reasoning', ''),
            }
            
            # Add product details if found
            if product_data:
                enriched_rec.update({
                    'product_id': product_data.get('product_id'),
                    'category': product_data.get('category'),
                    'description': product_data.get('description'),
                    'target_roles': product_data.get('target_roles', []),
                    'skills_assessed': product_data.get('skills_assessed', []),
                    'duration': product_data.get('duration'),
                    'similarity_score': product_data.get('similarity_score')
                })
            
            enriched.append(enriched_rec)
        
        return enriched
    
    def _create_fallback_response(self, query, retrieved_docs, start_time):
        """
        Create fallback response when LLM fails.
        
        Args:
            query: Original query
            retrieved_docs: Retrieved documents
            start_time: Start timestamp
        
        Returns:
            dict: Fallback response
        """
        logger.info("Creating fallback response from retrieval results")
        
        recommendations = []
        
        for i, doc in enumerate(retrieved_docs[:5], 1):
            rec = {
                'assessment_name': doc['product_name'],
                'assessment_url': doc.get('assessment_url', doc.get('url', '')),
                'url': doc.get('url', doc.get('assessment_url', '')),
                'test_type': doc.get('test_type', ''),
                'relevance_score': doc['similarity_score'] * 10,  # Scale to 0-10
                'reasoning': f"This assessment matches your requirements based on semantic similarity. "
                            f"Category: {doc['category']}. "
                            f"Suitable for: {', '.join(doc.get('target_roles', []))}.",
                'product_id': doc.get('product_id'),
                'category': doc.get('category'),
                'description': doc.get('description'),
                'target_roles': doc.get('target_roles', []),
                'skills_assessed': doc.get('skills_assessed', []),
                'duration': doc.get('duration'),
                'similarity_score': doc.get('similarity_score')
            }
            recommendations.append(rec)
        
        return {
            'query': query,
            'recommendations': recommendations,
            'message': 'Recommendations based on similarity search (LLM unavailable)',
            'retrieved_count': len(retrieved_docs),
            'processing_time': time.time() - start_time
        }


def test_recommender():
    """Test recommender functionality."""
    from embeddings.load_embeddings import embeddings_exist
    
    if not embeddings_exist():
        print("No embeddings found. Please run build_embeddings.py first.")
        return
    
    # Initialize recommender
    try:
        recommender = Recommender()
    except Exception as e:
        print(f"Failed to initialize recommender: {e}")
        print("Note: OpenAI API key required for full functionality")
        return
    
    # Test queries
    test_queries = [
        "Hire fresh graduates for software engineering roles",
        "Assessment for senior leadership and management positions",
        "Customer service skills evaluation for retail staff"
    ]
    
    print("Testing Recommender\n")
    print("=" * 80)
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        print("-" * 80)
        
        try:
            result = recommender.recommend(query, top_k=5)
            
            print(f"Processing time: {result['processing_time']:.2f}s")
            print(f"Retrieved: {result.get('retrieved_count', 0)} documents")
            print(f"Recommendations: {len(result['recommendations'])}\n")
            
            for i, rec in enumerate(result['recommendations'], 1):
                print(f"{i}. {rec['assessment_name']}")
                print(f"   Score: {rec.get('relevance_score', 0):.1f}/10")
                print(f"   Reasoning: {rec.get('reasoning', 'N/A')[:150]}...")
                print()
        
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    test_recommender()

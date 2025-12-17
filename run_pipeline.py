"""Run the complete data pipeline and test the system."""
import logging
import sys
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def run_pipeline():
    """Run the complete data pipeline."""
    
    print("\n" + "="*80)
    print("SHL ASSESSMENT RECOMMENDER - PIPELINE EXECUTION")
    print("="*80 + "\n")
    
    # Step 1: Scrape data
    print("Step 1: Scraping SHL product data...")
    print("-" * 80)
    try:
        from scraper.scrape_shl import main as scrape_main
        scrape_main()
        print("✅ Scraping completed\n")
    except Exception as e:
        print(f"❌ Scraping failed: {e}\n")
        return False
    
    # Step 2: Parse products
    print("Step 2: Parsing product data...")
    print("-" * 80)
    try:
        from scraper.parse_products import main as parse_main
        parse_main()
        print("✅ Parsing completed\n")
    except Exception as e:
        print(f"❌ Parsing failed: {e}\n")
        return False
    
    # Step 3: Build embeddings
    print("Step 3: Building embeddings...")
    print("-" * 80)
    try:
        from embeddings.build_embeddings import main as embeddings_main
        embeddings_main()
        print("✅ Embeddings completed\n")
    except Exception as e:
        print(f"❌ Embeddings failed: {e}\n")
        print("Note: This step requires an OpenAI API key")
        return False
    
    # Step 4: Build vector store
    print("Step 4: Building vector store...")
    print("-" * 80)
    try:
        from vector_store.vector_store import build_vector_store_from_embeddings
        build_vector_store_from_embeddings()
        print("✅ Vector store completed\n")
    except Exception as e:
        print(f"❌ Vector store failed: {e}\n")
        return False
    
    print("="*80)
    print("✅ PIPELINE COMPLETED SUCCESSFULLY")
    print("="*80 + "\n")
    
    return True


def test_system():
    """Test the system with sample queries."""
    
    print("\n" + "="*80)
    print("TESTING SYSTEM")
    print("="*80 + "\n")
    
    test_queries = [
        "Hire fresh graduates for software engineering roles",
        "Assessment for senior leadership positions",
        "Customer service skills evaluation"
    ]
    
    try:
        from rag.recommender import Recommender
        
        print("Initializing recommender...")
        recommender = Recommender()
        print("✅ Recommender initialized\n")
        
        for i, query in enumerate(test_queries, 1):
            print(f"Test {i}: {query}")
            print("-" * 80)
            
            try:
                result = recommender.recommend(query, top_k=3)
                
                print(f"Processing time: {result['processing_time']:.2f}s")
                print(f"Recommendations: {len(result['recommendations'])}\n")
                
                for j, rec in enumerate(result['recommendations'], 1):
                    print(f"  {j}. {rec['assessment_name']}")
                    print(f"     Score: {rec.get('relevance_score', 0):.1f}/10")
                
                print()
            
            except Exception as e:
                print(f"❌ Test failed: {e}\n")
                return False
        
        print("="*80)
        print("✅ ALL TESTS PASSED")
        print("="*80 + "\n")
        
        return True
    
    except Exception as e:
        print(f"❌ System test failed: {e}\n")
        return False


def main():
    """Main execution function."""
    
    print("\n🚀 Starting SHL Assessment Recommender Setup\n")
    
    # Check for API key
    from config import Config
    
    if not Config.OPENAI_API_KEY:
        print("⚠️  WARNING: OPENAI_API_KEY not found in environment")
        print("Please set your OpenAI API key in the .env file\n")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            print("Exiting...")
            return
    
    # Run pipeline
    pipeline_success = run_pipeline()
    
    if not pipeline_success:
        print("\n❌ Pipeline failed. Please check the errors above.")
        return
    
    # Test system
    print("\nWould you like to test the system? (y/n): ", end='')
    response = input()
    
    if response.lower() == 'y':
        test_success = test_system()
        
        if test_success:
            print("\n🎉 Setup and testing completed successfully!")
            print("\nNext steps:")
            print("  1. Start API: python api/main.py")
            print("  2. Start Web App: streamlit run webapp/app.py")
            print("  3. Run Evaluation: python evaluation/retrieval_metrics.py")
            print("  4. Export Predictions: python export_predictions.py")
    else:
        print("\n✅ Pipeline completed. You can now:")
        print("  1. Start API: python api/main.py")
        print("  2. Start Web App: streamlit run webapp/app.py")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        print(f"\n❌ Unexpected error: {e}")

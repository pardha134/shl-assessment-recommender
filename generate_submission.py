"""Generate predictions for submission."""
import pandas as pd
import logging
from pathlib import Path
from config import Config
from rag.recommender import Recommender

logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(__name__)


def generate_submission_file(input_file, output_filename):
    """
    Generate predictions from test queries and create submission CSV.
    
    Args:
        input_file: Path to test queries CSV
        output_filename: Output CSV filename
    
    Returns:
        Path: Path to exported CSV file
    """
    # Read test queries
    logger.info(f"Reading test queries from {input_file}")
    df = pd.read_csv(input_file)
    
    # Get unique queries
    unique_queries = df['Query'].unique()
    logger.info(f"Found {len(unique_queries)} unique queries")
    
    # Initialize recommender
    logger.info("Initializing recommender...")
    recommender = Recommender()
    logger.info("Recommender initialized successfully")
    
    # Generate predictions
    results = []
    
    for i, query in enumerate(unique_queries, 1):
        logger.info(f"Processing query {i}/{len(unique_queries)}")
        
        try:
            # Get recommendations
            result = recommender.recommend(query, top_k=10)
            
            # Extract assessment URLs from recommendations
            assessment_urls = []
            for rec in result.get('recommendations', []):
                url = rec.get('assessment_url', rec.get('url', ''))
                if url and url != 'N/A':
                    assessment_urls.append(url)
            
            # Add result
            results.append({
                'Query': query,
                'Assessment_url': ', '.join(assessment_urls) if assessment_urls else 'No recommendations'
            })
            
        except Exception as e:
            logger.error(f"Error processing query {i}: {e}")
            results.append({
                'Query': query,
                'Assessment_url': 'Error'
            })
    
    # Create DataFrame
    results_df = pd.DataFrame(results)
    
    # Save to CSV
    output_path = Config.PREDICTIONS_DIR / output_filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    results_df.to_csv(output_path, index=False)
    logger.info(f"Saved predictions to {output_path}")
    
    return output_path


def main():
    """Main function."""
    input_file = "data/test_queries.csv"
    output_filename = "Pardha_Saradhi_Thumma.csv"
    
    print("\n" + "="*80)
    print("GENERATING SUBMISSION FILE")
    print("="*80 + "\n")
    
    try:
        output_path = generate_submission_file(input_file, output_filename)
        
        print(f"\n✅ SUCCESS!")
        print(f"Predictions saved to: {output_path}")
        print("\nSample predictions:")
        
        # Show sample
        df = pd.read_csv(output_path)
        print(f"\nTotal queries: {len(df)}")
        print("\nFirst 3 predictions:")
        print(df.head(3).to_string(index=False))
        
    except Exception as e:
        logger.error(f"Failed to generate submission: {e}", exc_info=True)
        print(f"\n❌ ERROR: {e}")


if __name__ == "__main__":
    main()

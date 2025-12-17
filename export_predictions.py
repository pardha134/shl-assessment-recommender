"""Export predictions to CSV for submission."""
import csv
import logging
from datetime import datetime
from pathlib import Path
from config import Config
from rag.recommender import Recommender

logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(__name__)


def export_predictions_to_csv(queries, output_filename=None, recommender=None):
    """
    Generate predictions and export to CSV.
    
    Args:
        queries: List of query strings or dictionaries with 'query' key
        output_filename: Output CSV filename (defaults to firstname_lastname.csv)
        recommender: Recommender instance (will create if None)
    
    Returns:
        Path: Path to exported CSV file
    """
    if recommender is None:
        recommender = Recommender()
    
    if output_filename is None:
        output_filename = "firstname_lastname.csv"
    
    output_path = Config.PREDICTIONS_DIR / output_filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    logger.info(f"Generating predictions for {len(queries)} queries")
    
    predictions = []
    
    for i, query_item in enumerate(queries, 1):
        # Extract query string
        if isinstance(query_item, dict):
            query = query_item.get('query', '')
        else:
            query = str(query_item)
        
        if not query.strip():
            logger.warning(f"Skipping empty query at index {i}")
            continue
        
        logger.info(f"Processing query {i}/{len(queries)}: {query}")
        
        try:
            # Generate recommendations
            result = recommender.recommend(query, top_k=5)
            
            # Extract recommended assessment names
            recommended_names = [
                rec.get('assessment_name', '')
                for rec in result.get('recommendations', [])
            ]
            
            # Format as comma-separated string
            recommendations_str = ', '.join(recommended_names) if recommended_names else 'No recommendations'
            
            predictions.append({
                'query': query,
                'recommendations': recommendations_str,
                'num_recommendations': len(recommended_names),
                'processing_time': result.get('processing_time', 0)
            })
        
        except Exception as e:
            logger.error(f"Error processing query {i}: {e}")
            predictions.append({
                'query': query,
                'recommendations': 'Error',
                'num_recommendations': 0,
                'processing_time': 0
            })
    
    # Write to CSV
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Write header
        writer.writerow(['Query', 'Recommended Assessments'])
        
        # Write predictions
        for pred in predictions:
            writer.writerow([pred['query'], pred['recommendations']])
    
    logger.info(f"Exported {len(predictions)} predictions to {output_path}")
    
    return output_path


def export_detailed_predictions(queries, output_filename=None, recommender=None):
    """
    Generate detailed predictions with scores and export to CSV.
    
    Args:
        queries: List of query strings
        output_filename: Output CSV filename
        recommender: Recommender instance
    
    Returns:
        Path: Path to exported CSV file
    """
    if recommender is None:
        recommender = Recommender()
    
    if output_filename is None:
        output_filename = "detailed_predictions.csv"
    
    output_path = Config.PREDICTIONS_DIR / output_filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    logger.info(f"Generating detailed predictions for {len(queries)} queries")
    
    rows = []
    
    for i, query_item in enumerate(queries, 1):
        # Extract query string
        if isinstance(query_item, dict):
            query = query_item.get('query', '')
        else:
            query = str(query_item)
        
        if not query.strip():
            continue
        
        logger.info(f"Processing query {i}/{len(queries)}")
        
        try:
            result = recommender.recommend(query, top_k=5)
            
            for rec in result.get('recommendations', []):
                rows.append({
                    'query': query,
                    'assessment_name': rec.get('assessment_name', ''),
                    'relevance_score': rec.get('relevance_score', 0),
                    'category': rec.get('category', ''),
                    'reasoning': rec.get('reasoning', '')[:200]  # Truncate reasoning
                })
        
        except Exception as e:
            logger.error(f"Error processing query {i}: {e}")
    
    # Write to CSV
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        if rows:
            fieldnames = ['query', 'assessment_name', 'relevance_score', 'category', 'reasoning']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(rows)
    
    logger.info(f"Exported detailed predictions to {output_path}")
    
    return output_path


def load_queries_from_file(filepath):
    """
    Load queries from a file (CSV or text).
    
    Args:
        filepath: Path to queries file
    
    Returns:
        list: List of query strings
    """
    filepath = Path(filepath)
    queries = []
    
    if filepath.suffix == '.csv':
        import pandas as pd
        df = pd.read_csv(filepath)
        
        # Look for 'query' column
        if 'query' in df.columns:
            queries = df['query'].tolist()
        else:
            # Use first column
            queries = df.iloc[:, 0].tolist()
    
    elif filepath.suffix == '.txt':
        with open(filepath, 'r', encoding='utf-8') as f:
            queries = [line.strip() for line in f if line.strip()]
    
    else:
        raise ValueError(f"Unsupported file format: {filepath.suffix}")
    
    logger.info(f"Loaded {len(queries)} queries from {filepath}")
    return queries


def main():
    """Main function."""
    # Sample queries for demonstration
    sample_queries = [
        "Hire fresh graduates for software engineering roles",
        "Assessment for senior leadership and management positions",
        "Customer service skills evaluation for retail staff",
        "Technical coding test for Python developers",
        "Personality assessment for sales team members",
        "Cognitive ability test for data analyst positions",
        "Situational judgment for customer support roles",
        "Mechanical comprehension for engineering technicians"
    ]
    
    try:
        # Initialize recommender
        recommender = Recommender()
        
        # Export basic predictions
        logger.info("Exporting basic predictions...")
        basic_path = export_predictions_to_csv(
            sample_queries,
            output_filename="firstname_lastname.csv",
            recommender=recommender
        )
        print(f"\n✅ Basic predictions exported to: {basic_path}")
        
        # Export detailed predictions
        logger.info("Exporting detailed predictions...")
        detailed_path = export_detailed_predictions(
            sample_queries,
            output_filename="detailed_predictions.csv",
            recommender=recommender
        )
        print(f"✅ Detailed predictions exported to: {detailed_path}")
        
        # Print sample
        print("\nSample predictions:")
        with open(basic_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()[:4]  # First 3 predictions + header
            for line in lines:
                print(line.strip())
    
    except Exception as e:
        logger.error(f"Export failed: {e}", exc_info=True)
        print(f"\n❌ Export failed: {e}")


if __name__ == "__main__":
    main()

"""Text cleaning and normalization utilities."""
import re
import html
import logging
from config import Config

logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(__name__)


def clean_text(text):
    """
    Clean and normalize text content.
    
    Args:
        text: Raw text string
    
    Returns:
        str: Cleaned text
    """
    if not text:
        return ""
    
    # Decode HTML entities
    text = html.unescape(text)
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove URLs
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove leading/trailing whitespace
    text = text.strip()
    
    # Remove special characters but keep basic punctuation
    text = re.sub(r'[^\w\s.,!?;:()\-\'/]', '', text)
    
    # Remove multiple consecutive punctuation
    text = re.sub(r'([.,!?;:])\1+', r'\1', text)
    
    return text


def clean_product_text(product):
    """
    Clean text fields in a product dictionary.
    
    Args:
        product: Product dictionary
    
    Returns:
        dict: Product with cleaned text fields
    """
    cleaned_product = product.copy()
    
    # Clean text fields
    if 'name' in cleaned_product:
        cleaned_product['name'] = clean_text(cleaned_product['name'])
    
    if 'description' in cleaned_product:
        cleaned_product['description'] = clean_text(cleaned_product['description'])
    
    if 'category' in cleaned_product:
        cleaned_product['category'] = clean_text(cleaned_product['category'])
    
    # Clean list fields
    if 'target_roles' in cleaned_product:
        cleaned_product['target_roles'] = [
            clean_text(role) for role in cleaned_product['target_roles']
        ]
    
    if 'skills_assessed' in cleaned_product:
        cleaned_product['skills_assessed'] = [
            clean_text(skill) for skill in cleaned_product['skills_assessed']
        ]
    
    return cleaned_product


def clean_products(products):
    """
    Clean text in a list of products.
    
    Args:
        products: List of product dictionaries
    
    Returns:
        list: List of products with cleaned text
    """
    logger.info(f"Cleaning text for {len(products)} products")
    
    cleaned_products = []
    for product in products:
        try:
            cleaned_product = clean_product_text(product)
            cleaned_products.append(cleaned_product)
        except Exception as e:
            logger.error(f"Error cleaning product {product.get('id', 'unknown')}: {e}")
            # Keep original product if cleaning fails
            cleaned_products.append(product)
    
    logger.info(f"Successfully cleaned {len(cleaned_products)} products")
    return cleaned_products


def normalize_text_for_embedding(text):
    """
    Normalize text specifically for embedding generation.
    
    Args:
        text: Text string
    
    Returns:
        str: Normalized text optimized for embeddings
    """
    # Clean the text
    text = clean_text(text)
    
    # Convert to lowercase for consistency
    text = text.lower()
    
    # Remove extra punctuation that doesn't add semantic meaning
    text = re.sub(r'[^\w\s.,]', '', text)
    
    # Ensure single spacing
    text = ' '.join(text.split())
    
    return text


def create_embedding_text(product):
    """
    Create a combined text representation of a product for embedding.
    
    Args:
        product: Product dictionary
    
    Returns:
        str: Combined text for embedding
    """
    parts = []
    
    # Add product name
    if product.get('name'):
        parts.append(f"Assessment: {product['name']}")
    
    # Add category
    if product.get('category'):
        parts.append(f"Category: {product['category']}")
    
    # Add description
    if product.get('description'):
        parts.append(product['description'])
    
    # Add target roles
    if product.get('target_roles'):
        roles = ', '.join(product['target_roles'])
        parts.append(f"Suitable for: {roles}")
    
    # Add skills
    if product.get('skills_assessed'):
        skills = ', '.join(product['skills_assessed'])
        parts.append(f"Assesses: {skills}")
    
    # Combine all parts
    combined_text = ' '.join(parts)
    
    # Normalize for embedding
    normalized_text = normalize_text_for_embedding(combined_text)
    
    return normalized_text


if __name__ == "__main__":
    # Test cleaning functions
    sample_text = """
    <p>This is a   test with <strong>HTML</strong> tags and   extra   spaces.</p>
    Visit http://example.com or email test@example.com!!!
    """
    
    cleaned = clean_text(sample_text)
    print("Original:", repr(sample_text))
    print("Cleaned:", repr(cleaned))
    
    # Test product cleaning
    sample_product = {
        'id': '1',
        'name': '  Test  Assessment  ',
        'description': '<p>This measures <b>cognitive</b> ability.</p>',
        'category': 'Cognitive   Ability',
        'target_roles': ['  Manager  ', 'Developer  '],
        'skills_assessed': ['problem-solving', '  analytical  ']
    }
    
    cleaned_product = clean_product_text(sample_product)
    print("\nCleaned product:")
    for key, value in cleaned_product.items():
        print(f"  {key}: {value}")
    
    # Test embedding text creation
    embedding_text = create_embedding_text(cleaned_product)
    print("\nEmbedding text:", embedding_text)

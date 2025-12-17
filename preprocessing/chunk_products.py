"""Text chunking utilities for long product descriptions."""
import logging
from typing import List, Dict
from config import Config

logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(__name__)


def estimate_tokens(text):
    """
    Estimate token count (rough approximation: 1 token ≈ 4 characters).
    
    Args:
        text: Text string
    
    Returns:
        int: Estimated token count
    """
    return len(text) // 4


def chunk_text(text, max_tokens=512, overlap_tokens=50):
    """
    Split text into overlapping chunks.
    
    Args:
        text: Text to chunk
        max_tokens: Maximum tokens per chunk
        overlap_tokens: Number of tokens to overlap between chunks
    
    Returns:
        list: List of text chunks
    """
    if not text:
        return []
    
    # Convert tokens to approximate character count
    max_chars = max_tokens * 4
    overlap_chars = overlap_tokens * 4
    
    # If text is short enough, return as single chunk
    if len(text) <= max_chars:
        return [text]
    
    chunks = []
    start = 0
    
    while start < len(text):
        # Calculate end position
        end = start + max_chars
        
        # If this is not the last chunk, try to break at sentence boundary
        if end < len(text):
            # Look for sentence endings near the end position
            sentence_ends = ['. ', '! ', '? ', '.\n', '!\n', '?\n']
            best_break = end
            
            # Search backwards from end position for sentence boundary
            search_start = max(start, end - 200)  # Search within 200 chars
            for i in range(end, search_start, -1):
                for ending in sentence_ends:
                    if text[i:i+len(ending)] == ending:
                        best_break = i + len(ending)
                        break
                if best_break != end:
                    break
            
            end = best_break
        
        # Extract chunk
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        
        # Move start position with overlap
        start = end - overlap_chars
        
        # Ensure we make progress
        if start <= chunks[-1] if chunks else 0:
            start = end
    
    return chunks


def chunk_product(product, max_tokens=512, overlap_tokens=50):
    """
    Chunk a product's description if it's too long.
    
    Args:
        product: Product dictionary
        max_tokens: Maximum tokens per chunk
        overlap_tokens: Overlap between chunks
    
    Returns:
        list: List of product dictionaries (original or chunked)
    """
    description = product.get('description', '')
    
    # Check if chunking is needed
    estimated_tokens = estimate_tokens(description)
    
    if estimated_tokens <= max_tokens:
        # No chunking needed
        return [product]
    
    # Chunk the description
    chunks = chunk_text(description, max_tokens, overlap_tokens)
    
    logger.debug(f"Chunked product {product.get('id')} into {len(chunks)} parts")
    
    # Create a product dict for each chunk
    chunked_products = []
    for i, chunk in enumerate(chunks):
        chunked_product = product.copy()
        chunked_product['description'] = chunk
        chunked_product['chunk_id'] = i
        chunked_product['total_chunks'] = len(chunks)
        chunked_product['original_id'] = product.get('id')
        chunked_product['id'] = f"{product.get('id')}_chunk_{i}"
        
        chunked_products.append(chunked_product)
    
    return chunked_products


def chunk_products(products, max_tokens=512, overlap_tokens=50):
    """
    Chunk all products that exceed max token length.
    
    Args:
        products: List of product dictionaries
        max_tokens: Maximum tokens per chunk
        overlap_tokens: Overlap between chunks
    
    Returns:
        list: List of products (some may be chunked)
    """
    logger.info(f"Chunking {len(products)} products (max_tokens={max_tokens})")
    
    chunked_products = []
    total_chunks = 0
    
    for product in products:
        product_chunks = chunk_product(product, max_tokens, overlap_tokens)
        chunked_products.extend(product_chunks)
        
        if len(product_chunks) > 1:
            total_chunks += len(product_chunks)
    
    logger.info(f"Created {len(chunked_products)} total items ({total_chunks} chunks from long descriptions)")
    
    return chunked_products


def merge_chunked_results(results):
    """
    Merge results from chunked products back together.
    
    Args:
        results: List of result dictionaries with 'id' and 'score'
    
    Returns:
        list: Merged results with original product IDs
    """
    # Group by original ID
    grouped = {}
    
    for result in results:
        product_id = result.get('id', '')
        
        # Check if this is a chunked product
        if '_chunk_' in product_id:
            original_id = result.get('original_id', product_id.split('_chunk_')[0])
        else:
            original_id = product_id
        
        if original_id not in grouped:
            grouped[original_id] = {
                'id': original_id,
                'scores': [],
                'result': result
            }
        
        grouped[original_id]['scores'].append(result.get('score', 0))
    
    # Merge by taking max score for each original product
    merged_results = []
    for original_id, data in grouped.items():
        result = data['result'].copy()
        result['id'] = original_id
        result['score'] = max(data['scores'])
        
        # Remove chunk-specific fields
        result.pop('chunk_id', None)
        result.pop('total_chunks', None)
        result.pop('original_id', None)
        
        merged_results.append(result)
    
    # Sort by score
    merged_results.sort(key=lambda x: x.get('score', 0), reverse=True)
    
    return merged_results


if __name__ == "__main__":
    # Test chunking
    long_text = """
    This is a very long product description that needs to be chunked into smaller pieces.
    It contains multiple sentences and paragraphs. The chunking algorithm should try to
    break at sentence boundaries when possible. This ensures that each chunk maintains
    semantic coherence and doesn't cut off in the middle of important information.
    
    The assessment measures various cognitive abilities including problem-solving,
    analytical thinking, and decision-making skills. It is suitable for roles that
    require strong analytical capabilities and the ability to work with complex data.
    
    Candidates will be presented with scenarios and asked to analyze information,
    draw conclusions, and make recommendations. The test takes approximately 45 minutes
    to complete and provides detailed insights into cognitive strengths and areas for
    development.
    """ * 5  # Repeat to make it long
    
    chunks = chunk_text(long_text, max_tokens=100, overlap_tokens=20)
    print(f"Created {len(chunks)} chunks")
    for i, chunk in enumerate(chunks):
        print(f"\nChunk {i+1} ({estimate_tokens(chunk)} tokens):")
        print(chunk[:100] + "..." if len(chunk) > 100 else chunk)
    
    # Test product chunking
    sample_product = {
        'id': 'test_1',
        'name': 'Test Assessment',
        'description': long_text,
        'category': 'Cognitive'
    }
    
    chunked = chunk_product(sample_product, max_tokens=100)
    print(f"\n\nProduct chunked into {len(chunked)} parts")
    for chunk in chunked:
        print(f"  - {chunk['id']}: {estimate_tokens(chunk['description'])} tokens")

"""Load and save embeddings and metadata."""
import json
import logging
import numpy as np
from pathlib import Path
from config import Config

logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(__name__)


def save_embeddings(embeddings, metadata, base_path=None):
    """
    Save embeddings and metadata to disk.
    
    Args:
        embeddings: numpy array of embeddings
        metadata: list of product dictionaries
        base_path: base directory path (defaults to Config.VECTOR_STORE_DIR)
    """
    if base_path is None:
        base_path = Config.VECTOR_STORE_DIR
    else:
        base_path = Path(base_path)
    
    # Create directory if it doesn't exist
    base_path.mkdir(parents=True, exist_ok=True)
    
    # Save embeddings as numpy file
    embeddings_path = base_path / "embeddings.npy"
    np.save(embeddings_path, embeddings)
    logger.info(f"Saved embeddings to {embeddings_path} (shape: {embeddings.shape})")
    
    # Save metadata as JSON
    metadata_path = base_path / "metadata.json"
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    logger.info(f"Saved metadata for {len(metadata)} items to {metadata_path}")
    
    # Save embedding info
    info = {
        'num_embeddings': len(embeddings),
        'embedding_dimension': embeddings.shape[1] if len(embeddings) > 0 else 0,
        'model': Config.EMBEDDING_MODEL
    }
    info_path = base_path / "embedding_info.json"
    with open(info_path, 'w', encoding='utf-8') as f:
        json.dump(info, f, indent=2)
    logger.info(f"Saved embedding info to {info_path}")


def load_embeddings(base_path=None):
    """
    Load embeddings and metadata from disk.
    
    Args:
        base_path: base directory path (defaults to Config.VECTOR_STORE_DIR)
    
    Returns:
        tuple: (embeddings array, metadata list)
    """
    if base_path is None:
        base_path = Config.VECTOR_STORE_DIR
    else:
        base_path = Path(base_path)
    
    # Load embeddings
    embeddings_path = base_path / "embeddings.npy"
    if not embeddings_path.exists():
        raise FileNotFoundError(f"Embeddings file not found at {embeddings_path}")
    
    embeddings = np.load(embeddings_path)
    logger.info(f"Loaded embeddings from {embeddings_path} (shape: {embeddings.shape})")
    
    # Load metadata
    metadata_path = base_path / "metadata.json"
    if not metadata_path.exists():
        raise FileNotFoundError(f"Metadata file not found at {metadata_path}")
    
    with open(metadata_path, 'r', encoding='utf-8') as f:
        metadata = json.load(f)
    logger.info(f"Loaded metadata for {len(metadata)} items from {metadata_path}")
    
    # Verify consistency
    if len(embeddings) != len(metadata):
        logger.warning(
            f"Mismatch: {len(embeddings)} embeddings but {len(metadata)} metadata items"
        )
    
    return embeddings, metadata


def load_embedding_info(base_path=None):
    """
    Load embedding information.
    
    Args:
        base_path: base directory path (defaults to Config.VECTOR_STORE_DIR)
    
    Returns:
        dict: Embedding information
    """
    if base_path is None:
        base_path = Config.VECTOR_STORE_DIR
    else:
        base_path = Path(base_path)
    
    info_path = base_path / "embedding_info.json"
    
    if not info_path.exists():
        logger.warning(f"Embedding info file not found at {info_path}")
        return {}
    
    with open(info_path, 'r', encoding='utf-8') as f:
        info = json.load(f)
    
    return info


def embeddings_exist(base_path=None):
    """
    Check if embeddings exist on disk.
    
    Args:
        base_path: base directory path (defaults to Config.VECTOR_STORE_DIR)
    
    Returns:
        bool: True if embeddings exist
    """
    if base_path is None:
        base_path = Config.VECTOR_STORE_DIR
    else:
        base_path = Path(base_path)
    
    embeddings_path = base_path / "embeddings.npy"
    metadata_path = base_path / "metadata.json"
    
    return embeddings_path.exists() and metadata_path.exists()


if __name__ == "__main__":
    # Test save/load functionality
    if embeddings_exist():
        logger.info("Testing load functionality...")
        embeddings, metadata = load_embeddings()
        info = load_embedding_info()
        
        print(f"\nEmbedding Info:")
        print(f"  Number of embeddings: {info.get('num_embeddings')}")
        print(f"  Embedding dimension: {info.get('embedding_dimension')}")
        print(f"  Model: {info.get('model')}")
        
        print(f"\nLoaded Data:")
        print(f"  Embeddings shape: {embeddings.shape}")
        print(f"  Metadata items: {len(metadata)}")
        
        if metadata:
            print(f"\nSample metadata:")
            print(f"  {metadata[0].get('name', 'N/A')}")
    else:
        logger.info("No embeddings found. Run build_embeddings.py first.")

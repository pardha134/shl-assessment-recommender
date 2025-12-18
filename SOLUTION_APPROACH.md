# SHL Assessment Recommender - Solution Approach

**Author:** Pardha Saradhi Thumma  
**Date:** December 18, 2024  
**Project:** GenAI-Powered SHL Assessment Recommendation System

---

## Executive Summary

Developed an AI-powered recommendation system that analyzes hiring requirements and suggests relevant SHL assessments from a catalog of 377 products. The solution leverages Retrieval-Augmented Generation (RAG) architecture combining semantic search with Large Language Models to provide contextually relevant, explainable recommendations.

---

## Problem Statement

Organizations struggle to identify appropriate SHL assessments from a large catalog when hiring for specific roles. The challenge requires:
- Understanding natural language job descriptions
- Matching requirements to relevant assessments
- Providing explainable recommendations
- Delivering results through accessible interfaces (API and Web UI)

---

## Solution Architecture

### 1. Data Collection & Processing

**Web Scraping Pipeline**
- Scraped 377 SHL assessment products from shl.com
- Extracted: product names, descriptions, categories, test types, durations, target roles, skills assessed
- Implemented robust HTML parsing with BeautifulSoup4
- Stored structured data in JSON format

**Text Preprocessing**
- Cleaned and normalized product descriptions
- Removed HTML artifacts and special characters
- Chunked long descriptions (max 512 tokens, 50-token overlap)
- Created embedding-ready text combining all relevant fields

### 2. Vector Store Creation

**Embedding Generation**
- Model: `sentence-transformers/all-MiniLM-L6-v2` (384 dimensions)
- Generated embeddings for all 377 products
- Stored in FAISS vector index for efficient similarity search
- Pre-computed embeddings to optimize deployment size and performance

**Storage Structure**
```
vector_store/shl_faiss/
├── index.faiss          # FAISS vector index
├── embeddings.npy       # 377 x 384 embedding matrix
├── metadata.json        # Product details
└── embedding_info.json  # Configuration
```

### 3. RAG Pipeline Implementation

**Retrieval Component**
- Query processing: Normalize and embed user queries
- Semantic search: FAISS L2 distance similarity
- Top-K retrieval: Configurable (default: 5 results)
- Metadata enrichment: Attach full product details to results

**Generation Component**
- LLM: OpenAI GPT-3.5-turbo
- Temperature: 0.3 (balanced creativity/consistency)
- Prompt engineering: Structured templates for consistent output
- Context injection: Retrieved products formatted for LLM consumption

**Fallback Mechanism**
- Graceful degradation when LLM unavailable
- Returns similarity-based recommendations
- Maintains system availability

### 4. API Development

**FastAPI Backend**
- RESTful endpoints: `/health`, `/recommend`
- Request validation with Pydantic schemas
- CORS middleware for cross-origin access
- Comprehensive error handling

**Response Format**
```json
{
  "recommended_assessments": [
    {
      "url": "string",
      "name": "string",
      "adaptive_support": "Yes/No",
      "description": "string",
      "duration": integer,
      "remote_support": "Yes/No",
      "test_type": ["string"]
    }
  ]
}
```

### 5. Web Interface

**Streamlit Application**
- Interactive UI with query input and results display
- Configurable recommendation count (1-10)
- Caching for optimal performance
- Detailed assessment cards with relevance scores

---

## Technical Implementation

### Key Technologies

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Web Scraping | BeautifulSoup4, Requests | Data collection |
| Embeddings | Sentence-Transformers | Semantic representation |
| Vector Store | FAISS | Fast similarity search |
| LLM | OpenAI GPT-3.5-turbo | Intelligent recommendations |
| Framework | LangChain | RAG orchestration |
| API | FastAPI | RESTful interface |
| Web UI | Streamlit | User interface |
| Deployment | Streamlit Cloud | Cloud hosting |

### Performance Optimizations

1. **Pre-computed Embeddings**: Generated offline to reduce runtime overhead
2. **Lazy Loading**: Components initialized only when needed
3. **Caching**: Streamlit resource caching for recommender instance
4. **Efficient Search**: FAISS IndexFlatL2 for exact similarity search
5. **Batch Processing**: Optimized embedding generation in batches

### Deployment Strategy

**Local Development**
- Environment variables via `.env` file
- Modular architecture for easy testing
- Comprehensive test scripts

**Cloud Deployment (Streamlit Cloud)**
- GitHub integration for automatic deployment
- Secrets management for API keys
- Requirements optimization for 1GB RAM limit
- Vector store files included in repository (~1.3 MB)

---

## Results & Performance

### System Metrics

- **Dataset Size**: 377 SHL assessments
- **Embedding Dimension**: 384
- **Vector Store Size**: 1.3 MB
- **Response Time**: 2-3 seconds (first query), 1-2 seconds (subsequent)
- **Memory Usage**: ~300-500 MB (within Streamlit's 1GB limit)

### Recommendation Quality

- **Semantic Understanding**: Accurately interprets job requirements
- **Relevance**: Top-5 recommendations consistently relevant
- **Explainability**: LLM provides reasoning for each recommendation
- **Fallback Reliability**: Similarity-based results when LLM unavailable

---

## Challenges & Solutions

### Challenge 1: Large Model Size
**Problem**: sentence-transformers model (~4GB) exceeded deployment limits  
**Solution**: Used lightweight model (all-MiniLM-L6-v2, ~90MB) with pre-computed embeddings

### Challenge 2: Vector Store Deployment
**Problem**: Binary files excluded by .gitignore  
**Solution**: Updated .gitignore to include vector store files; verified all files tracked in git

### Challenge 3: Dependency Management
**Problem**: Different requirements for local vs. cloud deployment  
**Solution**: Created separate requirements files (requirements.txt, requirements-streamlit.txt)

### Challenge 4: API Key Security
**Problem**: Secure API key management across environments  
**Solution**: Environment variables locally, Streamlit Secrets for cloud deployment

### Challenge 5: Import Errors
**Problem**: sentence-transformers import failures on Streamlit Cloud  
**Solution**: Implemented lazy initialization; ensured dependency in all requirements files

---

## Key Features

1. **Natural Language Understanding**: Processes free-form job descriptions
2. **Semantic Search**: Goes beyond keyword matching
3. **Intelligent Ranking**: LLM-powered relevance scoring
4. **Explainable AI**: Provides reasoning for recommendations
5. **Dual Interface**: Both API and web UI available
6. **Scalable Architecture**: Modular design for easy extension
7. **Production-Ready**: Error handling, logging, fallback mechanisms

---

## Future Enhancements

1. **Fine-tuned Embeddings**: Domain-specific embedding model for SHL assessments
2. **User Feedback Loop**: Collect ratings to improve recommendations
3. **Multi-language Support**: Extend to non-English job descriptions
4. **Advanced Filtering**: Filter by duration, test type, difficulty level
5. **Batch Processing**: Handle multiple job descriptions simultaneously
6. **Analytics Dashboard**: Track usage patterns and recommendation effectiveness

---

## Conclusion

Successfully developed and deployed a production-ready AI-powered recommendation system that:
- Processes natural language hiring requirements
- Provides relevant, explainable SHL assessment recommendations
- Delivers results through both API and web interfaces
- Operates efficiently within cloud platform constraints
- Maintains high availability with fallback mechanisms

The solution demonstrates effective application of modern AI techniques (RAG, semantic search, LLMs) to solve a real-world business problem, with careful attention to performance, scalability, and user experience.

---

## Repository & Deployment

- **GitHub**: https://github.com/pardha134/shl-assessment-recommender
- **Live Demo**: Deployed on Streamlit Cloud
- **Documentation**: Comprehensive guides for setup, testing, and deployment
- **Code Quality**: Modular, well-documented, production-ready

---

**Total Development Time**: Iterative development with focus on quality and deployment readiness  
**Lines of Code**: ~2,000 (excluding documentation)  
**Test Coverage**: Comprehensive manual testing with multiple query scenarios

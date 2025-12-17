# Add This Section to Your README.md

Add this section at the top of your README.md after uploading to GitHub:

```markdown
# SHL Assessment Recommender

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> GenAI-powered SHL Assessment Recommendation System using RAG (Retrieval-Augmented Generation)

## 🔗 Quick Links

- **GitHub Repository:** https://github.com/YOUR_USERNAME/shl-assessment-recommender
- **API Documentation:** [docs/API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md)
- **Quick Start Guide:** [QUICKSTART.md](QUICKSTART.md)
- **Postman Guide:** [POSTMAN_GUIDE.md](POSTMAN_GUIDE.md)
- **Submission File:** [predictions/Pardha_Saradhi_Thumma.csv](predictions/Pardha_Saradhi_Thumma.csv)

## 📊 Project Stats

- **API Endpoint:** `POST /recommend`
- **Vector Store:** 377 product embeddings
- **Test Queries:** 10 unique queries
- **Products:** 12 SHL assessments
- **Submission:** ✅ Complete

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Start API server
python api/main.py

# Test endpoint
curl -X POST "http://localhost:8000/recommend" \
  -H "Content-Type: application/json" \
  -d '{"query": "Hire software engineers", "top_k": 5}'
```

## 📁 Repository Structure

```
shl-assessment-recommender/
├── api/                          # FastAPI application
│   ├── main.py                  # API server ⭐
│   └── schemas.py               # Request/Response models
├── rag/                          # RAG system
│   ├── recommender.py           # Main recommendation logic
│   ├── retriever.py             # Vector similarity search
│   └── prompt.py                # LLM prompt templates
├── vector_store/                 # FAISS vector store
├── embeddings/                   # Embedding utilities
├── data/                         # Data files
│   ├── processed/
│   │   └── shl_products.json   # 12 SHL products
│   └── test_queries.csv         # Test dataset
├── predictions/                  # Output
│   └── Pardha_Saradhi_Thumma.csv  # Submission file ✅
├── docs/                         # Documentation
├── README.md                     # This file
├── QUICKSTART.md                # Quick start guide
├── requirements.txt             # Dependencies
└── config.py                    # Configuration
```

## 🎯 Key Features

- ✅ **FastAPI REST API** - Production-ready endpoint
- ✅ **RAG System** - Retrieval-Augmented Generation
- ✅ **FAISS Vector Store** - Fast similarity search
- ✅ **LLM Ranking** - GPT-3.5-turbo with fallback
- ✅ **Semantic Search** - Sentence transformers
- ✅ **Comprehensive Docs** - API, setup, and testing guides

## 📝 API Endpoint

**POST** `/recommend`

**Request:**
```json
{
  "query": "Hire software engineers with Python skills",
  "top_k": 5
}
```

**Response:**
```json
{
  "recommended_assessments": [
    {
      "url": "https://www.shl.com/solutions/products/...",
      "name": "Coding Assessment - Python",
      "description": "Practical coding test...",
      "duration": 60,
      "test_type": ["Technical Skills"]
    }
  ]
}
```

## 🔧 Technology Stack

- **Backend:** FastAPI, Python 3.9+
- **Vector Store:** FAISS
- **Embeddings:** Sentence Transformers (all-MiniLM-L6-v2)
- **LLM:** OpenAI GPT-3.5-turbo
- **Data Processing:** Pandas, BeautifulSoup4
- **API Testing:** Postman, cURL

## 📊 Evaluation

- **Test Dataset:** 10 unique job descriptions
- **Evaluation Metrics:** Semantic similarity, relevance scoring
- **Submission File:** `predictions/Pardha_Saradhi_Thumma.csv`
- **Results:** All queries processed successfully

## 📚 Documentation

- [API Documentation](docs/API_DOCUMENTATION.md) - Complete API reference
- [Quick Start Guide](QUICKSTART.md) - Get started in 5 minutes
- [Postman Guide](POSTMAN_GUIDE.md) - API testing with Postman
- [Cleanup Summary](CLEANUP_SUMMARY.md) - Project cleanup details
- [Essential Files](ESSENTIAL_FILES.md) - File structure guide

## 🤝 Contributing

This is a submission project. For questions or issues, please contact:
- **Name:** Pardha Saradhi Thumma
- **Email:** [your-email@example.com]

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- SHL for the assessment catalog
- OpenAI for GPT-3.5-turbo
- FastAPI and FAISS communities

---

**Built with ❤️ for SHL Assessment Recommendation Challenge**
```

---

## Instructions

1. **Copy the content above**
2. **Replace the existing README.md or add sections**
3. **Update YOUR_USERNAME with your GitHub username**
4. **Update your email address**
5. **Commit and push to GitHub**

This will make your repository look professional and complete!

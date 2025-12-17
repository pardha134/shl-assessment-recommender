# Essential Files - Clean Project Structure

## ✅ Core Files Retained

### API (Main Interface)
```
api/
├── main.py          # FastAPI application - START HERE
└── schemas.py       # Request/Response schemas
```

### RAG System (Recommendation Engine)
```
rag/
├── recommender.py   # Main recommendation logic
├── retriever.py     # Vector similarity search
└── prompt.py        # LLM prompt templates
```

### Vector Store (Search Index)
```
vector_store/
├── vector_store.py      # FAISS vector store management
├── query_processor.py   # Query embedding processor
└── shl_faiss/          # Pre-built FAISS index (377 vectors)
    ├── index.faiss
    ├── embeddings.npy
    └── metadata.json
```

### Embeddings (Vector Generation)
```
embeddings/
├── build_embeddings.py  # Create embeddings from products
└── load_embeddings.py   # Load embeddings utilities
```

### Data Processing
```
preprocessing/
├── chunk_products.py    # Split products into chunks
└── clean_text.py        # Text cleaning utilities

scraper/
├── scrape_shl.py       # Web scraping
└── parse_products.py   # Parse scraped data
```

### Data Files
```
data/
├── processed/
│   └── shl_products.json    # 12 SHL products (processed)
└── test_queries.csv         # Test dataset (10 queries)
```

### Predictions
```
predictions/
└── Pardha_Saradhi_Thumma.csv  # Submission file ✅
```

### Configuration & Scripts
```
config.py                    # Configuration management
run_pipeline.py             # Run complete data pipeline
export_predictions.py       # Export predictions utility
generate_submission.py      # Generate submission CSV
requirements.txt            # Python dependencies
.env                       # Environment variables (API keys)
.env.example              # Environment template
```

### Documentation
```
README.md                  # Main documentation
QUICKSTART.md             # Quick start guide
POSTMAN_GUIDE.md          # API testing with Postman
docs/
└── API_DOCUMENTATION.md  # Complete API reference
```

---

## 🚀 Quick Start Commands

### 1. Start API Server
```bash
python api/main.py
```
Server runs at: `http://localhost:8000`

### 2. Test API Endpoint
```bash
curl -X POST "http://localhost:8000/recommend" \
  -H "Content-Type: application/json" \
  -d '{"query": "Hire software engineers", "top_k": 5}'
```

### 3. Generate Submission File
```bash
python generate_submission.py
```
Output: `predictions/Pardha_Saradhi_Thumma.csv`

### 4. Rebuild Pipeline (if needed)
```bash
python run_pipeline.py
```

---

## 📊 File Count Summary

| Category | Count |
|----------|-------|
| API Files | 2 |
| RAG System | 3 |
| Vector Store | 2 + index |
| Embeddings | 2 |
| Data Processing | 4 |
| Data Files | 2 |
| Scripts | 4 |
| Documentation | 4 |
| Configuration | 3 |
| **Total Essential** | **26 files** |

---

## 🗑️ Removed Files

**Total Removed:** 23+ files including:
- Test scripts (3)
- Documentation files (8)
- Deployment files (3)
- Evaluation scripts (4)
- Web app (1)
- Redundant scripts (2)
- Raw data (1)
- Empty directories (3)

---

## ✨ Benefits

1. **Streamlined** - Only essential files remain
2. **Clear Purpose** - Each file has a specific role
3. **Easy Navigation** - Find what you need quickly
4. **Maintained Functionality** - All core features work
5. **Production Ready** - API endpoint fully functional

---

## 📝 Key Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | API info |
| `/health` | GET | Health check |
| `/recommend` | POST | Get recommendations |
| `/docs` | GET | Interactive API docs |

---

## 🎯 Main Workflow

```
1. Query → API (/recommend)
2. API → Query Processor (embed query)
3. Query Processor → Vector Store (similarity search)
4. Vector Store → Retriever (top-k results)
5. Retriever → Recommender (LLM ranking)
6. Recommender → API (JSON response)
7. API → User (recommendations)
```

---

## 💡 Notes

- Vector store is pre-built (no need to rebuild)
- API uses fallback mode if OpenAI quota exceeded
- Submission file already generated
- All dependencies in `requirements.txt`
- Environment variables in `.env`

---

## 🔧 Maintenance

To update the system:
1. Modify product data in `data/processed/shl_products.json`
2. Run `python run_pipeline.py` to rebuild
3. Restart API: `python api/main.py`

---

**Project is now clean, organized, and production-ready! 🎉**

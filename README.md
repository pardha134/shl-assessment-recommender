# SHL Assessment Recommendation Engine

A GenAI-powered system that intelligently recommends appropriate SHL assessments based on natural-language hiring requirements using RAG (Retrieval-Augmented Generation) techniques.

## ✅ Status: Complete and Working

- ✅ **377 Products**: Comprehensive SHL assessment catalog
- ✅ **Semantic Search**: HuggingFace embeddings + FAISS vector store
- ✅ **Balanced Recommendations**: Automatic K/P/S test type balancing
- ✅ **REST API**: FastAPI backend (specification compliant)
- ✅ **Web Interface**: Streamlit UI
- ✅ **Evaluation Framework**: Metrics and quality assessment
- ✅ **Production Ready**: Tested and deployable

## Key Features

- 🔍 **377 SHL Assessments**: Cognitive, Personality, SJT, Technical, Job-Focused
- 🧠 **Semantic Search**: HuggingFace sentence-transformers (384-dim embeddings)
- 🤖 **LLM Reasoning**: LangChain + GPT-3.5-turbo for explainable recommendations
- ⚖️ **Balanced Results**: Automatic K/P/S test type balancing
- 🚀 **REST API**: FastAPI with auto-generated docs
- 💻 **Web Interface**: Interactive Streamlit application
- 📊 **Evaluation**: Precision@K, Recall@K, MRR metrics
- 📥 **CSV Export**: Submission-ready format

## Architecture

```
SHL Website → Scraper → Structured Data → Embeddings → Vector DB
                                  ↑
User Query → Query Embedding → Retriever → LLM → Recommendation
                                  ↓
                       Web App / API Output
```

## Technology Stack

- **Scraping**: Requests, BeautifulSoup
- **Data Storage**: JSON, SQLite
- **Embeddings**: OpenAI / HuggingFace
- **Vector DB**: FAISS
- **LLM & RAG**: LangChain
- **Backend API**: FastAPI
- **Web UI**: Streamlit

## 🌐 Get Public URL (For Deployment/Demo)

**Want a public URL to share?** See **`DEPLOYMENT_STATUS.md`** for:
- ⚡ 2-minute option (Ngrok - temporary URL)
- 🚀 10-minute option (Render - permanent URL)

## Quick Start

### Prerequisites

- Python 3.9+ (3.11 recommended for deployment)
- OpenAI API key (optional - system uses HuggingFace by default)

### Installation & Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure environment (optional for HuggingFace)
cp .env.example .env
# Edit .env if using OpenAI

# 3. System is ready! (377 products already loaded)
# Data pipeline already complete:
# - Products: data/processed/shl_products.json
# - Embeddings: vector_store/shl_faiss/
```

### Verify Installation

```bash
# Test the system
python -c "from rag.retriever import Retriever; r = Retriever(); print(f'✅ System ready with {r.vector_store.get_stats()[\"total_vectors\"]} products')"
```

## Usage

### 1. Console Application (Simplest)

```bash
python console_app.py
```
Interactive command-line interface - just enter a job role and get recommendations!

See `CONSOLE_APP_GUIDE.md` for detailed usage.

### 2. Web Interface (Recommended)

```bash
streamlit run webapp/app.py
```
Visit: http://localhost:8501

### 3. REST API

```bash
python start_api.py
```
Visit: http://localhost:8000/docs (auto-generated documentation)

**Example API Request:**
```bash
curl -X POST "http://localhost:8000/recommend" \
  -H "Content-Type: application/json" \
  -d '{"query": "Hire Java developers who collaborate well"}'
```

**Example Response:**
```json
{
  "recommended_assessments": [
    {
      "url": "https://www.shl.com/solutions/products/coding-assessment---java/",
      "name": "Coding Assessment - Java",
      "adaptive_support": "No",
      "description": "Java programming skills evaluation",
      "duration": 60,
      "remote_support": "Yes",
      "test_type": ["Knowledge & Skills"]
    }
  ]
}
```

### 4. Generate Submission CSV

```bash
python generate_submission_csv.py
```
Creates: `predictions/submission.csv`

## Project Structure

```
shl-assessment-recommender/
├── scraper/              # Web scraping and parsing
├── preprocessing/        # Text cleaning and chunking
├── embeddings/          # Embedding generation
├── vector_store/        # FAISS index storage
├── rag/                 # RAG logic (retriever, recommender)
├── api/                 # FastAPI backend
├── webapp/              # Streamlit UI
├── evaluation/          # Metrics and evaluation
├── data/                # Raw and processed data
├── predictions/         # Output predictions
└── docs/                # Documentation
```

## Evaluation

```bash
# Retrieval metrics (Precision@K, Recall@K, MRR)
python evaluation/retrieval_metrics.py

# LLM quality metrics (Coverage, Diversity, Relevance)
python evaluation/llm_evaluation.py

# Generate comprehensive report
python evaluation/generate_report.py
```

## Deployment

### Quick Deploy (Choose One):

**Option A: Instant Testing (2 minutes)**
```bash
# Start API
python api/main.py

# In new terminal, expose with ngrok
ngrok http 8000
```
Get temporary public URL immediately!

**Option B: Permanent URL (10 minutes)**
1. Push to GitHub
2. Deploy on [Render](https://render.com) (free)
3. Get permanent URL: `https://your-app.onrender.com`

See `QUICK_DEPLOY.md` for step-by-step instructions.

## Documentation

- **PROJECT_STRUCTURE.md** - Complete project structure
- **QUICKSTART.md** - 5-minute setup guide
- **TESTING_GUIDE.md** - How to test queries
- **API_SPECIFICATION_COMPLIANCE.md** - API specification
- **CONSOLE_APP_GUIDE.md** - Console app usage
- **docs/SETUP_GUIDE.md** - Detailed setup instructions
- **docs/API_DOCUMENTATION.md** - API reference
- **docs/DEPLOYMENT.md** - Deployment guide
- **docs/APPROACH_DOCUMENT.md** - Technical approach

## System Stats

- **Products**: 377 SHL assessments
- **Embeddings**: 384-dimensional (HuggingFace)
- **Vector Store**: FAISS IndexFlatL2
- **Response Time**: <1 second
- **Memory**: ~500MB

## License

MIT License

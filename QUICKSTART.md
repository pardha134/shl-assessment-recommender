# Quick Start Guide

Get the SHL Assessment Recommender up and running in 5 minutes!

## Prerequisites

- Python 3.9+
- OpenAI API key

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Key

Create `.env` file:

```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:

```env
OPENAI_API_KEY=sk-your-actual-key-here
```

### 3. Run Setup Pipeline

```bash
python run_pipeline.py
```

This will:
- ✅ Scrape sample SHL product data
- ✅ Parse and process products
- ✅ Generate embeddings
- ✅ Build vector store
- ✅ Test the system

**Note:** This step requires an OpenAI API key and will make API calls (~$0.10-0.50 one-time cost).

## Usage

### Option 1: Console Application (Simplest)

```bash
python console_app.py
```

Interactive command-line interface - just type a job role and get recommendations!

Example:
```
Enter job role: Java Developer
Number of recommendations: 5
```

See `CONSOLE_APP_GUIDE.md` for more details.

### Option 2: Web Interface (Recommended)

```bash
streamlit run webapp/app.py
```

Open http://localhost:8501 in your browser.

### Option 3: API

```bash
python start_api.py
```

API available at http://localhost:8000

Test with:
```bash
curl -X POST "http://localhost:8000/recommend" \
  -H "Content-Type: application/json" \
  -d '{"query": "Hire fresh graduates for software engineering roles"}'
```

### Option 4: Python Code

```python
from rag.recommender import Recommender

recommender = Recommender()
result = recommender.recommend("Hire software engineers")

for rec in result['recommendations']:
    print(f"{rec['assessment_name']}: {rec['relevance_score']}/10")
```

## Example Queries

Try these in the web interface or API:

- "Hire fresh graduates for software engineering roles"
- "Assessment for senior leadership positions"
- "Customer service skills evaluation"
- "Technical coding test for Python developers"
- "Personality assessment for sales team"

## Next Steps

- 📊 **Run Evaluation**: `python evaluation/retrieval_metrics.py`
- 📥 **Export Predictions**: `python export_predictions.py`
- 📖 **Read Full Docs**: See `docs/` folder
- 🚀 **Deploy**: See `docs/DEPLOYMENT.md`

## Troubleshooting

### "OPENAI_API_KEY not found"
→ Make sure `.env` file exists with your API key

### "Vector store not found"
→ Run `python run_pipeline.py` to generate it

### "Module not found"
→ Run `pip install -r requirements.txt`

## Support

- 📖 Full documentation in `docs/` folder
- 🐛 Issues: Open an issue on GitHub
- 💬 Questions: Check README.md

## What's Next?

1. ✅ System is running
2. 🎯 Try different queries
3. 📊 Check evaluation metrics
4. 🚀 Deploy to production
5. 🔧 Customize for your needs

Happy recommending! 🧠✨

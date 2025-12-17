# GitHub Repository Setup Guide

## Step-by-Step Instructions to Upload Your Code

### Option 1: Using GitHub Desktop (Easiest)

1. **Download GitHub Desktop**
   - Go to: https://desktop.github.com/
   - Install and sign in with your GitHub account

2. **Create New Repository**
   - Click "File" → "New Repository"
   - Name: `shl-assessment-recommender`
   - Description: `GenAI-powered SHL Assessment Recommendation System using RAG`
   - Local Path: Choose your current project folder
   - Click "Create Repository"

3. **Publish to GitHub**
   - Click "Publish repository"
   - Choose public or private
   - Click "Publish repository"

4. **Your GitHub URL will be:**
   ```
   https://github.com/YOUR_USERNAME/shl-assessment-recommender
   ```

---

### Option 2: Using Git Command Line

1. **Initialize Git Repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: SHL Assessment Recommender with RAG"
   ```

2. **Create Repository on GitHub**
   - Go to: https://github.com/new
   - Repository name: `shl-assessment-recommender`
   - Description: `GenAI-powered SHL Assessment Recommendation System using RAG`
   - Choose Public or Private
   - Do NOT initialize with README (you already have one)
   - Click "Create repository"

3. **Push to GitHub**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/shl-assessment-recommender.git
   git branch -M main
   git push -u origin main
   ```

4. **Your GitHub URL will be:**
   ```
   https://github.com/YOUR_USERNAME/shl-assessment-recommender
   ```

---

### Option 3: Using GitHub Web Interface

1. **Create a ZIP file of your project**
   - Exclude: `__pycache__`, `.env`, `vector_store/shl_faiss/` (large files)

2. **Go to GitHub**
   - Visit: https://github.com/new
   - Create new repository: `shl-assessment-recommender`

3. **Upload Files**
   - Click "uploading an existing file"
   - Drag and drop your files
   - Commit changes

---

## Important: Files to Exclude from GitHub

Create/update `.gitignore` to exclude sensitive and large files:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/

# Environment variables
.env

# Large files
vector_store/shl_faiss/*.faiss
vector_store/shl_faiss/*.npy

# IDE
.vscode/
.idea/
.kiro/

# OS
.DS_Store
Thumbs.db

# Predictions (optional - include if you want to show results)
# predictions/*.csv
```

---

## Repository Structure for GitHub

Your repository will contain:

```
shl-assessment-recommender/
├── api/                          # FastAPI application
├── rag/                          # RAG system
├── vector_store/                 # Vector store (without large files)
├── embeddings/                   # Embedding utilities
├── preprocessing/                # Data preprocessing
├── scraper/                      # Web scraping
├── data/                         # Data files
├── predictions/                  # Predictions output
├── docs/                         # Documentation
├── README.md                     # Main documentation
├── QUICKSTART.md                # Quick start guide
├── requirements.txt             # Dependencies
├── config.py                    # Configuration
├── .gitignore                   # Git ignore rules
└── .env.example                 # Environment template
```

---

## What to Include in Your Submission

### 1. GitHub Repository URL
```
https://github.com/YOUR_USERNAME/shl-assessment-recommender
```

### 2. Key Features to Highlight

**Implementation:**
- ✅ FastAPI REST API endpoint
- ✅ RAG (Retrieval-Augmented Generation) system
- ✅ FAISS vector store with 377 embeddings
- ✅ LLM-based ranking with fallback mode
- ✅ Semantic search using sentence transformers

**Evaluation:**
- ✅ Test dataset: 10 unique queries
- ✅ Predictions generated: `predictions/Pardha_Saradhi_Thumma.csv`
- ✅ Vector similarity scoring
- ✅ Retrieval metrics available

### 3. Documentation Included
- README.md - Complete project overview
- QUICKSTART.md - Quick start guide
- POSTMAN_GUIDE.md - API testing guide
- docs/API_DOCUMENTATION.md - Full API reference
- CLEANUP_SUMMARY.md - Project cleanup details
- ESSENTIAL_FILES.md - File structure guide

---

## README.md Highlights

Your README.md already includes:
- ✅ Project overview
- ✅ Features and architecture
- ✅ Installation instructions
- ✅ API usage examples
- ✅ Technology stack
- ✅ Project structure
- ✅ Evaluation approach

---

## After Uploading to GitHub

### Update README with Your GitHub URL

Add this section to your README.md:

```markdown
## 🔗 Links

- **GitHub Repository:** https://github.com/YOUR_USERNAME/shl-assessment-recommender
- **API Documentation:** [docs/API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md)
- **Quick Start:** [QUICKSTART.md](QUICKSTART.md)
- **Submission File:** [predictions/Pardha_Saradhi_Thumma.csv](predictions/Pardha_Saradhi_Thumma.csv)
```

### Add Badges (Optional)

```markdown
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
```

---

## Submission Checklist

- [ ] Code uploaded to GitHub
- [ ] README.md is complete and clear
- [ ] .env.example included (not .env)
- [ ] requirements.txt is up to date
- [ ] API endpoint is documented
- [ ] Predictions file is included
- [ ] Documentation is comprehensive
- [ ] .gitignore excludes sensitive files
- [ ] Repository is public (if required)

---

## Sample Submission Format

**Name:** Pardha Saradhi Thumma

**GitHub URL:** https://github.com/YOUR_USERNAME/shl-assessment-recommender

**API Endpoint:** POST /recommend

**Submission File:** predictions/Pardha_Saradhi_Thumma.csv

**Key Features:**
- RAG-based recommendation system
- FastAPI REST API
- FAISS vector store
- LLM ranking with GPT-3.5-turbo
- Semantic search with sentence transformers

**Documentation:**
- Complete API documentation
- Quick start guide
- Postman testing guide
- Evaluation approach

---

## Need Help?

If you encounter issues:

1. **Large Files Error:**
   - Use Git LFS for large files
   - Or exclude them in .gitignore

2. **Authentication Issues:**
   - Use GitHub Personal Access Token
   - Or use GitHub Desktop

3. **Repository Already Exists:**
   - Use a different name
   - Or delete the existing repository

---

## Next Steps

1. Choose one of the upload methods above
2. Create your GitHub repository
3. Upload your code
4. Get your GitHub URL
5. Submit the URL

**Your GitHub URL will look like:**
```
https://github.com/YOUR_USERNAME/shl-assessment-recommender
```

Replace `YOUR_USERNAME` with your actual GitHub username.

---

Good luck with your submission! 🚀

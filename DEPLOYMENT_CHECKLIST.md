# Deployment Checklist ✅

## Pre-Deployment Checks

### 1. Local Testing
- [ ] API runs locally: `python api/main.py`
- [ ] Health endpoint works: `http://localhost:8000/health`
- [ ] Recommend endpoint works: `http://localhost:8000/docs`
- [ ] Test script passes: `python test_api_local.py`

### 2. Required Files Present
- [ ] `requirements-api.txt` exists
- [ ] `Procfile` exists
- [ ] `runtime.txt` exists (Python 3.11.9)
- [ ] `render.yaml` exists
- [ ] `vector_store/shl_faiss/` directory exists with files:
  - [ ] `index.faiss`
  - [ ] `metadata.json`
  - [ ] `embeddings.npy`
  - [ ] `embedding_info.json`
- [ ] `data/processed/shl_products.json` exists

### 3. Environment Configuration
- [ ] `.env` file has valid `OPENAI_API_KEY`
- [ ] API key is ready to add to Render dashboard
- [ ] `.gitignore` excludes `.env` (but NOT vector_store/)

### 4. Git Repository
- [ ] All files committed: `git status`
- [ ] Pushed to GitHub: `git push origin main`
- [ ] Repository is public or Render has access

---

## Deployment Options

### Option A: Ngrok (Instant - 2 minutes)

**Steps:**
1. [ ] Download ngrok: https://ngrok.com/download
2. [ ] Start API: `python api/main.py`
3. [ ] Run ngrok: `ngrok http 8000`
4. [ ] Copy public URL
5. [ ] Test: Visit `https://your-url.ngrok-free.app/docs`

**Result**: ✅ Temporary public URL

---

### Option B: Render (Permanent - 10 minutes)

**Steps:**
1. [ ] Sign up at https://render.com
2. [ ] Click "New +" → "Web Service"
3. [ ] Connect GitHub repository
4. [ ] Configure:
   - [ ] Name: `shl-recommender-api`
   - [ ] Build Command: `pip install --upgrade pip && pip install -r requirements-api.txt`
   - [ ] Start Command: `uvicorn api.main:app --host 0.0.0.0 --port $PORT`
5. [ ] Add environment variables:
   - [ ] `OPENAI_API_KEY` = (your key from .env)
   - [ ] `PYTHON_VERSION` = `3.11.9`
6. [ ] Click "Create Web Service"
7. [ ] Wait for build (5-10 minutes)
8. [ ] Verify deployment successful

**Result**: ✅ Permanent URL at `https://shl-recommender-api.onrender.com`

---

## Post-Deployment Testing

### Test Endpoints:

1. [ ] **Root endpoint**:
   ```bash
   curl https://your-url/
   ```
   Expected: `{"message": "SHL Assessment Recommender API", ...}`

2. [ ] **Health check**:
   ```bash
   curl https://your-url/health
   ```
   Expected: `{"status": "healthy"}`

3. [ ] **Recommendations**:
   ```bash
   curl -X POST "https://your-url/recommend" \
     -H "Content-Type: application/json" \
     -d '{"query": "Hire Java developers", "top_k": 3}'
   ```
   Expected: JSON with `recommended_assessments` array

4. [ ] **Interactive docs**:
   - Visit: `https://your-url/docs`
   - Try "Try it out" on `/recommend` endpoint

---

## Common Issues & Solutions

### ❌ Build fails with "pandas compilation error"
**Solution**: Ensure `PYTHON_VERSION` = `3.11.9` (not 3.13)

### ❌ "Vector store not found"
**Solution**: 
- Check `vector_store/shl_faiss/` is in git
- Run: `git add vector_store/shl_faiss/`
- Commit and push

### ❌ "OpenAI API key not found"
**Solution**: Add `OPENAI_API_KEY` in Render environment variables

### ❌ "Module not found" errors
**Solution**: Ensure using `requirements-api.txt` (not `requirements.txt`)

### ❌ Slow first request (30-60 seconds)
**Solution**: Normal for Render free tier - app sleeps after inactivity

---

## Final Steps

1. [ ] Update README.md with live URL
2. [ ] Test all endpoints work
3. [ ] Share URL with team/evaluators
4. [ ] Monitor logs for any errors

---

## Your Deployed URLs

**Ngrok (Temporary)**:
```
https://____________.ngrok-free.app
```

**Render (Permanent)**:
```
https://shl-recommender-api.onrender.com
```

**API Documentation**:
```
https://your-url/docs
```

---

## Success Criteria

✅ API is publicly accessible
✅ Health endpoint returns 200
✅ Recommend endpoint returns valid recommendations
✅ Interactive docs work
✅ URL can be shared with others

---

## Need Help?

- Quick guide: `GET_PUBLIC_URL.md`
- Detailed guide: `DEPLOYMENT_GUIDE.md`
- Full guide: `QUICK_DEPLOY.md`

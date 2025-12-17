# How to Get Your Public API URL

## 🚀 Two Options Available

---

## Option 1: INSTANT (2 Minutes) - Ngrok

**Best for**: Quick testing, immediate demo

### Steps:

1. **Download Ngrok**: https://ngrok.com/download

2. **Start your API**:
   ```bash
   python api/main.py
   ```
   Wait for: `Uvicorn running on http://0.0.0.0:8000`

3. **Open NEW terminal and run**:
   ```bash
   ngrok http 8000
   ```

4. **Copy the URL** from ngrok output:
   ```
   Forwarding: https://abc123.ngrok-free.app -> http://localhost:8000
   ```

5. **Your API is live!**
   - Docs: `https://abc123.ngrok-free.app/docs`
   - Health: `https://abc123.ngrok-free.app/health`

**Note**: URL changes each time you restart ngrok (free tier)

---

## Option 2: PERMANENT (10 Minutes) - Render

**Best for**: Production, permanent demo URL

### Steps:

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Deploy to Render"
   git push origin main
   ```

2. **Go to Render**:
   - Visit: https://render.com
   - Sign up (free)
   - Click "New +" → "Web Service"

3. **Connect Repository**:
   - Select your GitHub repo
   - Click "Connect"

4. **Configure**:
   - **Name**: `shl-recommender-api`
   - **Environment**: Python 3
   - **Build Command**: 
     ```
     pip install --upgrade pip && pip install -r requirements-api.txt
     ```
   - **Start Command**: 
     ```
     uvicorn api.main:app --host 0.0.0.0 --port $PORT
     ```

5. **Add Environment Variables** (click "Advanced"):
   - Variable 1:
     - Key: `OPENAI_API_KEY`
     - Value: `[Paste your OpenAI API key from .env file]`
   - Variable 2:
     - Key: `PYTHON_VERSION`
     - Value: `3.11.9`

6. **Deploy**:
   - Click "Create Web Service"
   - Wait 5-10 minutes for build

7. **Get Your URL**:
   - Once deployed: `https://shl-recommender-api.onrender.com`
   - Docs: `https://shl-recommender-api.onrender.com/docs`

---

## Testing Your Deployed API

### Test Health:
```bash
curl https://your-url/health
```

### Test Recommendations:
```bash
curl -X POST "https://your-url/recommend" \
  -H "Content-Type: application/json" \
  -d '{"query": "Hire Java developers", "top_k": 3}'
```

### Interactive Docs:
Visit: `https://your-url/docs`

---

## Comparison

| Feature | Ngrok | Render |
|---------|-------|--------|
| **Setup Time** | 2 min | 10 min |
| **URL** | Temporary | Permanent |
| **Uptime** | While running | 24/7 |
| **Cost** | Free | Free |
| **Best For** | Testing | Production |

---

## Troubleshooting

### Ngrok Issues:

**"command not found"**
- Download from: https://ngrok.com/download
- Or install: `choco install ngrok` (Windows)

**"Failed to connect"**
- Make sure API is running first: `python api/main.py`

### Render Issues:

**Build fails with pandas error**
- Ensure `PYTHON_VERSION` = `3.11.9` in environment variables

**"Vector store not found"**
- Make sure `vector_store/shl_faiss/` is committed to git
- Check `.gitignore` doesn't exclude it

**"OpenAI API key not found"**
- Add `OPENAI_API_KEY` in Render dashboard environment variables

**Slow first request (30-60 seconds)**
- Normal for Render free tier (app sleeps after inactivity)

---

## Recommended Approach

1. **Start with Ngrok** (2 min) - Test everything works
2. **Then deploy to Render** (10 min) - Get permanent URL
3. **Share the Render URL** - Professional and permanent

---

## Need Help?

- Ngrok Docs: https://ngrok.com/docs
- Render Docs: https://render.com/docs
- This project's deployment guide: `DEPLOYMENT_GUIDE.md`

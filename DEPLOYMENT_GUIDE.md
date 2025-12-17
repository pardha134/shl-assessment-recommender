# Deployment Guide - SHL Assessment Recommender API

## ⚠️ Important: Python Version Compatibility

This project requires **Python 3.11** (not 3.13) due to pandas compatibility issues.

## Quick Deploy Options

### Option 1: Render (Recommended - Free Tier)

**Steps:**

1. **Push to GitHub** (if not already done):
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Deploy on Render**:
   - Go to https://render.com and sign up/login
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name**: shl-recommender-api
     - **Environment**: Python 3
     - **Python Version**: 3.11.9 (in Environment Variables)
     - **Build Command**: `pip install --upgrade pip && pip install -r requirements-api.txt`
     - **Start Command**: `uvicorn api.main:app --host 0.0.0.0 --port $PORT`
   - Add Environment Variables:
     - **Key**: `OPENAI_API_KEY`
     - **Value**: Your OpenAI API key (from .env file)
     - **Key**: `PYTHON_VERSION`
     - **Value**: `3.11.9`
   - Click "Create Web Service"

3. **Your API will be live at**: `https://shl-recommender-api.onrender.com`

**Note**: Free tier may spin down after inactivity (takes ~30 seconds to wake up).

**Build Time**: First deployment takes 5-10 minutes.

---

### Option 2: Railway (Fast & Easy)

**Steps:**

1. **Deploy**:
   - Go to https://railway.app
   - Click "Start a New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway auto-detects Python and deploys

2. **Add Environment Variables**:
   - Go to your project → Variables
   - Add: `OPENAI_API_KEY` = your key

3. **Get your URL**:
   - Go to Settings → Generate Domain
   - Your API will be at: `https://your-app.up.railway.app`

---

### Option 3: Ngrok (Instant Testing - Temporary)

**For immediate testing without deployment:**

1. **Install Ngrok**:
   - Download from https://ngrok.com/download
   - Or: `choco install ngrok` (Windows)

2. **Start your API locally**:
   ```bash
   python api/main.py
   ```

3. **In another terminal, expose it**:
   ```bash
   ngrok http 8000
   ```

4. **Copy the public URL** (e.g., `https://abc123.ngrok.io`)

**Note**: URL changes each time you restart ngrok (free tier).

---

### Option 4: Vercel (Serverless)

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Deploy**:
   ```bash
   vercel
   ```

3. **Add environment variables** in Vercel dashboard

---

## Testing Your Deployed API

Once deployed, test with:

```bash
# Replace with your actual URL
curl -X POST "https://your-app-url.com/recommend" \
  -H "Content-Type: application/json" \
  -d '{"query": "Hire Java developers", "top_k": 3}'
```

Or visit: `https://your-app-url.com/docs` for interactive API documentation.

---

## Troubleshooting

### Issue: "Vector store not found"
**Solution**: Ensure `vector_store/shl_faiss/` directory is included in deployment.

### Issue: "OpenAI API key not found"
**Solution**: Add `OPENAI_API_KEY` environment variable in your platform's dashboard.

### Issue: Cold starts (Render free tier)
**Solution**: First request may take 30-60 seconds. Upgrade to paid tier for always-on.

### Issue: Large file size
**Solution**: Ensure `.gitignore` excludes unnecessary files like `__pycache__`, `.env`.

---

## Recommended: Render Free Tier

For this project, **Render** is recommended because:
- ✅ Free tier available
- ✅ Easy GitHub integration
- ✅ Automatic deployments
- ✅ Built-in HTTPS
- ✅ Environment variable management
- ✅ Logs and monitoring

**Estimated deployment time**: 5-10 minutes

---

## Next Steps After Deployment

1. Test the `/health` endpoint
2. Test the `/recommend` endpoint with sample queries
3. Share the URL: `https://your-app.onrender.com`
4. Monitor logs for any issues
5. Update README with your live URL

---

## Need Help?

- Render Docs: https://render.com/docs
- Railway Docs: https://docs.railway.app
- Ngrok Docs: https://ngrok.com/docs

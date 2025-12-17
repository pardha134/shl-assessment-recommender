# Quick Deployment - Get Your API URL in 5 Minutes

## Option A: Instant Testing with Ngrok (Fastest)

**Get a public URL in 2 minutes:**

1. **Download Ngrok**:
   - Windows: https://ngrok.com/download
   - Or use: `choco install ngrok`

2. **Start API locally**:
   ```bash
   python api/main.py
   ```

3. **In a NEW terminal, expose it**:
   ```bash
   ngrok http 8000
   ```

4. **Copy your public URL** from the ngrok output:
   ```
   Forwarding: https://abc123.ngrok-free.app -> http://localhost:8000
   ```

5. **Test it**:
   ```bash
   curl https://your-ngrok-url.ngrok-free.app/health
   ```

**Your API is now publicly accessible!**

Visit: `https://your-ngrok-url.ngrok-free.app/docs`

⚠️ **Note**: Free ngrok URLs change each restart. For permanent URLs, use Render below.

---

## Option B: Permanent URL with Render (10 minutes)

**Get a permanent URL that stays online:**

### Step 1: Prepare Your Repository

```bash
# Make sure everything is committed
git add .
git commit -m "Ready for deployment"
git push origin main
```

### Step 2: Deploy on Render

1. Go to **https://render.com** (sign up free)
2. Click **"New +"** → **"Web Service"**
3. Connect your **GitHub repository**
4. Fill in:
   - **Name**: `shl-recommender-api`
   - **Environment**: `Python 3`
   - **Build Command**: 
     ```
     pip install --upgrade pip && pip install -r requirements-api.txt
     ```
   - **Start Command**: 
     ```
     uvicorn api.main:app --host 0.0.0.0 --port $PORT
     ```

5. **Add Environment Variables** (click "Advanced"):
   - `OPENAI_API_KEY` = `[Your OpenAI API key from .env file]`
   - `PYTHON_VERSION` = `3.11.9`

6. Click **"Create Web Service"**

### Step 3: Wait for Build (5-10 minutes)

Watch the logs. When you see:
```
Your service is live 🎉
```

### Step 4: Get Your URL

Your API is now live at:
```
https://shl-recommender-api.onrender.com
```

### Step 5: Test It

```bash
# Health check
curl https://shl-recommender-api.onrender.com/health

# Get recommendations
curl -X POST "https://shl-recommender-api.onrender.com/recommend" \
  -H "Content-Type: application/json" \
  -d '{"query": "Hire Java developers", "top_k": 3}'
```

Visit the interactive docs:
```
https://shl-recommender-api.onrender.com/docs
```

---

## Troubleshooting

### Build fails with "pandas compilation error"
**Solution**: Make sure `PYTHON_VERSION` is set to `3.11.9` (not 3.13)

### "Vector store not found" error
**Solution**: Ensure `vector_store/shl_faiss/` folder is committed to git

### "OpenAI API key not found"
**Solution**: Add `OPENAI_API_KEY` in Render environment variables

### Render free tier sleeps after inactivity
**Solution**: First request takes 30-60 seconds to wake up. This is normal for free tier.

---

## Which Option Should I Use?

| Feature | Ngrok | Render |
|---------|-------|--------|
| Setup Time | 2 minutes | 10 minutes |
| URL Type | Temporary | Permanent |
| Cost | Free | Free |
| Uptime | While running | 24/7 |
| Best For | Quick testing | Production/Demo |

**Recommendation**: 
- Use **Ngrok** if you need a URL RIGHT NOW for testing
- Use **Render** if you need a permanent URL to share

---

## Next Steps

Once deployed, share your URL:
- API Docs: `https://your-url/docs`
- Health Check: `https://your-url/health`
- Recommendations: `POST https://your-url/recommend`

Update your README.md with the live URL!

# 🚀 Deploy to Render - Complete Guide

## Why Render Instead of Railway?

Your app's Docker image is **8.6 GB** (due to ML models in sentence-transformers), which exceeds:
- ❌ Railway free tier: 4 GB limit
- ✅ Render free tier: More flexible with image sizes

**Render is the better choice for ML/AI applications!**

---

## Prerequisites

✅ Your GitHub repo: `https://github.com/pardha134/shl-assessment-recommender`
✅ Your OpenAI API key (in `.env` file)

---

## Step-by-Step Deployment (10 Minutes)

### Step 1: Sign Up for Render (2 minutes)

1. Go to: **https://render.com**
2. Click **"Get Started"**
3. Sign up with **GitHub** (easiest option)
4. Authorize Render to access your repositories

---

### Step 2: Create New Web Service (2 minutes)

1. Click **"New +"** button (top right)
2. Select **"Web Service"**
3. Click **"Connect account"** if needed
4. Find and select: **`pardha134/shl-assessment-recommender`**
5. Click **"Connect"**

---

### Step 3: Configure Service (3 minutes)

Fill in these settings:

**Basic Settings:**
- **Name**: `shl-recommender-api` (or your choice)
- **Region**: Choose closest to you
- **Branch**: `main`
- **Root Directory**: Leave blank
- **Runtime**: `Python 3`

**Build Settings:**
- **Build Command**: 
  ```
  pip install --upgrade pip && pip install -r requirements.txt
  ```

- **Start Command**:
  ```
  uvicorn api.main:app --host 0.0.0.0 --port $PORT
  ```

**Instance Type:**
- Select **"Free"** (for now)

---

### Step 4: Add Environment Variables (2 minutes)

Scroll down to **"Environment Variables"** section:

Click **"Add Environment Variable"** and add these:

**Variable 1:**
- **Key**: `OPENAI_API_KEY`
- **Value**: Open your `.env` file and copy the key (starts with `sk-proj-`)

**Variable 2:**
- **Key**: `PYTHON_VERSION`
- **Value**: `3.11.9`

**Variable 3:**
- **Key**: `PORT`
- **Value**: `8000`

---

### Step 5: Deploy! (1 minute)

1. Click **"Create Web Service"** button at the bottom
2. Render will start building your app
3. Watch the logs in real-time

---

## Build Process (5-10 Minutes)

You'll see logs like:
```
==> Cloning from https://github.com/pardha134/shl-assessment-recommender...
==> Installing dependencies...
==> Building...
==> Starting service...
✅ Your service is live 🎉
```

**Note**: First build takes 5-10 minutes due to ML model downloads. Be patient!

---

## Get Your Public URL

Once deployed:

1. Look at the top of your service page
2. You'll see a URL like:
   ```
   https://shl-recommender-api.onrender.com
   ```
3. **Copy this URL!**

---

## Test Your Deployed API

### 1. Health Check
```bash
curl https://shl-recommender-api.onrender.com/health
```

Expected response:
```json
{"status": "healthy"}
```

### 2. Interactive API Docs
Visit in browser:
```
https://shl-recommender-api.onrender.com/docs
```

You should see Swagger UI with all your endpoints!

### 3. Get Recommendations
```bash
curl -X POST "https://shl-recommender-api.onrender.com/recommend" \
  -H "Content-Type: application/json" \
  -d '{"query": "Hire Java developers with teamwork skills", "top_k": 3}'
```

---

## Important: Free Tier Limitations

⚠️ **Render Free Tier:**
- ✅ Handles large images (8+ GB)
- ⚠️ Spins down after 15 minutes of inactivity
- ⚠️ First request after sleep takes 30-60 seconds to wake up
- ✅ 750 hours/month free

**For production/demos**: Consider upgrading to paid tier ($7/month) for always-on service.

---

## Troubleshooting

### Build Takes Too Long
- Normal for ML apps! First build: 5-10 minutes
- Subsequent builds: 3-5 minutes (cached)

### "Service Unavailable" on First Request
- Free tier sleeps after inactivity
- Wait 30-60 seconds for it to wake up
- Refresh the page

### Build Fails
- Check logs for specific error
- Verify environment variables are set
- Ensure `requirements.txt` is correct

### "Vector store not found"
- Make sure `vector_store/shl_faiss/` is in GitHub
- Check: https://github.com/pardha134/shl-assessment-recommender/tree/main/vector_store

---

## Monitoring Your App

In Render dashboard:

1. **Logs** - Real-time application logs
2. **Metrics** - CPU, memory, bandwidth usage
3. **Events** - Deployment history
4. **Settings** - Update configuration

---

## Auto-Deploy on Git Push

Render automatically redeploys when you push to GitHub!

```bash
# Make changes
git add .
git commit -m "Update API"
git push origin main

# Render automatically redeploys!
```

---

## Upgrade Options

If you need better performance:

**Starter Plan ($7/month):**
- ✅ Always-on (no sleep)
- ✅ Faster response times
- ✅ More resources
- ✅ Better for demos/production

To upgrade:
1. Go to your service → **"Settings"**
2. Scroll to **"Instance Type"**
3. Select **"Starter"**
4. Confirm

---

## Comparison: Render vs Railway

| Feature | Render | Railway |
|---------|--------|---------|
| **Image Size Limit** | ✅ Flexible (8+ GB) | ❌ 4 GB (free tier) |
| **ML/AI Apps** | ✅ Perfect | ❌ Too restrictive |
| **Free Tier** | ✅ 750 hrs/month | ✅ $5 credit |
| **Sleep Behavior** | ⚠️ Sleeps after 15 min | ✅ No sleep |
| **Build Time** | ⚠️ Slower | ✅ Faster |
| **Best For** | ML/AI apps | Small APIs |

**For your SHL Assessment API with ML models: Render is the right choice!**

---

## Success Checklist

- [ ] Render account created
- [ ] GitHub repository connected
- [ ] Service configured with correct commands
- [ ] 3 environment variables added
- [ ] Build completed successfully
- [ ] Public URL obtained
- [ ] Health endpoint returns 200
- [ ] API docs accessible
- [ ] Recommend endpoint works

---

## Your Deployed URLs

Once live, save these:

- **API Base**: `https://shl-recommender-api.onrender.com`
- **Health**: `https://shl-recommender-api.onrender.com/health`
- **Docs**: `https://shl-recommender-api.onrender.com/docs`
- **Recommend**: `https://shl-recommender-api.onrender.com/recommend`

---

## Next Steps

1. ✅ Deploy to Render (follow steps above)
2. ✅ Test all endpoints
3. ✅ Share your URL
4. ✅ Update README with live URL
5. ✅ Consider upgrading if you need always-on

---

## Need Help?

- Render Docs: https://render.com/docs
- Render Community: https://community.render.com
- This project's guide: `DEPLOYMENT_GUIDE.md`

---

## Estimated Timeline

- ⏱️ Sign up: 2 minutes
- ⏱️ Configure: 3 minutes
- ⏱️ First build: 5-10 minutes
- ⏱️ **Total: ~15 minutes**

**You'll have a working public URL in about 15 minutes!** 🎉

---

## Why This Works

✅ Render handles large Docker images (8+ GB)
✅ Perfect for ML/AI applications
✅ Free tier is generous
✅ Auto-deploys on git push
✅ Professional and reliable

**Render is designed for apps like yours!** 🚀

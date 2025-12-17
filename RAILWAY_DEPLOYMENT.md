# Deploy to Railway - Complete Guide

## Why Railway?

✅ **Faster deployment** than Render (5 minutes vs 10 minutes)
✅ **Auto-detects** Python apps
✅ **Simpler setup** - fewer configuration steps
✅ **Free tier** with $5 credit/month
✅ **Better performance** on free tier

---

## Prerequisites

1. ✅ GitHub repository: `https://github.com/pardha134/shl-assessment-recommender`
2. ✅ OpenAI API key (from your `.env` file)
3. ✅ Railway account (free - we'll create this)

---

## Step-by-Step Deployment

### Step 1: Push Your Code to GitHub

First, make sure all deployment files are on GitHub:

```bash
git add .
git commit -m "Ready for Railway deployment"
git push origin main
```

Verify at: https://github.com/pardha134/shl-assessment-recommender

---

### Step 2: Sign Up for Railway

1. Go to: **https://railway.app**
2. Click **"Login"** or **"Start a New Project"**
3. Sign in with **GitHub** (easiest option)
4. Authorize Railway to access your repositories

---

### Step 3: Create New Project

1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose: **`pardha134/shl-assessment-recommender`**
4. Click **"Deploy Now"**

Railway will automatically:
- ✅ Detect it's a Python app
- ✅ Find your `Procfile`
- ✅ Install dependencies from `requirements-api.txt`
- ✅ Start your API

---

### Step 4: Add Environment Variables

1. In your Railway project, click on your service
2. Go to **"Variables"** tab
3. Click **"+ New Variable"**
4. Add these variables:

**Variable 1:**
- **Key**: `OPENAI_API_KEY`
- **Value**: `[Paste your OpenAI API key from .env file]`

**Variable 2:**
- **Key**: `PYTHON_VERSION`
- **Value**: `3.11.9`

**Variable 3:**
- **Key**: `PORT`
- **Value**: `8000`

5. Click **"Add"** for each variable

---

### Step 5: Configure Build Settings (Optional)

Railway should auto-detect everything, but if needed:

1. Go to **"Settings"** tab
2. Under **"Build"**:
   - **Build Command**: `pip install --upgrade pip && pip install -r requirements-api.txt`
   - **Start Command**: `uvicorn api.main:app --host 0.0.0.0 --port $PORT`

3. Under **"Deploy"**:
   - **Python Version**: `3.11.9`

---

### Step 6: Generate Public URL

1. Go to **"Settings"** tab
2. Scroll to **"Networking"** section
3. Click **"Generate Domain"**
4. Railway will create a public URL like:
   ```
   https://shl-assessment-recommender-production.up.railway.app
   ```

---

### Step 7: Wait for Deployment

Watch the **"Deployments"** tab:
- You'll see build logs in real-time
- Wait for: ✅ **"Success"** status
- Usually takes **3-5 minutes**

---

### Step 8: Test Your API

Once deployed, test your endpoints:

**Health Check:**
```bash
curl https://your-app.up.railway.app/health
```

**Get Recommendations:**
```bash
curl -X POST "https://your-app.up.railway.app/recommend" \
  -H "Content-Type: application/json" \
  -d '{"query": "Hire Java developers", "top_k": 3}'
```

**Interactive Docs:**
Visit: `https://your-app.up.railway.app/docs`

---

## Your Railway URLs

After deployment, you'll have:

- **API Base URL**: `https://your-app.up.railway.app`
- **Health Check**: `https://your-app.up.railway.app/health`
- **API Docs**: `https://your-app.up.railway.app/docs`
- **Recommend Endpoint**: `https://your-app.up.railway.app/recommend`

---

## Railway Configuration Files

Railway works with your existing files:

✅ **`Procfile`** - Tells Railway how to start your app
✅ **`runtime.txt`** - Specifies Python 3.11.9
✅ **`requirements-api.txt`** - Lists dependencies

No additional Railway-specific files needed!

---

## Troubleshooting

### Build Fails with "pandas compilation error"
**Solution**: 
- Make sure `PYTHON_VERSION` = `3.11.9` in variables
- Use `requirements-api.txt` (not `requirements.txt`)

### "Vector store not found" error
**Solution**: 
- Ensure `vector_store/shl_faiss/` is committed to GitHub
- Check: https://github.com/pardha134/shl-assessment-recommender/tree/main/vector_store

### "OpenAI API key not found"
**Solution**: 
- Add `OPENAI_API_KEY` in Railway Variables tab
- Redeploy after adding

### "Application failed to respond"
**Solution**: 
- Check logs in Railway dashboard
- Ensure `PORT` variable is set
- Verify start command uses `$PORT`

### Build takes too long
**Solution**: 
- Railway free tier has build time limits
- Use `requirements-api.txt` (lighter dependencies)
- Consider upgrading to paid tier if needed

---

## Railway vs Render vs Ngrok

| Feature | Railway | Render | Ngrok |
|---------|---------|--------|-------|
| **Setup Time** | 5 min | 10 min | 2 min |
| **URL Type** | Permanent | Permanent | Temporary |
| **Free Tier** | $5/month credit | Limited hours | Limited |
| **Build Speed** | Fast | Slower | N/A |
| **Auto-deploy** | Yes | Yes | No |
| **Best For** | Production | Production | Testing |

**Recommendation**: Railway is the best option for your use case!

---

## Monitoring Your App

In Railway dashboard:

1. **Deployments** - See build history and logs
2. **Metrics** - View CPU, memory, network usage
3. **Logs** - Real-time application logs
4. **Variables** - Manage environment variables
5. **Settings** - Configure build and deploy settings

---

## Updating Your App

When you make changes:

```bash
# 1. Make your changes locally
# 2. Commit and push
git add .
git commit -m "Update API"
git push origin main

# 3. Railway auto-deploys!
# Watch progress in Railway dashboard
```

Railway automatically redeploys when you push to GitHub!

---

## Cost & Limits

**Free Tier:**
- $5 credit per month
- ~500 hours of usage
- Enough for development and demos
- No credit card required initially

**Paid Tier:**
- $5/month minimum
- Pay for what you use
- Better performance
- No sleep/wake delays

---

## Quick Reference

### Railway Dashboard
https://railway.app/dashboard

### Your GitHub Repo
https://github.com/pardha134/shl-assessment-recommender

### Railway Docs
https://docs.railway.app

### Support
https://help.railway.app

---

## Success Checklist

- [ ] Code pushed to GitHub
- [ ] Railway account created
- [ ] Project deployed from GitHub
- [ ] Environment variables added
- [ ] Public domain generated
- [ ] Health endpoint returns 200
- [ ] Recommend endpoint works
- [ ] API docs accessible

---

## Next Steps

1. ✅ Deploy to Railway (follow steps above)
2. ✅ Get your public URL
3. ✅ Test all endpoints
4. ✅ Share URL with team/evaluators
5. ✅ Monitor logs for any issues

---

## Need Help?

- Railway Discord: https://discord.gg/railway
- Railway Docs: https://docs.railway.app
- This project's guide: `DEPLOYMENT_STATUS.md`

---

## Estimated Timeline

- **Setup Railway account**: 2 minutes
- **Connect GitHub repo**: 1 minute
- **Configure variables**: 2 minutes
- **Build & deploy**: 3-5 minutes
- **Total**: ~10 minutes

**You'll have a working public URL in about 10 minutes!**

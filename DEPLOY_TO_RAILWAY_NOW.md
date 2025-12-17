# 🚂 Deploy to Railway NOW - 5 Minute Guide

## Why Railway?
- ⚡ **Fastest** deployment (5 min vs 10+ min on Render)
- 🎯 **Easiest** setup - auto-detects everything
- 💰 **$5 free** credit per month
- 🚀 **No sleep** delays (unlike Render free tier)
- ✅ **Auto-deploy** on git push

---

## Before You Start

✅ Your GitHub repo: `https://github.com/pardha134/shl-assessment-recommender`
✅ Your OpenAI API key: (in your `.env` file)

---

## 5-Minute Deployment

### ⏱️ Step 1: Push to GitHub (30 sec)

```bash
git add .
git commit -m "Deploy to Railway"
git push origin main
```

---

### ⏱️ Step 2: Create Railway Account (1 min)

1. Go to: **https://railway.app**
2. Click **"Start a New Project"**
3. Click **"Login with GitHub"**
4. Authorize Railway

---

### ⏱️ Step 3: Deploy Your Repo (1 min)

1. Click **"Deploy from GitHub repo"**
2. Find and select: **`pardha134/shl-assessment-recommender`**
3. Click **"Deploy Now"**

Railway will automatically start building!

---

### ⏱️ Step 4: Add Environment Variables (2 min)

1. Click on your deployed service (the card that appears)
2. Click **"Variables"** tab
3. Click **"+ New Variable"** and add these **3 variables**:

**Variable 1:**
```
OPENAI_API_KEY
```
Value:
```
[Paste your OpenAI API key from .env file here]
```

**Variable 2:**
```
PYTHON_VERSION
```
Value:
```
3.11.9
```

**Variable 3:**
```
PORT
```
Value:
```
8000
```

4. Click **"Add"** after each one

---

### ⏱️ Step 5: Generate Public URL (30 sec)

1. Go to **"Settings"** tab
2. Scroll to **"Networking"** section
3. Click **"Generate Domain"**
4. **Copy your URL!** It will look like:
   ```
   https://shl-assessment-recommender-production.up.railway.app
   ```

---

## ✅ You're Live!

Your API is now publicly accessible at your Railway URL!

---

## 🧪 Test Your API

### Test 1: Health Check
```bash
curl https://your-app.up.railway.app/health
```

Expected response:
```json
{"status": "healthy"}
```

### Test 2: Get Recommendations
```bash
curl -X POST "https://your-app.up.railway.app/recommend" \
  -H "Content-Type: application/json" \
  -d '{"query": "Hire Java developers", "top_k": 3}'
```

### Test 3: Interactive Docs
Visit in browser:
```
https://your-app.up.railway.app/docs
```

---

## 📊 Monitor Your Deployment

In Railway dashboard:

1. **Deployments** - See build progress and logs
2. **Metrics** - CPU, memory, network usage
3. **Logs** - Real-time application logs
4. **Variables** - Manage environment variables

---

## 🔄 Auto-Deploy Updates

When you make changes:

```bash
git add .
git commit -m "Update API"
git push origin main
```

Railway automatically redeploys! No manual steps needed.

---

## 🆘 Troubleshooting

### Build fails?
- Check logs in Railway dashboard
- Ensure `PYTHON_VERSION` = `3.11.9`
- Verify all 3 environment variables are set

### "Vector store not found"?
- Make sure `vector_store/shl_faiss/` is in GitHub
- Check: https://github.com/pardha134/shl-assessment-recommender/tree/main/vector_store

### API not responding?
- Check logs for errors
- Verify `PORT` variable is set to `8000`
- Wait 1-2 minutes after deployment completes

---

## 💰 Cost

**Free Tier:**
- $5 credit per month
- Enough for ~500 hours
- Perfect for demos and testing
- No credit card required initially

**Your Usage:**
- Small API like this: ~$0.01/hour
- For demos: Will stay within $5 free credit
- For 24/7: ~$7/month (only $2 after free credit)

---

## ✅ Success Checklist

- [ ] Code pushed to GitHub
- [ ] Railway account created
- [ ] Project deployed from GitHub
- [ ] 3 environment variables added (OPENAI_API_KEY, PYTHON_VERSION, PORT)
- [ ] Public domain generated
- [ ] Health endpoint tested (returns 200)
- [ ] Recommend endpoint tested (returns recommendations)
- [ ] API docs accessible

---

## 🎉 What You Get

✅ **Permanent public URL**
✅ **Auto-deploy on git push**
✅ **Real-time logs and monitoring**
✅ **No sleep delays**
✅ **Fast performance**
✅ **Professional deployment**

---

## 📚 Additional Resources

- **Full Railway Guide**: `RAILWAY_DEPLOYMENT.md`
- **Comparison with other platforms**: `DEPLOYMENT_COMPARISON.md`
- **Your GitHub repo**: https://github.com/pardha134/shl-assessment-recommender
- **Railway Dashboard**: https://railway.app/dashboard
- **Railway Docs**: https://docs.railway.app

---

## 🚀 Ready? Let's Deploy!

1. Open terminal
2. Run: `git push origin main`
3. Go to: https://railway.app
4. Follow the 5 steps above
5. Get your public URL in 5 minutes!

**Your API will be live and ready to share!**

---

## 📝 Save Your URL

Once deployed, save your Railway URL here:

```
My Railway URL: https://________________________________.up.railway.app
```

Share this URL with:
- Team members
- Evaluators
- In your resume/portfolio
- In project submissions

---

## Need Help?

- Railway Discord: https://discord.gg/railway
- Railway Docs: https://docs.railway.app
- This project's guides: See `RAILWAY_DEPLOYMENT.md`

**You've got this! Railway makes deployment super easy! 🚂**

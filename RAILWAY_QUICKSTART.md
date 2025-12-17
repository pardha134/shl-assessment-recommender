# Railway Deployment - Quick Start (5 Minutes)

## 🚀 Deploy in 5 Steps

### Step 1: Push to GitHub (30 seconds)
```bash
git add .
git commit -m "Deploy to Railway"
git push origin main
```

### Step 2: Go to Railway (30 seconds)
Visit: **https://railway.app**
- Click **"Start a New Project"**
- Sign in with **GitHub**

### Step 3: Deploy from GitHub (1 minute)
- Click **"Deploy from GitHub repo"**
- Select: **`pardha134/shl-assessment-recommender`**
- Click **"Deploy Now"**

### Step 4: Add Environment Variables (2 minutes)
Click on your service → **"Variables"** tab → Add:

```
OPENAI_API_KEY = [Paste your key from .env file]

PYTHON_VERSION = 3.11.9

PORT = 8000
```

### Step 5: Generate Domain (30 seconds)
- Go to **"Settings"** → **"Networking"**
- Click **"Generate Domain"**
- Copy your URL!

---

## ✅ Done!

Your API is now live at:
```
https://your-app.up.railway.app
```

Test it:
```bash
curl https://your-app.up.railway.app/health
```

Visit docs:
```
https://your-app.up.railway.app/docs
```

---

## 📋 Checklist

- [ ] Code pushed to GitHub
- [ ] Railway account created (sign in with GitHub)
- [ ] Project deployed
- [ ] 3 environment variables added
- [ ] Domain generated
- [ ] API tested and working

---

## 🆘 Issues?

See full guide: **`RAILWAY_DEPLOYMENT.md`**

---

## 🎯 What You Get

- ✅ Permanent public URL
- ✅ Auto-deploy on git push
- ✅ Free $5/month credit
- ✅ Fast deployment (~5 min)
- ✅ Real-time logs
- ✅ Easy to manage

**Railway is the easiest way to deploy your API!**

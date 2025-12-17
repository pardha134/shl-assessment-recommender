# 🚀 Deploy to Streamlit Community Cloud (Free & Permanent)

## Why Streamlit Cloud?

- ✅ **100% Free** - No credit card required
- ✅ **Permanent URL** - Doesn't change
- ✅ **Perfect for ML/AI** - Designed for data apps
- ✅ **Easy deployment** - Connect GitHub and deploy
- ✅ **No configuration issues** - Just works!

---

## Step-by-Step Deployment (5 Minutes)

### Step 1: Push to GitHub

Make sure all changes are committed:

```bash
git add .
git commit -m "Add Streamlit app"
git push origin main
```

### Step 2: Sign Up for Streamlit Cloud

1. Go to: **https://streamlit.io/cloud**
2. Click **"Sign up"**
3. Sign in with **GitHub**
4. Authorize Streamlit

### Step 3: Deploy Your App

1. Click **"New app"** button
2. Fill in the form:
   - **Repository**: `pardha134/shl-assessment-recommender`
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py`
3. Click **"Advanced settings"**
4. **Python version**: 3.11
5. **Requirements file**: `requirements-streamlit.txt` (IMPORTANT!)
6. Add **Secrets** (important!):
   ```toml
   OPENAI_API_KEY = "your-openai-api-key-here"
   ```
   (Copy your key from `.env` file)

7. Click **"Deploy!"**

### Step 4: Wait for Deployment

- First deployment takes 3-5 minutes
- Watch the logs in real-time
- Look for "Your app is live!"

### Step 5: Get Your Permanent URL

Your app will be live at:
```
https://your-app-name.streamlit.app
```

**This URL is permanent and free!**

---

## Test Your App

Once deployed:

1. **Visit your URL**
2. **Enter a query** like: "Hire Java developers with teamwork skills"
3. **Click "Get Recommendations"**
4. **See AI-powered results!**

---

## Features of Your Streamlit App

✅ **Clean UI** - Professional interface
✅ **Real-time recommendations** - Powered by your RAG system
✅ **Interactive** - Adjust number of recommendations
✅ **Detailed results** - Shows relevance scores, descriptions, reasoning
✅ **Mobile-friendly** - Works on all devices

---

## Updating Your App

Streamlit auto-deploys when you push to GitHub:

```bash
# Make changes
git add .
git commit -m "Update app"
git push origin main

# Streamlit automatically redeploys!
```

---

## Managing Secrets

To update your OpenAI API key:

1. Go to Streamlit Cloud dashboard
2. Click your app
3. Click **"Settings"** → **"Secrets"**
4. Update the key
5. Click **"Save"**
6. App automatically restarts

---

## Troubleshooting

### "Module not found" errors

Make sure `requirements.txt` includes all dependencies:
- langchain
- langchain-openai
- openai
- faiss-cpu
- streamlit

### "OpenAI API key not found"

1. Check Secrets in Streamlit dashboard
2. Make sure key is named `OPENAI_API_KEY`
3. Restart the app

### "Vector store not found"

Make sure `vector_store/shl_faiss/` is committed to GitHub:
```bash
git add vector_store/
git commit -m "Add vector store"
git push
```

---

## Cost

**Completely FREE!**

Streamlit Community Cloud includes:
- ✅ Unlimited public apps
- ✅ 1 GB RAM per app
- ✅ Permanent URLs
- ✅ Auto-deploy from GitHub
- ✅ SSL certificates
- ✅ No credit card required

---

## Comparison

| Feature | Streamlit Cloud | Railway | Ngrok |
|---------|----------------|---------|-------|
| **Cost** | Free | $5 credit | Free (temp) |
| **URL** | Permanent | Permanent | Temporary |
| **Setup** | 5 min | Complex | 2 min |
| **ML/AI** | ✅ Perfect | ❌ Issues | ✅ Works |
| **UI** | ✅ Beautiful | API only | API only |

**For your RAG system: Streamlit Cloud is the best choice!**

---

## Your Permanent URLs

After deployment:

**Streamlit App**: `https://your-app.streamlit.app`

Share this URL for:
- ✅ Demos
- ✅ Portfolio
- ✅ Submissions
- ✅ User testing

---

## Next Steps

1. ✅ Commit and push: `git push origin main`
2. ✅ Sign up: https://streamlit.io/cloud
3. ✅ Deploy your app
4. ✅ Add OpenAI API key in Secrets
5. ✅ Share your permanent URL!

**You'll have a beautiful, permanent web app in 5 minutes!** 🎉

---

## Example Queries to Test

Once deployed, try these:

- "Hire software engineers with Python skills"
- "Find assessments for sales managers"
- "Evaluate leadership potential for executives"
- "Test problem-solving skills for graduates"

---

## Support

- Streamlit Docs: https://docs.streamlit.io
- Community Forum: https://discuss.streamlit.io
- This guide: `STREAMLIT_DEPLOYMENT.md`

**Streamlit Cloud is the easiest, most reliable way to deploy your RAG system!**

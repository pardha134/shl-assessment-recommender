# 🔑 How to Add OpenAI API Key to Streamlit Cloud

## Your OpenAI API Key

**Get your key from the `.env` file in your project folder.**

It looks like this:
```
sk-proj-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

**⚠️ Keep this key private! Never share it publicly.**

---

## Method 1: Add During Deployment (Recommended)

### When Creating Your App

1. **Go to Streamlit Cloud**
   - Visit: https://streamlit.io/cloud
   - Sign in with GitHub

2. **Click "New app"**

3. **Fill in Basic Info**
   - Repository: `pardha134/shl-assessment-recommender`
   - Branch: `main`
   - Main file path: `streamlit_app.py`

4. **Click "Advanced settings"** (at the bottom)

5. **In the "Secrets" Section**
   
   You'll see a text box. Use this format (replace with YOUR key from .env file):
   
   ```toml
   OPENAI_API_KEY = "your-actual-api-key-from-env-file"
   ```

6. **Important Notes:**
   - Use TOML format (shown above)
   - Include the quotes around the key
   - Make sure there are no extra spaces
   - The key name must be exactly `OPENAI_API_KEY`

7. **Click "Deploy!"**

---

## Method 2: Add After Deployment

### If You Already Deployed Without Adding the Key

1. **Go to Streamlit Cloud Dashboard**
   - Visit: https://share.streamlit.io/
   - Sign in with GitHub

2. **Find Your App**
   - Look for `shl-assessment-recommender` in your apps list
   - Click on it

3. **Click the Menu (⋮) Button**
   - Located in the top-right corner of your app

4. **Select "Settings"**

5. **Click "Secrets" Tab**
   - You'll see a text editor

6. **Add Your Secret**
   
   Use this format (replace with YOUR key from .env file):
   
   ```toml
   OPENAI_API_KEY = "your-actual-api-key-from-env-file"
   ```

7. **Click "Save"**

8. **App Will Restart Automatically**
   - Takes about 30 seconds
   - Your app will now have access to the API key

---

## Visual Guide

### What the Secrets Section Looks Like

```
┌─────────────────────────────────────────────┐
│ Secrets                                     │
├─────────────────────────────────────────────┤
│                                             │
│  # Paste your secrets here in TOML format  │
│                                             │
│  OPENAI_API_KEY = "sk-proj-Kb7c..."        │
│                                             │
│                                             │
└─────────────────────────────────────────────┘
         [Cancel]              [Save]
```

---

## Format Requirements

### ✅ Correct Format (TOML)

```toml
OPENAI_API_KEY = "sk-proj-YOUR_ACTUAL_KEY_HERE"
```

### ❌ Wrong Formats

```toml
# Missing quotes
OPENAI_API_KEY = sk-proj-Kb7c...

# Wrong variable name
OPENAI_KEY = "sk-proj-Kb7c..."

# Extra spaces
OPENAI_API_KEY  =  "sk-proj-Kb7c..."

# Using single quotes (use double quotes)
OPENAI_API_KEY = 'sk-proj-Kb7c...'
```

---

## How to Access Secrets in Your Code

Your `streamlit_app.py` already has this configured:

```python
import streamlit as st
import os

# Streamlit automatically loads secrets
# Access them like environment variables
api_key = st.secrets["OPENAI_API_KEY"]

# Or through os.environ (Streamlit sets this automatically)
api_key = os.environ.get("OPENAI_API_KEY")
```

Your app uses `Config.OPENAI_API_KEY` which reads from environment variables, so it will work automatically!

---

## Troubleshooting

### Error: "OPENAI_API_KEY not found"

**Solution:**
1. Check that you added the secret in Streamlit Cloud
2. Verify the variable name is exactly `OPENAI_API_KEY`
3. Make sure you clicked "Save"
4. Wait for the app to restart (30 seconds)

### Error: "Invalid API key"

**Solution:**
1. Check that you copied the entire key (it's very long!)
2. Make sure there are no extra spaces or line breaks
3. Verify the key starts with `sk-proj-`
4. Try copying the key again from your `.env` file

### Error: "Secrets not loading"

**Solution:**
1. Make sure you're using TOML format (with quotes)
2. Check for syntax errors (missing quotes, wrong format)
3. Try deleting and re-adding the secret
4. Restart the app manually from the dashboard

---

## Security Best Practices

### ✅ Do This:
- Store API keys in Streamlit Secrets
- Use environment variables
- Keep your `.env` file private
- Never commit API keys to GitHub

### ❌ Don't Do This:
- Hardcode API keys in your code
- Share your API key publicly
- Commit `.env` file to GitHub
- Post API keys in screenshots or documentation

---

## Testing Your Secret

After adding the secret and deploying:

1. **Visit Your App**
   ```
   https://your-app-name.streamlit.app
   ```

2. **Try a Query**
   - Enter: "Hire Java developers with teamwork skills"
   - Click "Get Recommendations"

3. **Check for Errors**
   - ✅ If you see recommendations → Secret is working!
   - ❌ If you see "API key not found" → Check the steps above

---

## Quick Copy-Paste Template

**For Streamlit Cloud Secrets (replace with YOUR key from .env):**

```toml
OPENAI_API_KEY = "your-actual-api-key-from-env-file"
```

**Steps:**
1. Open your `.env` file
2. Copy the key after `OPENAI_API_KEY=`
3. Paste it in the format above (with quotes)
4. Add to Streamlit Secrets

---

## Video Tutorial

If you prefer a video guide, Streamlit has an official tutorial:
- https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management

---

## Summary

1. **Copy your API key** from above
2. **Go to Streamlit Cloud** → Advanced settings → Secrets
3. **Paste the TOML format** (with quotes)
4. **Click Save**
5. **Wait for restart** (30 seconds)
6. **Test your app** with a query

**That's it! Your app will now have access to OpenAI API! 🎉**

---

## Need Help?

If you're still having issues:
1. Check the Streamlit Cloud logs (in the dashboard)
2. Verify the secret format matches exactly
3. Try redeploying the app
4. Check the troubleshooting section above

**Your API key is ready to use! Just follow the steps above! 🚀**

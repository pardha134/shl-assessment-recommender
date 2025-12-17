# 🚀 Quick Guide: Add API Key to Streamlit (30 Seconds)

## Your API Key

**Find your API key in the `.env` file in your project folder.**

It starts with `sk-proj-` and is very long (about 164 characters).

---

## Step-by-Step (With Screenshots)

### Step 1: Go to Streamlit Cloud
🔗 https://streamlit.io/cloud

Click **"Sign in"** → Use GitHub

---

### Step 2: Create New App
Click **"New app"** button

---

### Step 3: Fill in Details

```
Repository: pardha134/shl-assessment-recommender
Branch: main
Main file path: streamlit_app.py
```

---

### Step 4: Click "Advanced settings"

Look for this button at the bottom of the form

---

### Step 5: Add Your Secret

In the **Secrets** text box, use this format:

```toml
OPENAI_API_KEY = "your-actual-api-key-from-env-file"
```

**How to get your key:**
1. Open the `.env` file in your project
2. Copy the value after `OPENAI_API_KEY=`
3. Paste it in the format above (with quotes)

**Important:**
- ✅ Include the quotes `"`
- ✅ Use the exact format shown
- ✅ No extra spaces
- ✅ Replace with YOUR actual key

---

### Step 6: Deploy!

Click **"Deploy!"** button

Wait 3-7 minutes for deployment

---

## Visual Reference

```
┌────────────────────────────────────────────────┐
│  Deploy an app                                 │
├────────────────────────────────────────────────┤
│                                                │
│  Repository: pardha134/shl-assessment-...     │
│  Branch: main                                  │
│  Main file path: streamlit_app.py             │
│                                                │
│  [Advanced settings ▼]  ← CLICK THIS          │
│                                                │
│  ┌──────────────────────────────────────┐    │
│  │ Secrets                              │    │
│  ├──────────────────────────────────────┤    │
│  │ OPENAI_API_KEY = "your-key-here"    │    │
│  │                                      │    │
│  └──────────────────────────────────────┘    │
│                                                │
│              [Deploy!]  ← THEN CLICK THIS     │
└────────────────────────────────────────────────┘
```

---

## Already Deployed? Add Secret Later

### Option A: Through Dashboard

1. Go to https://share.streamlit.io/
2. Click your app
3. Click **⋮** (menu) → **Settings**
4. Click **Secrets** tab
5. Paste the secret (same format as above)
6. Click **Save**

### Option B: Redeploy

1. Delete the app
2. Create new app
3. Add secret during creation (Step 5 above)

---

## Format Template

**Use this format (replace with YOUR key from .env file):**

```toml
OPENAI_API_KEY = "your-actual-api-key-from-env-file"
```

**To get your key:**
1. Open `.env` file in your project
2. Find the line: `OPENAI_API_KEY=sk-proj-...`
3. Copy everything after the `=`
4. Paste it in the format above (with quotes)

---

## Test Your App

After deployment, visit your app URL:
```
https://your-app-name.streamlit.app
```

Try this query:
```
Hire Java developers with strong teamwork skills
```

Click **"Get Recommendations"**

✅ If you see results → Success!
❌ If you see error → Check secret format

---

## Common Mistakes

### ❌ Wrong
```toml
# Missing quotes
OPENAI_API_KEY = sk-proj-Kb7c...

# Wrong name
OPENAI_KEY = "sk-proj-Kb7c..."

# Single quotes
OPENAI_API_KEY = 'sk-proj-Kb7c...'
```

### ✅ Correct
```toml
OPENAI_API_KEY = "sk-proj-YOUR_ACTUAL_KEY_FROM_ENV_FILE"
```

---

## Troubleshooting

### "API key not found"
- Check you clicked "Save" in Secrets
- Wait 30 seconds for app to restart
- Verify the variable name is `OPENAI_API_KEY`

### "Invalid API key"
- Copy the entire key (it's very long!)
- Check for extra spaces or line breaks
- Make sure it starts with `sk-proj-`

### "Secrets not loading"
- Use TOML format (with double quotes)
- Check for typos in variable name
- Try deleting and re-adding the secret

---

## That's It!

**3 Simple Steps:**
1. Copy the secret format above
2. Paste in Streamlit Cloud → Advanced settings → Secrets
3. Click Deploy!

**Your app will be live in 5 minutes! 🎉**

---

## Need More Help?

See detailed guide: `HOW_TO_ADD_SECRETS_STREAMLIT.md`

Or visit: https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management

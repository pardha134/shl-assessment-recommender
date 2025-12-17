# 🔑 How to Add Your OpenAI API Key (Super Simple)

## Step 1: Find Your API Key

1. Open the `.env` file in your project folder
2. Look for this line:
   ```
   OPENAI_API_KEY=sk-proj-...
   ```
3. Copy everything after the `=` sign (the part that starts with `sk-proj-`)

---

## Step 2: Go to Streamlit Cloud

1. Visit: **https://streamlit.io/cloud**
2. Click **"Sign in"**
3. Choose **"Continue with GitHub"**

---

## Step 3: Create Your App

1. Click the **"New app"** button (big blue button)

2. Fill in these fields:
   ```
   Repository: pardha134/shl-assessment-recommender
   Branch: main
   Main file path: streamlit_app.py
   ```

3. Click **"Advanced settings"** at the bottom

---

## Step 4: Add Your Secret

1. You'll see a section called **"Secrets"**

2. In the text box, type this (replace `YOUR_KEY` with the key you copied from Step 1):

   ```toml
   OPENAI_API_KEY = "YOUR_KEY"
   ```

   **Example:**
   ```toml
   OPENAI_API_KEY = "sk-proj-abc123xyz..."
   ```

3. Make sure to:
   - ✅ Include the quotes `"`
   - ✅ Use the exact name `OPENAI_API_KEY`
   - ✅ No extra spaces

---

## Step 5: Deploy!

1. Click the **"Deploy!"** button

2. Wait 3-7 minutes (grab a coffee ☕)

3. Your app will be live!

---

## Your App URL

After deployment, you'll get a permanent URL like:
```
https://your-app-name.streamlit.app
```

---

## Test It!

1. Visit your app URL
2. Type: "Hire Java developers with teamwork skills"
3. Click "Get Recommendations"
4. See the magic! ✨

---

## Troubleshooting

### "API key not found" error?
- Check that you added the secret in Step 4
- Make sure the name is exactly `OPENAI_API_KEY`
- Verify you included the quotes

### "Invalid API key" error?
- Make sure you copied the entire key from `.env`
- Check for extra spaces or line breaks
- The key should start with `sk-proj-`

### Still not working?
- Try deleting the app and creating it again
- Make sure you clicked "Save" after adding the secret
- Wait 30 seconds for the app to restart

---

## That's It!

**You now have a live AI-powered assessment recommender! 🎉**

Share your URL with:
- Recruiters
- Hiring managers
- Your portfolio
- Job applications

---

## Need More Help?

See detailed guides:
- `STREAMLIT_SECRETS_QUICK_GUIDE.md` - Quick reference
- `HOW_TO_ADD_SECRETS_STREAMLIT.md` - Detailed guide
- `STREAMLIT_DEPLOYMENT.md` - Full deployment guide

**You've got this! 💪**

# 🔗 How to Get Your GitHub URL

## Quick Answer

Your GitHub URL will be in this format:
```
https://github.com/YOUR_USERNAME/shl-assessment-recommender
```

Replace `YOUR_USERNAME` with your actual GitHub username.

---

## Step-by-Step Guide

### Method 1: GitHub Desktop (Easiest - 5 minutes)

1. **Download GitHub Desktop**
   - Go to: https://desktop.github.com/
   - Install and sign in

2. **Create Repository**
   - File → New Repository
   - Name: `shl-assessment-recommender`
   - Local Path: Your current project folder
   - Click "Create Repository"

3. **Publish to GitHub**
   - Click "Publish repository"
   - Click "Publish repository" again

4. **Get Your URL**
   - Click "View on GitHub"
   - Copy the URL from your browser
   - Format: `https://github.com/YOUR_USERNAME/shl-assessment-recommender`

---

### Method 2: Command Line (10 minutes)

1. **Open Command Prompt in your project folder**

2. **Run these commands:**

```bash
# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: SHL Assessment Recommender"
```

3. **Create repository on GitHub:**
   - Go to: https://github.com/new
   - Name: `shl-assessment-recommender`
   - Click "Create repository"

4. **Push your code:**
```bash
git remote add origin https://github.com/YOUR_USERNAME/shl-assessment-recommender.git
git branch -M main
git push -u origin main
```

5. **Your URL is:**
```
https://github.com/YOUR_USERNAME/shl-assessment-recommender
```

---

## What You Need

- GitHub account (free): https://github.com/signup
- Your project folder (current location)
- 5-10 minutes

---

## After Getting Your URL

Submit this information:

**GitHub URL:**
```
https://github.com/YOUR_USERNAME/shl-assessment-recommender
```

**API Endpoint:**
```
POST http://localhost:8000/recommend
```

**Submission File:**
```
predictions/Pardha_Saradhi_Thumma.csv
```

---

## Need Help?

See detailed guides:
- `GITHUB_SETUP.md` - Complete setup guide
- `SUBMISSION_CHECKLIST.md` - Submission checklist
- `init_git.bat` - Automated git initialization

---

**That's it! Your code will be on GitHub and you'll have your URL!** 🎉

# 🔧 Railway Manual Fix - Do This NOW

## The Problem

Railway is using the old Procfile command that has `$PORT` variable issues.

## ✅ MANUAL FIX (Do This in Railway Dashboard)

### Step 1: Go to Railway Dashboard
Visit: https://railway.app/dashboard

### Step 2: Click on Your Service
Find your `shl-assessment-recommender` service and click it

### Step 3: Go to Settings
Click on the **"Settings"** tab

### Step 4: Find "Deploy" Section
Scroll down to find the **"Deploy"** section

### Step 5: Override Start Command
Look for **"Custom Start Command"** or **"Start Command"**

**Enter this EXACT command:**
```
python start.py
```

### Step 6: Save and Redeploy
1. Click **"Save"** or **"Update"**
2. Railway will automatically redeploy
3. Wait 2-3 minutes

---

## Alternative: Set Environment Variable

If the above doesn't work, try this:

### In Railway Dashboard:

1. Go to your service
2. Click **"Variables"** tab
3. Click **"+ New Variable"**
4. Add:
   - **Key**: `PORT`
   - **Value**: `8000`
5. Click **"Add"**
6. Redeploy

---

## Why This Works

The `start.py` script we created properly handles the PORT variable:

```python
import os
import uvicorn

port = int(os.getenv("PORT", "8000"))
uvicorn.run("api.main:app", host="0.0.0.0", port=port)
```

This Python script:
- ✅ Reads PORT from environment
- ✅ Defaults to 8000 if not set
- ✅ No shell expansion issues
- ✅ Works 100% of the time

---

## Verify It's Working

After redeployment, check logs in Railway:

**Good logs (success):**
```
INFO: Started server process
INFO: Waiting for application startup
INFO: Application startup complete
INFO: Uvicorn running on http://0.0.0.0:XXXX
```

**Bad logs (still failing):**
```
Error: Invalid value for '--port': '$PORT'
```

If you still see bad logs, Railway is not using the new start command.

---

## Nuclear Option: Delete and Recreate

If nothing works:

### Step 1: Delete Current Service
1. Go to Railway dashboard
2. Click your service
3. Settings → Danger → Delete Service

### Step 2: Create New Service
1. Click "New Project"
2. "Deploy from GitHub repo"
3. Select: `pardha134/shl-assessment-recommender`
4. **IMPORTANT**: In configuration, set:
   - **Start Command**: `python start.py`
   - **Build Command**: `pip install -r requirements.txt`

### Step 3: Add Environment Variables
- `OPENAI_API_KEY` = (your key)
- `PORT` = `8000` (optional, but helps)

### Step 4: Deploy
Click "Deploy" and wait 3-5 minutes

---

## Check Railway Configuration Files

Railway might be using old config. Check these in Railway dashboard:

### Procfile
Should say:
```
web: python start.py
```

If it says something else, that's the problem!

### railway.toml
Should NOT exist, or should be minimal

### Dockerfile
Should have:
```dockerfile
CMD ["python", "start.py"]
```

---

## Manual Deployment Test

To test if your code works locally:

```bash
# Set PORT manually
set PORT=8000

# Run start.py
python start.py

# Should see:
# INFO: Uvicorn running on http://0.0.0.0:8000
```

If this works locally, the code is fine. Railway configuration is the issue.

---

## Contact Railway Support

If all else fails:

1. Go to Railway dashboard
2. Click the "?" icon (Help)
3. Describe the issue:
   ```
   My app fails with "Invalid value for '--port': '$PORT'"
   
   I need Railway to use this start command:
   python start.py
   
   Repository: pardha134/shl-assessment-recommender
   ```

Railway support is usually responsive!

---

## Permanent Fix (Already Done)

The code is already fixed in your repository:
- ✅ `start.py` created
- ✅ `Dockerfile` updated
- ✅ `Procfile` updated

**The issue is Railway is using cached/old configuration.**

---

## Force Railway to Use New Config

Try these in order:

### Option 1: Clear Build Cache
1. Railway dashboard → Your service
2. Settings → Danger
3. Click "Clear Build Cache"
4. Redeploy

### Option 2: Trigger New Deployment
1. Make a small change to README
2. Commit and push
3. Railway auto-deploys

### Option 3: Manual Redeploy
1. Railway dashboard → Deployments
2. Click "..." on latest deployment
3. Click "Redeploy"

---

## Summary

**The Fix (in Railway Dashboard):**
1. Go to Settings
2. Set Start Command: `python start.py`
3. Save and redeploy

**OR**

1. Delete service
2. Create new service
3. Set start command during creation

**Your code is correct. Railway configuration needs updating.**

---

## Need Immediate Solution?

While fixing Railway, use Ngrok:

```bash
# Terminal 1
python api/main.py

# Terminal 2
ngrok http 8000
```

**You'll have a working URL in 2 minutes!**

See `USE_NGROK_NOW.md` for details.

---

## Timeline

- **Manual fix in Railway**: 5 minutes
- **Railway redeploy**: 3-5 minutes
- **Total**: ~10 minutes

**OR**

- **Ngrok setup**: 2 minutes
- **Total**: 2 minutes

**Your choice!** Both will work.

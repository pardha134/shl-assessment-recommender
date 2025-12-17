# Railway Deployment Troubleshooting

## Common Issue: Dependency Conflicts

If you see errors like:
```
ERROR: ResolutionImpossible
ERROR: Cannot install package X because it conflicts with Y
```

### Solution Applied ✅

We've created optimized deployment files:

1. **`nixpacks.toml`** - Tells Railway exactly how to build
2. **`requirements-api.txt`** - Minimal dependencies with flexible versions
3. **`railway.json`** - Railway configuration

These files ensure Railway uses the right dependencies.

---

## If Build Still Fails

### Option 1: Check Railway is Using Correct Files

In Railway dashboard:
1. Go to your service → **"Settings"**
2. Under **"Build"**, verify:
   - Build Command: `pip install --upgrade pip setuptools wheel && pip install -r requirements-api.txt`
   - Start Command: `uvicorn api.main:app --host 0.0.0.0 --port $PORT`

### Option 2: Set Python Version Explicitly

In Railway dashboard:
1. Go to **"Variables"** tab
2. Add variable:
   - Key: `NIXPACKS_PYTHON_VERSION`
   - Value: `3.11`

### Option 3: Force Rebuild

Sometimes Railway cache causes issues:
1. Go to **"Settings"** → **"Danger"**
2. Click **"Clear Build Cache"**
3. Redeploy

---

## Understanding the Files

### `nixpacks.toml` (Railway's preferred config)
```toml
[phases.setup]
nixPkgs = ["python311"]  # Use Python 3.11

[phases.install]
cmds = [
  "pip install --upgrade pip setuptools wheel",
  "pip install -r requirements-api.txt"  # Use lightweight deps
]

[start]
cmd = "uvicorn api.main:app --host 0.0.0.0 --port $PORT"
```

### `requirements-api.txt` (Deployment-only deps)
- ✅ Only includes packages needed for API
- ✅ Uses `>=` instead of `==` for flexibility
- ✅ Excludes heavy packages like pandas, streamlit
- ✅ Avoids version conflicts

### `requirements.txt` (Full development deps)
- Used for local development
- Includes all packages (scraping, data processing, etc.)
- NOT used by Railway

---

## Verification Steps

After deployment, test:

### 1. Check Logs
In Railway dashboard → **"Deployments"** → Click latest deployment → View logs

Look for:
```
✅ Successfully installed fastapi uvicorn...
✅ Application startup complete
```

### 2. Test Health Endpoint
```bash
curl https://your-app.up.railway.app/health
```

Expected:
```json
{"status": "healthy"}
```

### 3. Test API Docs
Visit: `https://your-app.up.railway.app/docs`

Should see interactive Swagger UI.

---

## Still Having Issues?

### Check These:

1. **Environment Variables Set?**
   - `OPENAI_API_KEY` ✅
   - `PYTHON_VERSION` = `3.11.9` ✅
   - `PORT` = `8000` ✅

2. **Files Committed to GitHub?**
   ```bash
   git status
   # Should show: nothing to commit, working tree clean
   ```

3. **Railway Connected to Correct Branch?**
   - Settings → Should be connected to `main` branch

4. **Vector Store Files Present?**
   - Check GitHub: `vector_store/shl_faiss/` should have files

---

## Alternative: Use Render Instead

If Railway continues to have issues, Render is more forgiving:

See `DEPLOYMENT_GUIDE.md` for Render instructions.

---

## Get Help

- Railway Discord: https://discord.gg/railway
- Railway Docs: https://docs.railway.app
- Check Railway status: https://status.railway.app

---

## Quick Fix Commands

If you need to update and redeploy:

```bash
# 1. Make sure latest files are committed
git add nixpacks.toml requirements-api.txt railway.json
git commit -m "Fix Railway deployment configuration"
git push origin main

# 2. Railway will auto-deploy
# Watch progress in Railway dashboard
```

---

## Success Indicators

✅ Build completes without errors
✅ Deployment shows "Success" status
✅ Health endpoint returns 200
✅ API docs are accessible
✅ Recommend endpoint works

Once you see these, your API is live! 🎉

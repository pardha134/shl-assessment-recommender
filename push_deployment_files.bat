@echo off
echo ========================================
echo Pushing Deployment Files to GitHub
echo ========================================
echo.

echo Step 1: Adding all files...
git add .
echo ✓ Files staged
echo.

echo Step 2: Committing changes...
git commit -m "Add deployment configuration and documentation"
echo ✓ Changes committed
echo.

echo Step 3: Pushing to GitHub...
git push origin main
echo ✓ Pushed to GitHub
echo.

echo ========================================
echo SUCCESS! Changes are now on GitHub
echo ========================================
echo.
echo Next steps:
echo 1. Visit your GitHub repo to verify files are there
echo 2. Deploy to Render (see DEPLOYMENT_STATUS.md)
echo.
pause

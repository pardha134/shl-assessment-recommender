@echo off
echo ========================================
echo Git Repository Initialization
echo ========================================
echo.

echo Step 1: Initializing Git repository...
git init
echo.

echo Step 2: Adding all files...
git add .
echo.

echo Step 3: Creating initial commit...
git commit -m "Initial commit: SHL Assessment Recommender with RAG"
echo.

echo ========================================
echo Git repository initialized successfully!
echo ========================================
echo.
echo Next steps:
echo 1. Create a new repository on GitHub: https://github.com/new
echo 2. Name it: shl-assessment-recommender
echo 3. Run these commands (replace YOUR_USERNAME):
echo.
echo    git remote add origin https://github.com/YOUR_USERNAME/shl-assessment-recommender.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo ========================================
pause

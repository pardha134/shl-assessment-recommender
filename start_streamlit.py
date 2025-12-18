"""Start the Streamlit web app."""
import subprocess
import sys

if __name__ == "__main__":
    print("=" * 60)
    print("🎯 Starting SHL Assessment Recommender Web App")
    print("=" * 60)
    print("\n📍 App will open at: http://localhost:8501")
    print("⏳ Starting Streamlit...\n")
    
    subprocess.run([sys.executable, "-m", "streamlit", "run", "streamlit_app.py"])

"""Start the FastAPI server."""
import uvicorn
from config import Config

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 Starting SHL Assessment Recommender API")
    print("=" * 60)
    print(f"\n📍 Server will run at: http://{Config.API_HOST}:{Config.API_PORT}")
    print(f"📚 API Documentation: http://{Config.API_HOST}:{Config.API_PORT}/docs")
    print(f"🔍 Interactive API: http://{Config.API_HOST}:{Config.API_PORT}/redoc")
    print("\n⏳ Starting server...\n")
    
    uvicorn.run(
        "api.main:app",
        host=Config.API_HOST,
        port=Config.API_PORT,
        reload=True,
        log_level=Config.LOG_LEVEL.lower()
    )

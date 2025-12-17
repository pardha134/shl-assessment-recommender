"""FastAPI application for SHL Assessment Recommender."""
import sys
import os
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from config import Config
from api.schemas import (
    RecommendRequest,
    RecommendResponse,
    HealthResponse,
    ErrorResponse,
    Recommendation
)
from rag.recommender import Recommender

logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(__name__)

# Global recommender instance
recommender = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifecycle manager for startup and shutdown."""
    # Startup
    global recommender
    logger.info("Starting up API server...")
    
    try:
        # Initialize recommender (loads vector store)
        recommender = Recommender()
        logger.info("Recommender initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize recommender: {e}")
        logger.warning("API will start but recommendations will fail")
    
    yield
    
    # Shutdown
    logger.info("Shutting down API server...")


# Create FastAPI app
app = FastAPI(
    title="SHL Assessment Recommender API",
    description="GenAI-powered API for recommending SHL assessments based on hiring requirements",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_requests(request, call_next):
    """Log all requests."""
    logger.info(f"{request.method} {request.url.path}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response


@app.get("/", tags=["Root"])
async def root():
    """Root endpoint."""
    return {
        "message": "SHL Assessment Recommender API",
        "version": "1.0.0",
        "status": "operational",
        "endpoints": {
            "health": "/health",
            "recommend": "/recommend",
            "docs": "/docs"
        }
    }


@app.get(
    "/health",
    tags=["Health"],
    summary="Health check endpoint",
    status_code=200
)
async def health_check():
    """
    Check API health status.
    
    Returns:
        dict: Status "healthy" if API is operational
    """
    return {"status": "healthy"}


@app.post(
    "/recommend",
    tags=["Recommendations"],
    summary="Get assessment recommendations",
    status_code=200,
    responses={
        200: {"description": "Successful recommendation"},
        400: {"description": "Invalid request"},
        500: {"description": "Internal server error"}
    }
)
async def get_recommendations(request: RecommendRequest):
    """
    Generate assessment recommendations based on hiring requirements.
    
    Accepts:
    - Natural language query (JD/query in string)
    - Job description text
    
    Returns 1-10 most relevant Individual Test Solutions with required fields:
    - url: Valid URL in string
    - adaptive_support: "Yes/No"
    - description: Description in string
    - duration: Integer (minutes)
    - remote_support: "Yes/No"
    - test_type: List of strings
    """
    global recommender
    
    # Check if recommender is initialized
    if recommender is None:
        logger.error("Recommender not initialized")
        raise HTTPException(
            status_code=500,
            detail="Recommendation service not available"
        )
    
    # Validate query
    if not request.query.strip():
        raise HTTPException(
            status_code=400,
            detail="Query cannot be empty"
        )
    
    try:
        # Generate recommendations
        result = recommender.recommend(
            query=request.query,
            top_k=min(request.top_k, 10)  # Max 10 as per spec
        )
        
        # Check for errors in result
        if 'error' in result:
            raise HTTPException(
                status_code=500,
                detail=result['error']
            )
        
        # Format recommendations according to exact API specification
        recommendations = []
        for rec in result['recommendations']:
            # Get the assessment URL
            url = rec.get('assessment_url', rec.get('url', ''))
            if not url or url == 'N/A':
                # Try to construct URL from name
                name = rec.get('assessment_name', rec.get('name', ''))
                if name:
                    # Create a slug from the name
                    slug = name.lower().replace(' ', '-').replace('/', '-')
                    url = f"https://www.shl.com/solutions/products/{slug}/"
            
            # Get test type as list
            test_type = rec.get('test_type', '')
            if isinstance(test_type, str):
                test_type_list = [test_type] if test_type and test_type != 'N/A' else []
            else:
                test_type_list = test_type if test_type else []
            
            # Get duration as integer
            duration_str = rec.get('duration', '0')
            if isinstance(duration_str, str):
                # Extract first number from duration string (e.g., "20-45 minutes" -> 20)
                import re
                duration_match = re.search(r'\d+', duration_str)
                duration = int(duration_match.group()) if duration_match else 0
            else:
                duration = int(duration_str) if duration_str else 0
            
            recommendations.append({
                "url": url,
                "name": rec.get('assessment_name', rec.get('name', '')),
                "adaptive_support": "No",  # Default value, can be enhanced
                "description": rec.get('description', ''),
                "duration": duration,
                "remote_support": "Yes",  # Default value, can be enhanced
                "test_type": test_type_list
            })
        
        return {
            "recommended_assessments": recommendations
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error generating recommendations: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate recommendations: {str(e)}"
        )


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler."""
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"error": "Internal server error", "detail": str(exc)}
    )


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "api.main:app",
        host=Config.API_HOST,
        port=Config.API_PORT,
        reload=True,
        log_level=Config.LOG_LEVEL.lower()
    )

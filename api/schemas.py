"""Pydantic schemas for API request/response validation."""
from typing import List, Optional
from pydantic import BaseModel, Field


class RecommendRequest(BaseModel):
    """Request schema for recommendation endpoint."""
    query: str = Field(..., description="Natural language query, job description text, or URL containing JD", min_length=1)
    top_k: int = Field(10, description="Number of recommendations to return", ge=1, le=10)
    
    class Config:
        json_schema_extra = {
            "example": {
                "query": "I am hiring for Java developers who can also collaborate effectively with my business teams.",
                "top_k": 10
            }
        }


class Recommendation(BaseModel):
    """Schema for a single recommendation."""
    assessment_name: str = Field(..., description="Name of the recommended assessment")
    assessment_url: str = Field(..., description="URL to the assessment on SHL catalog")
    relevance_score: Optional[float] = Field(None, description="Relevance score (0-10)", ge=0, le=10)
    test_type: Optional[str] = Field(None, description="Test type (K=Knowledge/Skills, P=Personality/Behavior, etc.)")
    reasoning: Optional[str] = Field(None, description="Explanation for the recommendation")
    category: Optional[str] = Field(None, description="Assessment category")
    description: Optional[str] = Field(None, description="Product description")
    
    class Config:
        json_schema_extra = {
            "example": {
                "assessment_name": "Verify G+ (General Ability)",
                "relevance_score": 8.5,
                "reasoning": "This assessment measures cognitive ability essential for software engineering roles",
                "product_id": "1",
                "category": "Cognitive Ability",
                "target_roles": ["Graduate", "Professional"],
                "skills_assessed": ["problem-solving", "analytical"],
                "duration": "36 minutes",
                "similarity_score": 0.85
            }
        }


class RecommendResponse(BaseModel):
    """Response schema for recommendation endpoint."""
    query: str = Field(..., description="Original query")
    recommendations: List[Recommendation] = Field(..., description="List of recommendations")
    retrieved_count: Optional[int] = Field(None, description="Number of documents retrieved")
    processing_time: float = Field(..., description="Processing time in seconds")
    message: Optional[str] = Field(None, description="Additional message or warning")
    
    class Config:
        json_schema_extra = {
            "example": {
                "query": "Hire fresh graduates for software engineering roles",
                "recommendations": [
                    {
                        "assessment_name": "Coding Skills Assessment - Python",
                        "relevance_score": 9.2,
                        "reasoning": "Directly evaluates Python programming skills",
                        "category": "Technical Skills"
                    }
                ],
                "retrieved_count": 5,
                "processing_time": 1.23
            }
        }


class HealthResponse(BaseModel):
    """Response schema for health check endpoint."""
    status: str = Field(..., description="Service status")
    vector_store_loaded: bool = Field(..., description="Whether vector store is loaded")
    total_products: int = Field(..., description="Number of products in vector store")
    model: str = Field(..., description="LLM model being used")
    
    class Config:
        json_schema_extra = {
            "example": {
                "status": "healthy",
                "vector_store_loaded": True,
                "total_products": 12,
                "model": "gpt-3.5-turbo"
            }
        }


class ErrorResponse(BaseModel):
    """Response schema for errors."""
    error: str = Field(..., description="Error message")
    detail: Optional[str] = Field(None, description="Detailed error information")
    
    class Config:
        json_schema_extra = {
            "example": {
                "error": "Vector store not found",
                "detail": "Please run build_embeddings.py first"
            }
        }

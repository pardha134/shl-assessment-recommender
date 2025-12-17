# API Documentation

## Base URL

```
http://localhost:8000
```

## Authentication

Currently, no authentication is required. For production deployment, implement appropriate authentication mechanisms.

## Endpoints

### 1. Root Endpoint

**GET** `/`

Returns basic API information.

**Response:**
```json
{
  "message": "SHL Assessment Recommender API",
  "version": "1.0.0",
  "docs": "/docs"
}
```

---

### 2. Health Check

**GET** `/health`

Check API health and system status.

**Response:**
```json
{
  "status": "healthy",
  "vector_store_loaded": true,
  "total_products": 12,
  "model": "gpt-3.5-turbo"
}
```

**Status Codes:**
- `200 OK`: Service is healthy
- `503 Service Unavailable`: Service is degraded

---

### 3. Get Recommendations

**POST** `/recommend`

Generate assessment recommendations based on hiring requirements.

**Request Body:**
```json
{
  "query": "Hire fresh graduates for software engineering roles",
  "top_k": 5,
  "template_type": "default"
}
```

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| query | string | Yes | - | Natural language hiring requirement |
| top_k | integer | No | 5 | Number of recommendations (1-20) |
| template_type | string | No | "default" | Prompt template ("default", "simple", "structured") |

**Response:**
```json
{
  "query": "Hire fresh graduates for software engineering roles",
  "recommendations": [
    {
      "assessment_name": "Coding Skills Assessment - Python",
      "relevance_score": 9.2,
      "reasoning": "This assessment directly evaluates Python programming skills essential for software engineering roles...",
      "product_id": "8",
      "category": "Technical Skills",
      "description": "Practical coding test evaluating Python programming skills...",
      "target_roles": ["Software Engineer", "Developer", "Data Scientist"],
      "skills_assessed": ["technical", "coding", "problem-solving"],
      "duration": "60 minutes",
      "similarity_score": 0.92
    },
    {
      "assessment_name": "Verify G+ (General Ability)",
      "relevance_score": 8.5,
      "reasoning": "Measures cognitive ability and problem-solving skills crucial for software engineers...",
      "product_id": "1",
      "category": "Cognitive Ability",
      "target_roles": ["Graduate", "Professional"],
      "skills_assessed": ["logical", "problem-solving", "analytical"],
      "duration": "36 minutes",
      "similarity_score": 0.85
    }
  ],
  "retrieved_count": 5,
  "processing_time": 1.23,
  "message": null
}
```

**Status Codes:**
- `200 OK`: Successful recommendation
- `400 Bad Request`: Invalid request parameters
- `500 Internal Server Error`: Server error
- `503 Service Unavailable`: Service not available

**Error Response:**
```json
{
  "error": "Vector store not found",
  "detail": "Please run build_embeddings.py first"
}
```

---

## Interactive Documentation

FastAPI provides interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Example Usage

### cURL

```bash
curl -X POST "http://localhost:8000/recommend" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Hire fresh graduates for software engineering roles",
    "top_k": 5
  }'
```

### Python

```python
import requests

url = "http://localhost:8000/recommend"
payload = {
    "query": "Hire fresh graduates for software engineering roles",
    "top_k": 5
}

response = requests.post(url, json=payload)
recommendations = response.json()

for rec in recommendations['recommendations']:
    print(f"{rec['assessment_name']}: {rec['relevance_score']}/10")
```

### JavaScript

```javascript
const url = 'http://localhost:8000/recommend';
const payload = {
  query: 'Hire fresh graduates for software engineering roles',
  top_k: 5
};

fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(payload),
})
  .then(response => response.json())
  .then(data => {
    data.recommendations.forEach(rec => {
      console.log(`${rec.assessment_name}: ${rec.relevance_score}/10`);
    });
  });
```

## Rate Limiting

Currently, no rate limiting is implemented. For production:
- Implement per-user/IP rate limits
- Consider caching frequent queries
- Monitor API usage

## CORS

CORS is enabled for all origins in development. For production:
- Configure specific allowed origins
- Set appropriate CORS policies

## Error Handling

All errors return JSON with the following structure:

```json
{
  "error": "Error message",
  "detail": "Detailed error information"
}
```

Common error scenarios:
- Empty query string → 400 Bad Request
- Vector store not loaded → 503 Service Unavailable
- LLM API failure → 500 Internal Server Error
- Invalid parameters → 400 Bad Request

## Performance

Typical response times:
- Health check: < 50ms
- Recommendations: 1-3 seconds (depends on LLM response time)

Factors affecting performance:
- LLM model choice (GPT-3.5 vs GPT-4)
- Number of results requested (top_k)
- Query complexity
- Network latency to OpenAI API

## Deployment

For production deployment:

1. Set environment variables securely
2. Use HTTPS
3. Implement authentication
4. Add rate limiting
5. Configure CORS appropriately
6. Set up monitoring and logging
7. Use a production ASGI server (e.g., Gunicorn with Uvicorn workers)

Example production command:
```bash
gunicorn api.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

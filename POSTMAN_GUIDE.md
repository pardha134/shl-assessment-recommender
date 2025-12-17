# Postman API Testing Guide

## Endpoint: POST /recommend

### Configuration

**Method:** `POST`  
**URL:** `http://localhost:8000/recommend`

### Headers
```
Content-Type: application/json
```

### Request Body (JSON)
```json
{
  "query": "Hire software engineers with Python and problem-solving skills",
  "top_k": 5
}
```

### Parameters

| Parameter | Type    | Required | Default | Description                           |
|-----------|---------|----------|---------|---------------------------------------|
| query     | string  | Yes      | -       | Natural language hiring requirement   |
| top_k     | integer | No       | 5       | Number of recommendations (1-10)      |

---

## Example Queries

### 1. Software Engineering Role
```json
{
  "query": "Hire software engineers with Python and problem-solving skills",
  "top_k": 5
}
```

### 2. Fresh Graduate
```json
{
  "query": "Hire fresh graduates for entry-level positions",
  "top_k": 3
}
```

### 3. Leadership Role
```json
{
  "query": "Assess candidates for senior management positions with leadership skills",
  "top_k": 5
}
```

### 4. Sales Position
```json
{
  "query": "Find assessments for sales representatives with customer service skills",
  "top_k": 4
}
```

### 5. Data Analyst
```json
{
  "query": "Evaluate data analysts with analytical and statistical skills",
  "top_k": 5
}
```

---

## Response Format

### Success Response (200 OK)
```json
{
  "recommended_assessments": [
    {
      "url": "https://www.shl.com/solutions/products/assessment-name/",
      "name": "Assessment Name",
      "adaptive_support": "Yes/No",
      "description": "Description of the assessment...",
      "duration": 30,
      "remote_support": "Yes/No",
      "test_type": ["Type1", "Type2"]
    }
  ]
}
```

### Error Response (400 Bad Request)
```json
{
  "detail": "Query cannot be empty"
}
```

### Error Response (500 Internal Server Error)
```json
{
  "detail": "Recommendation service not available"
}
```

---

## Other Endpoints

### 1. Health Check
**Method:** `GET`  
**URL:** `http://localhost:8000/health`  
**Response:**
```json
{
  "status": "healthy"
}
```

### 2. Root Endpoint
**Method:** `GET`  
**URL:** `http://localhost:8000/`  
**Response:**
```json
{
  "message": "SHL Assessment Recommender API",
  "version": "1.0.0",
  "status": "operational",
  "endpoints": {
    "health": "/health",
    "recommend": "/recommend",
    "docs": "/docs"
  }
}
```

### 3. Interactive Documentation
**Method:** `GET` (Open in Browser)  
**URL:** `http://localhost:8000/docs`

---

## Troubleshooting

### Connection Refused
- Make sure the API is running: `python api/main.py`
- Check if port 8000 is available

### Empty Response
- Verify the request body is valid JSON
- Check that `Content-Type: application/json` header is set

### 400 Bad Request
- Ensure `query` field is not empty
- Verify JSON syntax is correct

### 500 Internal Server Error
- Check API logs for detailed error messages
- Verify vector store is loaded
- Ensure OpenAI API key is configured in `.env`

---

## Postman Collection Import

Save this as `SHL_API.postman_collection.json` and import into Postman:

```json
{
  "info": {
    "name": "SHL Assessment Recommender API",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Get Recommendations",
      "request": {
        "method": "POST",
        "header": [
          {
            "key": "Content-Type",
            "value": "application/json"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"query\": \"Hire software engineers with Python and problem-solving skills\",\n  \"top_k\": 5\n}"
        },
        "url": {
          "raw": "http://localhost:8000/recommend",
          "protocol": "http",
          "host": ["localhost"],
          "port": "8000",
          "path": ["recommend"]
        }
      }
    },
    {
      "name": "Health Check",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "http://localhost:8000/health",
          "protocol": "http",
          "host": ["localhost"],
          "port": "8000",
          "path": ["health"]
        }
      }
    },
    {
      "name": "Root Endpoint",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "http://localhost:8000/",
          "protocol": "http",
          "host": ["localhost"],
          "port": "8000",
          "path": [""]
        }
      }
    }
  ]
}
```

---

## Quick Start

1. **Start the API:**
   ```bash
   python api/main.py
   ```

2. **Open Postman**

3. **Create POST request to:** `http://localhost:8000/recommend`

4. **Add Header:** `Content-Type: application/json`

5. **Add Body (raw JSON):**
   ```json
   {
     "query": "Your hiring requirement here",
     "top_k": 5
   }
   ```

6. **Click Send**

Done! You should see JSON recommendations in the response.

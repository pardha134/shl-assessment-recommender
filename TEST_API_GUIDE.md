# 🧪 How to Test the REST API

## Quick Start

### Step 1: Start the API Server

```bash
python start_api.py
```

The API will be available at:
- **Base URL**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

---

## Method 1: Using the Interactive Swagger UI (Easiest)

### 1. Start the API
```bash
python start_api.py
```

### 2. Open Swagger UI
Go to: **http://localhost:8000/docs**

### 3. Test the `/recommend` Endpoint

1. Click on **POST /recommend**
2. Click **"Try it out"**
3. Edit the request body:
   ```json
   {
     "query": "Hire Java developers with strong teamwork skills",
     "top_k": 5
   }
   ```
4. Click **"Execute"**
5. See the response below!

### Example Queries to Try:
- "Hire Java developers with strong teamwork skills"
- "Assessment for senior leadership positions"
- "Customer service skills evaluation"
- "Technical coding test for Python developers"

---

## Method 2: Using Python Script

### Option A: Use the Existing Test Script

```bash
python test_api_local.py
```

This will automatically test all endpoints.

### Option B: Create Your Own Test

Create a file `my_test.py`:

```python
import requests

# API endpoint
url = "http://localhost:8000/recommend"

# Request payload
payload = {
    "query": "Hire Java developers with strong teamwork skills",
    "top_k": 5
}

# Make the request
response = requests.post(url, json=payload)

# Print the response
print("Status Code:", response.status_code)
print("\nResponse:")
print(response.json())
```

Run it:
```bash
python my_test.py
```

---

## Method 3: Using cURL (Command Line)

### Test Health Endpoint
```bash
curl http://localhost:8000/health
```

### Test Recommend Endpoint
```bash
curl -X POST "http://localhost:8000/recommend" ^
  -H "Content-Type: application/json" ^
  -d "{\"query\": \"Hire Java developers with teamwork skills\", \"top_k\": 5}"
```

**Note:** On Windows CMD, use `^` for line continuation. On PowerShell or Linux/Mac, use `\`.

---

## Method 4: Using PowerShell

```powershell
# Test Health Endpoint
Invoke-RestMethod -Uri "http://localhost:8000/health" -Method Get

# Test Recommend Endpoint
$body = @{
    query = "Hire Java developers with strong teamwork skills"
    top_k = 5
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/recommend" -Method Post -Body $body -ContentType "application/json"
```

---

## Method 5: Using Postman

### 1. Download Postman
- Visit: https://www.postman.com/downloads/
- Install and open

### 2. Create a New Request

**Health Check:**
- Method: `GET`
- URL: `http://localhost:8000/health`
- Click "Send"

**Get Recommendations:**
- Method: `POST`
- URL: `http://localhost:8000/recommend`
- Headers: `Content-Type: application/json`
- Body (raw JSON):
  ```json
  {
    "query": "Hire Java developers with strong teamwork skills",
    "top_k": 5
  }
  ```
- Click "Send"

---

## Available Endpoints

### 1. Root Endpoint
```
GET http://localhost:8000/
```

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

### 2. Health Check
```
GET http://localhost:8000/health
```

**Response:**
```json
{
  "status": "healthy"
}
```

### 3. Get Recommendations
```
POST http://localhost:8000/recommend
```

**Request Body:**
```json
{
  "query": "Hire Java developers with strong teamwork skills",
  "top_k": 5
}
```

**Response:**
```json
{
  "recommended_assessments": [
    {
      "url": "https://www.shl.com/solutions/products/...",
      "name": "Java Programming Test",
      "adaptive_support": "No",
      "description": "Assesses Java programming skills...",
      "duration": 45,
      "remote_support": "Yes",
      "test_type": ["Technical", "Programming"]
    },
    ...
  ]
}
```

---

## Example Test Scenarios

### Scenario 1: Technical Role
```json
{
  "query": "Need a Python developer with data analysis skills",
  "top_k": 3
}
```

### Scenario 2: Leadership Role
```json
{
  "query": "Assessment for senior management and leadership positions",
  "top_k": 5
}
```

### Scenario 3: Customer Service
```json
{
  "query": "Evaluate customer service and communication skills",
  "top_k": 5
}
```

### Scenario 4: Graduate Hiring
```json
{
  "query": "Hire fresh graduates for entry-level positions",
  "top_k": 5
}
```

---

## Response Fields Explained

| Field | Type | Description |
|-------|------|-------------|
| `url` | string | Direct link to the assessment on SHL website |
| `name` | string | Name of the assessment |
| `adaptive_support` | string | "Yes" or "No" - whether assessment adapts to candidate |
| `description` | string | Detailed description of what the assessment measures |
| `duration` | integer | Time in minutes to complete the assessment |
| `remote_support` | string | "Yes" or "No" - whether can be taken remotely |
| `test_type` | array | List of test categories (e.g., ["Technical", "Cognitive"]) |

---

## Error Handling

### Empty Query
```json
{
  "query": "",
  "top_k": 5
}
```

**Response (400 Bad Request):**
```json
{
  "detail": "Query cannot be empty"
}
```

### Invalid top_k
```json
{
  "query": "Hire developers",
  "top_k": 100
}
```

**Response:** Automatically limited to 10 (max allowed)

---

## Performance Testing

### Test Response Time

```python
import requests
import time

url = "http://localhost:8000/recommend"
payload = {"query": "Hire Java developers", "top_k": 5}

start = time.time()
response = requests.post(url, json=payload)
end = time.time()

print(f"Response time: {end - start:.2f} seconds")
print(f"Status: {response.status_code}")
```

**Expected Response Time:**
- First request: 3-5 seconds (model loading)
- Subsequent requests: 1-2 seconds

---

## Troubleshooting

### API Won't Start

**Error:** `Address already in use`
```bash
# Kill the process using port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Then restart:
python start_api.py
```

### "Recommender not initialized"

**Solution:** Check that vector store exists:
```bash
# Verify vector store files exist
dir vector_store\shl_faiss
```

Should see:
- `index.faiss`
- `embeddings.npy`
- `metadata.json`

### "OpenAI API quota exceeded"

**Solution:** The API has fallback mode that still works! You'll get recommendations based on similarity search without LLM-generated reasoning.

---

## Quick Test Commands

### Windows PowerShell
```powershell
# Start API
python start_api.py

# In another terminal, test it:
Invoke-RestMethod -Uri "http://localhost:8000/health"
```

### Windows CMD
```cmd
# Start API
python start_api.py

# In another terminal, test it:
curl http://localhost:8000/health
```

---

## Complete Test Flow

1. **Start the API:**
   ```bash
   python start_api.py
   ```

2. **Open Swagger UI:**
   - Go to http://localhost:8000/docs

3. **Test Health:**
   - Click GET /health → Try it out → Execute

4. **Test Recommendations:**
   - Click POST /recommend → Try it out
   - Enter query: "Hire Java developers"
   - Click Execute

5. **View Results:**
   - See recommended assessments below

---

## Automated Testing

Run the complete test suite:

```bash
python test_api_local.py
```

This will test:
- ✅ Root endpoint
- ✅ Health check
- ✅ Recommendations with various queries
- ✅ Error handling
- ✅ Response format validation

---

## Next Steps

1. **Test locally** using any method above
2. **Deploy to cloud** (see STREAMLIT_DEPLOYMENT.md)
3. **Integrate with your app** using the API endpoints

---

## Summary

**Easiest Method:** Open http://localhost:8000/docs and use Swagger UI

**For Automation:** Use `test_api_local.py`

**For Integration:** Use the `/recommend` endpoint with POST requests

**Your API is ready to test! 🚀**

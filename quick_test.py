"""Quick API test - Run this after starting the API server."""
import requests
import json

print("🧪 Quick API Test\n")
print("=" * 60)

# Test 1: Health Check
print("\n1️⃣ Testing Health Endpoint...")
try:
    response = requests.get("http://localhost:8000/health")
    if response.status_code == 200:
        print("✅ Health check passed!")
    else:
        print(f"❌ Health check failed: {response.status_code}")
except Exception as e:
    print(f"❌ Cannot connect to API. Is it running?")
    print(f"   Start it with: python start_api.py")
    exit(1)

# Test 2: Get Recommendations
print("\n2️⃣ Testing Recommendations Endpoint...")
print("   Query: 'Hire Java developers with teamwork skills'")

payload = {
    "query": "Hire Java developers with teamwork skills",
    "top_k": 3
}

try:
    response = requests.post(
        "http://localhost:8000/recommend",
        json=payload
    )
    
    if response.status_code == 200:
        print("✅ Recommendations received!")
        
        result = response.json()
        assessments = result.get('recommended_assessments', [])
        
        print(f"\n📊 Found {len(assessments)} recommendations:\n")
        
        for i, assessment in enumerate(assessments, 1):
            print(f"{i}. {assessment.get('name', 'N/A')}")
            print(f"   Duration: {assessment.get('duration', 0)} minutes")
            print(f"   Type: {', '.join(assessment.get('test_type', []))}")
            print(f"   URL: {assessment.get('url', 'N/A')[:50]}...")
            print()
    else:
        print(f"❌ Request failed: {response.status_code}")
        print(f"   Response: {response.text}")
        
except Exception as e:
    print(f"❌ Error: {e}")

print("=" * 60)
print("\n✅ Test Complete!")
print("\n📚 For more testing options, see: TEST_API_GUIDE.md")
print("🌐 Interactive API docs: http://localhost:8000/docs")

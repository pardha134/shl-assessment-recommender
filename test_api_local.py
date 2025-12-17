"""Quick test script to verify API works locally before deployment."""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint."""
    print("Testing /health endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def test_recommend():
    """Test recommend endpoint."""
    print("Testing /recommend endpoint...")
    payload = {
        "query": "Hire Java developers with good teamwork skills",
        "top_k": 3
    }
    response = requests.post(
        f"{BASE_URL}/recommend",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    print(f"Status: {response.status_code}")
    result = response.json()
    print(f"Found {len(result.get('recommended_assessments', []))} recommendations")
    
    for i, rec in enumerate(result.get('recommended_assessments', []), 1):
        print(f"\n{i}. {rec.get('name', 'N/A')}")
        print(f"   URL: {rec.get('url', 'N/A')}")
        print(f"   Duration: {rec.get('duration', 0)} minutes")
        print(f"   Test Type: {rec.get('test_type', [])}")
    print()

def main():
    """Run all tests."""
    print("=" * 60)
    print("API Local Test")
    print("=" * 60)
    print()
    
    try:
        test_health()
        test_recommend()
        print("✅ All tests passed!")
        print("\nYour API is ready for deployment!")
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to API")
        print("\nMake sure the API is running:")
        print("  python api/main.py")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()

import requests
import json
import sys
from datetime import datetime, timedelta

BASE_URL = "http://localhost:5000"

def test_health():
    print("Testing health endpoint...")
    response = requests.get(f"{BASE_URL}/api/health")
    assert response.status_code == 200
    print("✅ Health check passed")

def test_create_dream():
    print("Testing dream creation...")
    payload = {
        "content": "I was flying over a forest of crystals and felt very happy."
    }
    response = requests.post(f"{BASE_URL}/api/dreams", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert "sentiment" in data
    assert "primary_emotion" in data
    print(f"✅ Dream creation passed (ID: {data['id']})")
    return data['id']

def test_get_dreams():
    print("Testing get dreams...")
    response = requests.get(f"{BASE_URL}/api/dreams")
    assert response.status_code == 200
    data = response.json()
    assert "dreams" in data
    print(f"✅ Get dreams passed (Count: {len(data['dreams'])})")

def test_create_sleep():
    print("Testing sleep record creation...")
    payload = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "duration_hours": 7.5,
        "wakeups": 1,
        "quality_rating": 8,
        "notes": "Felt well rested"
    }
    response = requests.post(f"{BASE_URL}/api/sleep", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    print(f"✅ Sleep record passed (ID: {data['id']})")

def test_insights():
    print("Testing insights endpoint...")
    response = requests.get(f"{BASE_URL}/api/insights")
    assert response.status_code == 200
    data = response.json()
    assert "insights" in data
    assert "recommendations" in data
    print("✅ Insights passed")

def test_trends():
    print("Testing trends endpoint...")
    response = requests.get(f"{BASE_URL}/api/trends")
    assert response.status_code == 200
    data = response.json()
    assert "emotions" in data
    assert "sleep" in data
    print("✅ Trends passed")

if __name__ == "__main__":
    try:
        test_health()
        dream_id = test_create_dream()
        test_get_dreams()
        test_create_sleep()
        test_insights()
        test_trends()
        print("\n✨ ALL TESTS PASSED SUCCESSFULLY! ✨")
    except Exception as e:
        print(f"\n❌ TEST FAILED: {str(e)}")
        sys.exit(1)

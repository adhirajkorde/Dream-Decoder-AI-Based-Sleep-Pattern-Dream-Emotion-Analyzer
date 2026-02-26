import requests
import unittest
import time
import random
import string

BASE_URL = "http://localhost:5000"

def random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

class TestProductionReadyE2E(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.username = f"tester_{random_string()}"
        cls.email = f"{cls.username}@example.com"
        cls.password = "TestPass123!"
        cls.token = None
        cls.user_id = None
        cls.dream_ids = []

    def test_01_signup(self):
        """Test user signup."""
        payload = {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "language_preference": "en"
        }
        response = requests.post(f"{BASE_URL}/api/auth/signup", json=payload)
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertIn("token", data)
        self.__class__.token = data["token"]
        self.__class__.user_id = data["user"]["id"]
        print(f"Signup successful: {self.username}")

    def test_02_login(self):
        """Test user login."""
        payload = {
            "username": self.username,
            "password": self.password
        }
        response = requests.post(f"{BASE_URL}/api/auth/login", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.json())
        print("Login successful")

    def test_03_english_dream_analysis(self):
        """Test English dream analysis (Positive/Joy)."""
        headers = {"Authorization": f"Bearer {self.token}"}
        payload = {"content": "I was flying over a beautiful ocean and felt so happy and victorious!"}
        response = requests.post(f"{BASE_URL}/api/dreams", json=payload, headers=headers)
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data["primary_emotion"], "joy")
        self.assertEqual(data["sentiment"], "positive")
        self.assertIn("interpretation", data)
        self.__class__.dream_ids.append(data["id"])
        print("English Dream Analysis: joy/positive - PASSED")

    def test_04_hindi_horror_analysis(self):
        """Test Hindi/Hinglish horror analysis (Fear/Negative)."""
        headers = {"Authorization": f"Bearer {self.token}"}
        # "Maine dekha ki ek bhoot mera peecha kar raha hai andhere jungle mein."
        payload = {"content": "Maine dekha ki ek bhoot mera peecha kar raha hai andhere jungle mein, main bahut dar gaya."}
        response = requests.post(f"{BASE_URL}/api/dreams", json=payload, headers=headers)
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data["primary_emotion"], "fear")
        self.assertEqual(data["sentiment"], "negative")
        print("Hindi Horror Analysis: fear/negative - PASSED")

    def test_05_marathi_victory_analysis(self):
        """Test Marathi victory analysis (Joy/Positive)."""
        headers = {"Authorization": f"Bearer {self.token}"}
        # "Mee aaj yash milavle ani mala khup aanand jhala." (I got success today and am very happy)
        payload = {"content": "Mee aaj yash milavle ani mala khup aanand jhala."}
        response = requests.post(f"{BASE_URL}/api/dreams", json=payload, headers=headers)
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data["primary_emotion"], "joy")
        self.assertEqual(data["sentiment"], "positive")
        print("Marathi Victory Analysis: joy/positive - PASSED")

    def test_06_sleep_log_management(self):
        """Test saving and getting sleep logs."""
        headers = {"Authorization": f"Bearer {self.token}"}
        payload = {
            "date": "2026-02-24",
            "duration_hours": 8,
            "wakeups": 1,
            "quality_rating": 4,
            "notes": "Felt good after a long time."
        }
        response = requests.post(f"{BASE_URL}/api/sleep", json=payload, headers=headers)
        self.assertEqual(response.status_code, 201)
        
        # Get sleep stats
        response = requests.get(f"{BASE_URL}/api/sleep/stats", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["total_records"], 1)
        print("Sleep Log Management - PASSED")

    def test_07_analytics_insights(self):
        """Test insights and trends endpoints."""
        headers = {"Authorization": f"Bearer {self.token}"}
        
        # Insights
        response = requests.get(f"{BASE_URL}/api/insights", headers=headers)
        self.assertEqual(response.status_code, 200)
        
        # Trends
        response = requests.get(f"{BASE_URL}/api/trends", headers=headers)
        self.assertEqual(response.status_code, 200)
        print("Analytics & Insights - PASSED")

    def test_08_account_deletion(self):
        """Test full account deletion (Cascading)."""
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.delete(f"{BASE_URL}/api/auth/account", headers=headers)
        self.assertEqual(response.status_code, 200)
        
        # Verify login fails now
        payload = {"username": self.username, "password": self.password}
        response = requests.post(f"{BASE_URL}/api/auth/login", json=payload)
        self.assertEqual(response.status_code, 401)
        print("Account Deletion & Data Wipe - PASSED")

if __name__ == "__main__":
    unittest.main()

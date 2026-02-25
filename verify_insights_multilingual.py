
import sys
import os
from datetime import datetime, timedelta

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.services.insights_generator import generate_insights
from backend.models.dream import Dream
from backend.models.user import User
from backend.database.db import get_db_connection

def test_language(lang):
    print(f"\n--- Testing Insights for Language: {lang} ---")
    # Using a dummy user ID that likely has dreams (from previous research we saw user_id 2 has dreams)
    user_id = 2 
    insights = generate_insights(user_id, days=7, language=lang)
    
    print(f"Total Insights: {len(insights['insights'])}")
    for insight in insights['insights']:
        print(f"[{insight['type'].upper()}] {insight['title']}")
        print(f"Message: {insight['message']}")
        print("-" * 20)
    
    if insights['health_tips']:
        print(f"Health Tips: {len(insights['health_tips'])}")
        tip = insights['health_tips'][0]
        print(f"Title: {tip['title']}")
        print(f"Insight: {tip['insight']}")

if __name__ == "__main__":
    # Set console output to utf-8 if possible, or just write to file
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    # Test all supported languages
    languages = ['en', 'hi', 'mr', 'hinglish']
    for lang in languages:
        try:
            test_language(lang)
        except UnicodeEncodeError:
            print(f"Skipping detailed print for {lang} due to terminal encoding limitations.")


import sys
import os

# Ensure backend can be imported
sys.path.append(os.getcwd())

from backend.services.nlp_engine import analyze_dream

def test_analysis():
    print("Testing Dream Analysis...")
    test_text = "I was flying over a vast ocean and felt very happy."
    
    try:
        print(f"Input text: {test_text}")
        result = analyze_dream(test_text, user_language='en')
        print("Analysis successful!")
        print(f"Sentiment: {result['sentiment']}")
        print(f"Primary Emotion: {result['primary_emotion']}")
        print(f"Summary: {result['summary']}")
    except Exception as e:
        print(f"Analysis FAILED: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    test_analysis()

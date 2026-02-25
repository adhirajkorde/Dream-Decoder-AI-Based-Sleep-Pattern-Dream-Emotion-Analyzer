
import sys
import os

# Ensure the parent directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.services.nlp_engine import analyze_dream

text = "\u092e\u0930\u093e\u0920\u0940: \u092e\u0940 \u0938\u092e\u0941\u0926\u094d\u0930\u0915\u093f\u0928\u093e\u0930\u0940 \u092c\u0938\u0932\u094b \u0939\u094b\u0924\u094b, \u0932\u093e\u091f\u093e \u0936\u093e\u0902\u0924 \u0939\u094b\u0924\u094d\u092f\u093e."
# Remove the prefix for actual test
text = "\u092e\u0940 \u0938\u092e\u0941\u0926\u094d\u0930\u0915\u093f\u0928\u093e\u0930\u0940 \u092c\u0938\u0932\u094b \u0939\u094b\u0924\u094b, \u0932\u093e\u091f\u093e \u0936\u093e\u0902\u0924 \u0939\u094b\u0924\u094d\u092f\u093e."

analysis = analyze_dream(text, 'mr')
print(f"Text: {text}")
print(f"Emotion: {analysis['primary_emotion']}")
print(f"Sentiment: {analysis['sentiment']}")
print(f"Scores: {analysis.get('emotion_scores', {})}")
print(f"Sentiment Score: {analysis.get('sentiment_score', 0)}")
print(f"Summary: {analysis['summary']}")


import sys
import os

# Ensure the parent directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.services.emotion_analyzer import analyze_emotions, REINFORCEMENT_KEYWORDS
from backend.services.sentiment_analyzer import analyze_sentiment

text = "कल मैंने एक घर देखा जहाँ कोई नहीं था।"
text_lower = text.lower()

print(f"Text: {text}")

# Check house mention
is_house_mention = any(h in text_lower for h in ['home', 'house', 'ghar', '\u0918\u0930'])
print(f"is_house_mention: {is_house_mention}")

# Check safety markers
safety_markers = [
    'peace', 'light', 'shanti', 'shant', 'bright', 'prakash', 'asha', 'shaanti',
    '\u0936\u093e\u0902\u0924\u093f', '\u092a\u094d\u0930\u0915\u093e\u0936', '\u0906\u0936\u093e', '\u0936\u093e\u0902\u0924', 'divinity', 'divine', 'divya', '\u0926\u093f\u0935\u094d\u092f'
]
found_safety = [m for m in safety_markers if m in text_lower]
print(f"Found Safety Markers: {found_safety}")

# Check joy keywords
joy_keywords = REINFORCEMENT_KEYWORDS['joy']
found_joy = [kw for kw in joy_keywords if kw in text_lower]
print(f"Found Joy Keywords: {found_joy}")

# Run analysis
emo_result = analyze_emotions(text)
sent_result = analyze_sentiment(text)

print(f"\nEmotion Result: {emo_result}")
print(f"Sentiment Result: {sent_result}")

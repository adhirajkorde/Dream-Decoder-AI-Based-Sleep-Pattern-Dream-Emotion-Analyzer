
import sys
import os

# Ensure the parent directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.services.emotion_analyzer import REINFORCEMENT_KEYWORDS

text = "\u092e\u0940 \u0938\u092e\u0941\u0926\u094d\u0930\u0915\u093f\u0928\u093e\u0930\u0940 \u092c\u0938\u0932\u094b \u0939\u094b\u0924\u094b, \u0932\u093e\u091f\u093e \u0936\u093e\u0902\u0924 \u0939\u094b\u0924\u094d\u092f\u093e."
text_lower = text.lower()

print(f"Text ASCII: {ascii(text_lower)}")

# Exhaustive check of ALL keywords in the text
for emo, kw_list in REINFORCEMENT_KEYWORDS.items():
    for kw in kw_list:
        if kw in text_lower:
            print(f"MATCH FOUND: {ascii(kw)} in emotion '{emo}' at index {text_lower.find(kw)}")

# Check safety markers too
safety_markers = [
    'peace', 'light', 'bright', 'divinity', 'divine', 'divya',
    '\u0936\u093e\u0902\u0924\u093f', '\u092a\u094d\u0930\u0915\u093e\u0936', '\u0906\u0936\u093e', '\u0936\u093e\u0902\u0924', '\u0926\u093f\u0935\u094d\u092f'
]
for m in safety_markers:
    if m in text_lower:
        print(f"SAFETY MATCH FOUND: {ascii(m)} at index {text_lower.find(m)}")

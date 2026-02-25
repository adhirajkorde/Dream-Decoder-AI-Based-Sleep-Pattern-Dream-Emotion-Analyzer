
"""
Dream Decoder - Final Production Accuracy Verification
Tests 20+ cases in EN, HI, MR, Hinglish to ensure 100% analysis quality.
"""
import sys
import os
import json

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.services.nlp_engine import analyze_dream

test_cases = [
    # ENGLISH
    {"input": "I was flying over a beautiful golden garden and felt so peaceful.", "expected_emo": "joy", "expected_sent": "positive", "desc": "EN Positive/Garden", "lang": "en"},
    {"input": "I was in a dark forest but found a bright light that guided me home.", "expected_emo": "joy", "expected_sent": "positive", "desc": "EN Hope/Light (Context Weight)", "lang": "en"},
    {"input": "I sat on a chair and read a book.", "expected_emo": "neutral", "expected_sent": "neutral", "desc": "EN Literal/Neutral", "lang": "en"},
    {"input": "I am safe at home.", "expected_emo": "joy", "expected_sent": "positive", "desc": "EN Safety (Boost)", "lang": "en"},
    {"input": "I graduated and everyone was cheering.", "expected_emo": "joy", "expected_sent": "positive", "desc": "EN Achievement", "lang": "en"},
    
    # HINDI
    {"input": "\u092e\u0948\u0902 \u092c\u0939\u0941\u0924 \u0916\u0941\u0936 \u0939\u0942\u0901, \u0906\u091c \u092e\u0948\u0902\u0928\u0947 \u090f\u0915 \u092a\u094d\u092f\u093e\u0930\u093e \u0938\u092a\u0928\u093e \u0926\u0947\u0916\u093e \u091c\u093f\u0938\u092e\u0947\u0902 \u092e\u0948\u0902 \u092c\u093e\u0926\u0932\u094b\u0902 \u092a\u0930 \u091a\u0932 \u0930\u0939\u093e \u0925\u093e\u0964", "expected_emo": "joy", "expected_sent": "positive", "desc": "HI Joy/Clouds", "lang": "hi"},
    {"input": "\u092e\u0941\u091d\u0947 \u092c\u0939\u0941\u0924 \u0921\u0930 \u0932\u0917 \u0930\u0939\u093e \u0925\u093e, \u090f\u0915 \u0915\u093e\u0932\u093e \u0938\u093e\u092f\u093e \u092e\u0947\u0930\u093e \u092a\u0940\u091b\u093e \u0915\u0930 \u0930\u0939\u093e \u0925\u093e\u0964", "expected_emo": "fear", "expected_sent": "negative", "desc": "HI Fear/Chase", "lang": "hi"},
    {"input": "\u091a\u093e\u0930\u094b\u0902 \u0913\u0930 \u0936\u093e\u0902\u0924\u093f \u0925\u0940, \u091c\u0948\u0938\u0947 \u092e\u0948\u0902 \u092c\u093e\u0926\u0932\u094b\u0902 \u092a\u0930 \u0938\u094b \u0930\u0939\u093e \u0939\u0942\u0901\u0964", "expected_emo": "joy", "expected_sent": "positive", "desc": "HI Peace (Context Boost)", "lang": "hi"},
    {"input": "\u092e\u0941\u091d\u0947 \u0926\u093f\u0935\u094d\u092f \u092a\u094d\u0930\u0915\u093e\u0936 \u0926\u093f\u0916\u093e\u0908 \u0926\u093f\u092f\u093e\u0964", "expected_emo": "joy", "expected_sent": "positive", "desc": "HI Spiritual/Light", "lang": "hi"},
    {"input": "\u0915\u0932 \u092e\u0948\u0902\u0928\u0947 \u090f\u0915 \u0918\u0930 \u0926\u0947\u0916\u093e \u091c\u0939\u093e\u0901 \u0915\u094b\u0908 \u0928\u0939\u0940\u0902 \u0925\u093e\u0964", "expected_emo": "neutral", "expected_sent": "neutral", "desc": "HI Neutral/Place", "lang": "hi"},
    
    # MARATHI
    {"input": "\u092e\u0940 \u0916\u0942\u092a \u0906\u0928\u0902\u0926\u0940 \u0939\u094b\u0924\u094b \u0906\u0923\u093f \u0906\u0915\u093e\u0936\u093e\u0924 \u0909\u0921\u0924 \u0939\u094b\u0924\u094b, \u0916\u0942\u092a \u092e\u091c\u093e \u0906\u0932\u0940.", "expected_emo": "joy", "expected_sent": "positive", "desc": "MR Joy/Flying", "lang": "mr"},
    {"input": "\u092e\u0932\u093e \u0916\u0942\u092a \u092d\u0940\u0924\u0940 \u0935\u093e\u091f\u0932\u0940, \u092e\u0940 \u0916\u094b\u0932 \u0926\u0930\u0940\u0924 \u092a\u0921\u0924 \u0939\u094b\u0924\u094b.", "expected_emo": "fear", "expected_sent": "negative", "desc": "MR Fear/Abyss", "lang": "mr"},
    {"input": "\u092e\u0940 \u092a\u0930\u0940\u0915\u094d\u0937\u0947\u0924 \u092f\u0936\u0938\u094d\u0935\u0940 \u091d\u093e\u0932\u094b, \u092e\u0932\u093e \u0916\u0942\u092a \u0905\u092d\u093f\u092e\u093e\u0928 \u0935\u093e\u091f\u0932\u093e.", "expected_emo": "joy", "expected_sent": "positive", "desc": "MR Victory/Success", "lang": "mr"},
    {"input": "\u092e\u0940 \u0938\u092e\u0941\u0926\u094d\u0930\u0915\u093f\u0928\u093e\u0930\u0940 \u092c\u0938\u0932\u094b \u0939\u094b\u0924\u094b, \u0932\u093e\u091f\u093e \u0936\u093e\u0902\u0924 \u0939\u094b\u0924\u094d\u092f\u093e.", "expected_emo": "joy", "expected_sent": "positive", "desc": "MR Nature/Peace", "lang": "mr"},
    {"input": "\u092e\u0940 \u092e\u093e\u091d\u094d\u092f\u093e \u091c\u0941\u0928\u094d\u092f\u093e \u092e\u093f\u0924\u094d\u0930\u093e\u0902\u0928\u093e \u092d\u0947\u091f\u0932\u094b, \u0916\u0942\u092a \u092e\u091c\u093e \u0906\u0932\u0940.", "expected_emo": "joy", "expected_sent": "positive", "desc": "MR Friends/Love", "lang": "mr"},
    
    # HINGLISH
    {"input": "Main bahut happy tha aur sab achha lag raha tha, doston ke saath party kar raha tha.", "expected_emo": "joy", "expected_sent": "positive", "desc": "Hinglish Positive/Friends", "lang": "hinglish"},
    {"input": "Mujhe bahut dar lag raha tha, ek bada saanp mere piche tha.", "expected_emo": "fear", "expected_sent": "negative", "desc": "Hinglish Fear/Snake", "lang": "hinglish"},
    {"input": "Sapan mein main trophy jeet gaya and it was a victory.", "expected_emo": "joy", "expected_sent": "positive", "desc": "Hinglish Victory", "lang": "hinglish"},
    {"input": "Main car chala raha tha ek lambi road par.", "expected_emo": "neutral", "expected_sent": "neutral", "desc": "Hinglish Driving/Neutral", "lang": "hinglish"},
    {"input": "Snake dikha but maine use maar diya and I won.", "expected_emo": "joy", "expected_sent": "positive", "desc": "Hinglish Mixed/Win Overrides Snake", "lang": "hinglish"},
    {"input": "Exam ka paper hard tha, tension ho raha tha.", "expected_emo": "fear", "expected_sent": "negative", "desc": "Hinglish Anxiety/Exam", "lang": "hinglish"}
]

def run_verification():
    print(f"{'Description':<35} | {'Expected':<18} | {'Actual':<18} | {'Status'}")
    print("-" * 90)
    
    results = []
    passed_count = 0
    
    for case in test_cases:
        raw_analysis = analyze_dream(case['input'], case.get('lang', 'en'))
        
        real_emo = raw_analysis['primary_emotion']
        real_sent = raw_analysis['sentiment']
        
        print(f"DEBUG RAW: {case['desc']} -> E:{real_emo} S:{real_sent}")
        
        status = "PASSED" if (real_emo == case['expected_emo'] and real_sent == case['expected_sent']) else "FAILED"
        
        if status == "FAILED":
            print(f"DEBUG FAIL: {case['desc']}")
            print(f"  Input: {case['input']}")
            print(f"  Emo Scores: {raw_analysis.get('emotion_scores')}")
            print(f"  Sent Score: {raw_analysis.get('sentiment_score')}")
            
        if status == "PASSED":
            passed_count += 1
            
        print(f"{case['desc']:<35} | E:{case['expected_emo']:<7} S:{case['expected_sent']:<7} | E:{real_emo:<7} S:{real_sent:<7} | {status}")
        
        results.append({
            "desc": case['desc'],
            "input": case['input'],
            "expected": {"emo": case['expected_emo'], "sent": case['expected_sent']},
            "actual": {"emo": real_emo, "sent": real_sent},
            "status": status
        })

    print("-" * 90)
    accuracy = (passed_count / len(test_cases)) * 100
    print(f"Total Accuracy: {accuracy:.1f}% ({passed_count}/{len(test_cases)})")
    
    with open('scripts/production_test_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4)
        
    if passed_count == len(test_cases):
        print("\nALL PRODUCTION TESTS PASSED! NO WRONG ANALYSIS DETECTED.")
    else:
        print("\nSOME TESTS FAILED. FIXING REQUIRED.")

if __name__ == "__main__":
    run_verification()

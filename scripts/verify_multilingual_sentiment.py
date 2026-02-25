import sys
import os
import json

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.services.nlp_engine import analyze_dream

def run_tests():
    test_cases = [
        {
            "text": "आज मैं बहुत खुश हूँ, मैंने एक प्यारा सपना देखा जिसमें मैं बादलों पर चल रहा था।",
            "expected_sentiment": "positive",
            "description": "Hindi Positive (Happy/Clouds)"
        },
        {
            "text": "मी खूप आनंदी होतो आणि आकाशात पक्षांसारखा उडत होतो, खूप मजा आली.",
            "expected_sentiment": "positive",
            "description": "Marathi Positive (Happy/Flying)"
        },
        {
            "text": "Main bahut happy tha aur sab achha lag raha tha, doston ke saath party kar raha tha.",
            "expected_sentiment": "positive",
            "description": "Hinglish Positive (Happy/Friends/Party)"
        },
        {
            "text": "I saw a car parked in front of a house.",
            "expected_sentiment": "neutral",
            "description": "English Neutral (Literal objects)"
        },
        {
            "text": "Mujhe bahut dar lag raha tha, ek bada saanp mere piche tha.",
            "expected_sentiment": "negative",
            "description": "Hinglish Negative (Fear/Snake/Chase)"
        },
        {
            "text": "मला खूप भीती पडण्याची आणि काळोखात हरवल्यासारखं वाटलं.",
            "expected_sentiment": "negative",
            "description": "Marathi Negative (Fear/Falling/Darkness)"
        },
        {
            "text": "I saw a cat.",
            "expected_sentiment": "neutral",
            "description": "Very Short Dream (Deep-dive check)"
        }
    ]
    
    results = []
    for case in test_cases:
        print(f"Testing: {case['description']}...")
        result = analyze_dream(case['text'])
        
        actual_sentiment = result.get('sentiment')
        actual_emotion = result.get('primary_emotion')
        interpretation = result.get('interpretation', {})
        
        # QUALITY CHECKS
        has_elements = len(interpretation.get('numbered_elements', [])) > 0
        has_narrative = len(interpretation.get('overall_interpretation', '')) > 50
        has_insight = len(interpretation.get('final_insight', '')) > 20
        
        # Check for weak labels
        weak_labels = ["Needs Improvement", "Too Simple", "Incomplete"]
        is_weak = any(label in str(interpretation) for label in weak_labels)
        
        status = "PASSED" if (actual_sentiment == case['expected_sentiment'] and has_narrative and not is_weak) else "FAILED"
        
        results.append({
            "description": case['description'],
            "input": case['text'],
            "expected": case['expected_sentiment'],
            "actual": actual_sentiment,
            "status": status,
            "quality": {
                "has_elements": has_elements,
                "narrative_length": len(interpretation.get('overall_interpretation', '')),
                "has_insight": has_insight,
                "is_weak": is_weak
            },
            "interpretation_snippet": interpretation.get('overall_interpretation', '')[:100]
        })
    
    with open('scripts/test_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    
    print(f"\nFinal Verification Results (Summary):")
    for r in results:
        print(f"[{r['status']}] {r['description']}")
    
    print(f"\nDetailed results saved to scripts/test_results.json")

if __name__ == "__main__":
    run_tests()

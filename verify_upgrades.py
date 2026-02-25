import sys
import os

# Add the project root to sys.path
sys.path.append(os.getcwd())

from backend.services.nlp_engine import analyze_dream

def test_flying_car():
    print("\n" + "="*50)
    print("TEST CASE: FLYING CAR DREAM")
    print("="*50)
    
    dream_text = "I was driving a flying car through a small city. I felt very happy and excited, everything was moving so fast!"
    result = analyze_dream(dream_text)
    
    print(f"Dream: {dream_text}")
    print(f"Detected Keywords: {result['keywords']}")
    print(f"Primary Emotion: {result['primary_emotion']}")
    print(f"Sentiment: {result['sentiment']}")
    print("-" * 30)
    print("Interpretation:")
    interpretation = result['interpretation']
    print(f"Overall: {interpretation['overall_interpretation']}")
    print(f"DEBUG_LOW: {interpretation['overall_interpretation'].lower()}")
    print("\nNumbered Elements:")

    for el in interpretation['numbered_elements']:
        print(f"{el['number']}. {el['element']} (Weight: {el.get('weight', 'N/A')})")
        print(f"   Symbolic Meaning: {el['symbolic_meaning']}")
    print(f"\nFinal Insight: {interpretation['final_insight']}")
    
    # Assertions for verification
    # 1. Preprocessing: "flying car" or "flying" + "car" detected
    has_flying = any("fly" in k.lower() for k in result['keywords'])
    has_car = any("car" in k.lower() for k in result['keywords'])
    print(f"\n[CHECK] Preprocessing: Flying={has_flying}, Car={has_car}")
    
    # 2. Consistency: Joy emotion -> Not Negative sentiment
    is_consistent = not (result['primary_emotion'] == 'joy' and result['sentiment'] == 'negative')
    print(f"[CHECK] Consistency (Joy != Negative): {is_consistent}")
    
    # 3. Conflict Detection: "inner conflict" should not be in interpretation
    no_conflict = "inner conflict" not in interpretation['overall_interpretation'].lower()
    print(f"[CHECK] Conflict Detection (No 'inner conflict'): {no_conflict}")
    
    # 4. Weighting: Flying (Weight 3) should be high up
    top_element = interpretation['numbered_elements'][0]['element'].lower()
    is_weighted = "flying" in top_element
    print(f"[CHECK] Weighting (Flying is top): {is_weighted}")

def test_conflict_case():
    print("\n" + "="*50)
    print("TEST CASE: DARK FOREST (CONFLICT)")
    print("="*50)
    
    dream_text = "I was lost in a dark forest and felt very scared. Something was chasing me."
    result = analyze_dream(dream_text)
    
    print(f"Dream: {dream_text}")
    print(f"Primary Emotion: {result['primary_emotion']}")
    print(f"Sentiment: {result['sentiment']}")
    print(f"Overall Interpretation: {result['interpretation']['overall_interpretation']}")
    
    # Conflict SHOULD be detected here (emotion fear + fear context)
    has_conflict = "inner conflict" in result['interpretation']['overall_interpretation'].lower()
    print(f"\n[CHECK] Conflict Detection (Has 'inner conflict'): {has_conflict}")

if __name__ == "__main__":
    try:
        test_flying_car()
        test_conflict_case()
    except Exception as e:
        print(f"An error occurred during verification: {e}")
        import traceback
        traceback.print_exc()

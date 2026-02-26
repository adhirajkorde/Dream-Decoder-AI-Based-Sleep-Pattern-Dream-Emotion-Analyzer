import sys
import os
import unittest

# Add parent directory to path to import backend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.services.nlp_engine import analyze_dream

class TestDreamAccuracy(unittest.TestCase):
    
    def test_horror_dream_alignment(self):
        """Verify that horror dreams are strictly forced to Fear/Negative."""
        dreams = [
            "I was chased by a scary ghost in the dark forest and I felt terrified.",
            "Ek bhoot mera peecha kar raha tha andhera mein, main bahut dar gaya tha.", # Hinglish
            "Main bahut dar gaya tha jab maine ek khooni bhoot dekha.", # Hindi
            "Andharyat mala ek bhoota ne dharle, mee khup ghabarlo hoto." # Marathi
        ]
        
        for dream in dreams:
            result = analyze_dream(dream)
            print(f"\nTesting Horror: {dream[:50]}...")
            print(f"Result: {result['primary_emotion']} / {result['sentiment']}")
            
            self.assertEqual(result['primary_emotion'], 'fear', f"Failed fear override for: {dream}")
            self.assertEqual(result['sentiment'], 'negative', f"Failed negative sentiment alignment for: {dream}")

    def test_joy_success_alignment(self):
        """Verify that success dreams are strictly forced to Joy/Positive."""
        dreams = [
            "I finally won the championship and received a beautiful golden trophy!",
            "Maine exam mein top kiya aur mujhe award mila, main bahut khush hoon.", # Hinglish
            "Mee spardhet pratham alo ani mala khup aanand jhala.", # Marathi
            "Victory is mine, I achieved my goal and felt divine peace."
        ]
        
        for dream in dreams:
            result = analyze_dream(dream)
            print(f"\nTesting Joy: {dream[:50]}...")
            print(f"Result: {result['primary_emotion']} / {result['sentiment']}")
            
            self.assertEqual(result['primary_emotion'], 'joy', f"Failed joy override for: {dream}")
            self.assertEqual(result['sentiment'], 'positive', f"Failed positive sentiment alignment for: {dream}")

    def test_neutral_house_logic(self):
        """Verify that literal house mentions without strong emotion stay neutral."""
        dreams = [
            "I saw a house.",
            "Ek ghar dikha.",
            "Mee ek ghar pahile.",
            "I was just sitting in a house, looking at the wall."
        ]
        
        for dream in dreams:
            result = analyze_dream(dream)
            print(f"\nTesting Neutral House: {dream[:50]}...")
            print(f"Result: {result['primary_emotion']} / {result['sentiment']}")
            
            self.assertEqual(result['primary_emotion'], 'neutral', f"Failed neutral literal check for: {dream}")
            self.assertEqual(result['sentiment'], 'neutral', f"Failed neutral sentiment for: {dream}")

    def test_symbol_verification(self):
        """Verify that symbols in interpretation actually exist in the dream text."""
        dream = "I was flying in a car over the ocean."
        result = analyze_dream(dream)
        
        elements = [e['element'].lower() for e in result['interpretation']['numbered_elements']]
        print(f"\nTesting Symbols for: {dream}")
        print(f"Symbols found: {elements}")
        
        # 'Flying' and 'Car' or 'Ocean' should be there if they are in symbols dataset
        # But most importantly, something like 'Ghost' should NOT be there.
        self.assertNotIn('ghost', elements, "Imaginary symbol 'ghost' found!")
        
        # Verify all found elements are actually in the text (case-insensitive)
        text_lower = dream.lower()
        for element in elements:
            # Note: element might be formatted differently or be a lemma, 
            # but for this test we check if the root is present.
            # (Simple check for this specific test case)
            found = any(word in text_lower for word in element.split())
            self.assertTrue(found, f"Symbol '{element}' not found in dream text!")

if __name__ == '__main__':
    unittest.main()

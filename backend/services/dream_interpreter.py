"""
Dream Decoder - Dream Interpreter Service
Provides deep psychological and symbolic analysis of dream content.
"""
import re

# Comprehensive Symbol Database
SYMBOL_DATABASE = {
    'water': {
        'symbolic': 'Represents the emotional state and the flow of the subconscious mind.',
        'subconscious': 'The clarity or turbulence of the water suggests how you are currently processing your feelings.'
    },
    'flying': {
        'symbolic': 'A symbol of liberation, release, and rising above current circumstances.',
        'subconscious': 'Indicates a desire for freedom or a sense of achievement and empowerment.'
    },
    'falling': {
        'symbolic': 'Represents a loss of control, insecurity, or a fear of failure.',
        'subconscious': 'Suggests you might be feeling overwhelmed or unsupported in some area of your waking life.'
    },
    'chased': {
        'symbolic': 'Symbolizes avoidance of a situation or emotion that needs to be addressed.',
        'subconscious': 'The "pursuer" often represents a part of yourself or a responsibility you are trying to escape.'
    },
    'house': {
        'symbolic': 'Represents the self or the structure of your own mind and personality.',
        'subconscious': 'Different rooms can represent different aspects of your life (e.g., attic for thoughts, basement for hidden fears).'
    },
    'forest': {
        'symbolic': 'A place of mystery, the unconscious, or a state of confusion.',
        'subconscious': 'Suggests you are navigating unfamiliar territory within your own psyche or life path.'
    },
    'bridge': {
        'symbolic': 'Symbolizes transition, change, or connecting two different states of being.',
        'subconscious': 'Indicates you are in the middle of a significant life shift or trying to overcome a gap.'
    },
    'death': {
        'symbolic': 'Represents transformation, endings, and the birth of something new.',
        'subconscious': 'Not a literal prediction, but a sign that an old way of thinking or living is making way for growth.'
    },
    'teeth': {
        'symbolic': 'Often related to communication, self-image, and personal power.',
        'subconscious': 'Losing teeth frequently indicates anxiety about how you are perceived or a fear of losing influence.'
    },
    'snake': {
        'symbolic': 'A complex symbol representing healing, transformation, or a hidden threat.',
        'subconscious': 'Can suggest a process of shedding old habits or dealing with a person you perceive as untrustworthy.'
    },
    'fire': {
        'symbolic': 'Represents passion, anger, destruction, or purification and rebirth.',
        'subconscious': 'The context of the fire shows whether you are feeling consumed by an emotion or energized by it.'
    },
    'mountain': {
        'symbolic': 'Symbolizes challenges, goals, and the perspective gained through effort.',
        'subconscious': 'Suggests you are focused on an upcoming milestone or seeking a "higher" view of a situation.'
    },
    'people': {
        'symbolic': 'Often represent different facets of the dreamer\'s own personality.',
        'subconscious': 'The traits of the person in the dream are usually qualities you are currently integrating or confronting in yourself.'
    },
    'ocean': {
        'symbolic': 'The vast, deep expanse of the collective unconscious and deep-seated emotions.',
        'subconscious': 'A calm ocean indicates inner peace, while a stormy one suggests emotional turmoil.'
    },
    'door': {
        'symbolic': 'Represents new opportunities or barriers depending on whether it is open or closed.',
        'subconscious': 'Suggests your readiness (or hesitation) to enter a new phase of life or explore hidden ideas.'
    },
    'car': {
        'symbolic': 'Represents the direction of your life and how much control you feel you have over it.',
        'subconscious': 'Being in the driver\'s seat shows agency; being a passenger suggests you feel others are in control.'
    }
}

def interpret_dream(text, nlp_analysis):
    """
    Generate a structured psychological interpretation of the dream.
    
    Args:
        text: Original dream description
        nlp_analysis: Dict containing 'keywords', 'entities', 'emotion', 'sentiment'
        
    Returns:
        Dict with interpretation structure
    """
    keywords = nlp_analysis.get('keywords', [])
    entities = nlp_analysis.get('entities', [])
    
    # 1. Extract and Analyze Elements
    elements = _extract_elements(text, keywords, entities)
    numbered_elements = []
    
    for i, element_text in enumerate(elements, 1):
        matching_symbol = _find_matching_symbol(element_text)
        
        if matching_symbol:
            symbol_data = SYMBOL_DATABASE[matching_symbol]
            symbolic_meaning = symbol_data['symbolic']
            subconscious_insight = symbol_data['subconscious']
        else:
            # Generic interpretation if no specific symbol matches
            symbolic_meaning = "This element represents a focal point of your subconscious attention within this dream sequence."
            subconscious_insight = "It suggests your mind is currently processing this specific detail as it relates to your personal context."
            
        numbered_elements.append({
            'number': i,
            'element': element_text.capitalize(),
            'symbolic_meaning': symbolic_meaning,
            'subconscious_insight': subconscious_insight
        })
        
    # 2. Overall Interpretation
    overall_interpretation = _generate_overall_interpretation(numbered_elements, nlp_analysis)
    
    # 3. Final Insight
    final_insight = _generate_final_insight(overall_interpretation, nlp_analysis)
    
    return {
        'numbered_elements': numbered_elements,
        'overall_interpretation': overall_interpretation,
        'final_insight': final_insight
    }

def _extract_elements(text, keywords, entities):
    """Break dream into key scenes/elements using NLP help."""
    # Split into sentences as a base for scenes
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    
    # Combine keywords and entities to find significant phrases
    focal_points = keywords[:5] + [e['text'] for e in entities[:3]]
    
    elements = []
    seen_elements = set()
    
    # Strategy: Find sentences that contain major focal points
    for sentence in sentences:
        for fp in focal_points:
            if fp.lower() in sentence.lower():
                # Extract a concise version of the scene
                # If the sentence is too long, we might just use the focal point in context
                if len(sentence) > 100:
                    element = f"The presence of {fp}"
                else:
                    element = sentence
                
                if element.lower() not in seen_elements:
                    elements.append(element)
                    seen_elements.add(element.lower())
                break
    
    # Fallback if no focal points found in sentences
    if not elements and focal_points:
        elements = [f"The element of {fp}" for fp in focal_points[:3]]
    elif not elements and sentences:
        elements = sentences[:3]
    
    return elements[:5] # Limit to top 5 elements

def _find_matching_symbol(text):
    """Find a symbol from our database within the given text."""
    text_lower = text.lower()
    for symbol in SYMBOL_DATABASE:
        if symbol in text_lower:
            return symbol
    return None

def _generate_overall_interpretation(elements, nlp_analysis):
    """Combine analysis into a cohesive narrative."""
    emotion = nlp_analysis.get('emotion', {}).get('primary_emotion', 'neutral')
    sentiment = nlp_analysis.get('sentiment', {}).get('sentiment', 'neutral')
    
    if not elements:
        return "This dream seems to be a subtle reflection of your current mental state, characterized by a {} emotional tone.".format(emotion)
    
    intro = "Your dream weaves together symbols of {} with a strong {} emotional undercurrent.".format(
        ", ".join([e['element'].lower() for e in elements[:2]]),
        emotion
    )
    
    mid = "The interaction of these elements suggests you are currently navigating a phase of {}.".format(
        "inner growth" if sentiment == 'positive' else "inner conflict" if sentiment == 'negative' else "reflection"
    )
    
    closing = "Ultimately, your subconscious is bringing these specific details to your attention to help you process your experiences."
    
    return f"{intro} {mid} {closing}"

def _generate_final_insight(interpretation, nlp_analysis):
    """Create a gentle reflective message."""
    emotion = nlp_analysis.get('emotion', {}).get('primary_emotion', 'neutral')
    
    if emotion == 'fear':
        return "Take comfort in knowing that your mind is safely processing these anxieties while you sleep. You have the strength to face what's chasing you."
    elif emotion == 'joy':
        return "Your subconscious is celebrating your current path. Carry this positive energy with you into your waking hours."
    elif emotion == 'sadness':
        return "Allow yourself the grace to feel these emotions. This dream is a step toward healing and emotional release."
    else:
        return "Trust your intuition as you reflect on these symbols. Your inner self is a wise guide on your journey of growth."

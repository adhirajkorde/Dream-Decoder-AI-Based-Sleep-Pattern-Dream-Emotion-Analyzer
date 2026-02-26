"""
Dream Decoder - Emotion Analyzer
Uses HuggingFace transformers for emotion detection
"""
from backend.config import EMOTION_MODEL

# Global model instance (lazy loaded)
_emotion_classifier = None


def get_emotion_classifier():
    """Get or initialize the emotion classifier."""
    global _emotion_classifier
    if _emotion_classifier is None:
        from transformers import pipeline
        print("Loading emotion detection model...")
        _emotion_classifier = pipeline(
            "text-classification",
            model=EMOTION_MODEL,
            top_k=None  # Return all emotion scores
        )
        print("Emotion model loaded!")
    return _emotion_classifier


# Mapping GoEmotions (28 labels) to core dream emotions
GO_EMOTIONS_MAPPING = {
    'admiration': 'love',
    'amusement': 'joy',
    'anger': 'anger',
    'annoyance': 'anger',
    'approval': 'joy',
    'caring': 'love',
    'confusion': 'surprise',
    'curiosity': 'surprise',
    'desire': 'love',
    'disappointment': 'sadness',
    'disapproval': 'anger',
    'disgust': 'anger',
    'excitement': 'joy',
    'fear': 'fear',
    'gratitude': 'joy',
    'grief': 'sadness',
    'joy': 'joy',
    'love': 'love',
    'nervousness': 'fear',
    'optimism': 'joy',
    'pride': 'joy',
    'realization': 'surprise',
    'relief': 'joy',
    'remorse': 'sadness',
    'sadness': 'sadness',
    'surprise': 'surprise',
    'neutral': 'neutral'
}


# Contextual reinforcement keywords for weighted scoring
# Expanded Multilingual Reinforcement Keywords
REINFORCEMENT_KEYWORDS = {
    'joy': [
        'happy', 'joy', 'wonderful', 'beautiful', 'pleasant', 'smiling', 'laughing', 
        'success', 'win', 'won', 'achievement', 'khush', 'sundar', 'sukhad', 'surakshit',
        'jeet', 'safalta', 'aanandi', 'asha', 'prakash', 'peaceful', 'calm', 'safe',
        'shanti', 'shaanti', 'shant', 'acha', 'mazza', 'sakal', 'victory', 'passed', 
        'award', 'graduating', 'maar', 'pyaar', 'prem', 'mitra', 'dost', 'aanand', 'vijay', 'yash',
        # Hindi/Marathi (Unicode)
        '\u0936\u093e\u0902\u0924\u093f', '\u0938\u0941\u0902\u0926\u0930', '\u0938\u0941\u0916\u0926', 
        '\u0938\u0941\u0930\u0915\u094d\u0937\u093f\u0924', '\u091c\u0940\u0924', '\u0938\u092b\u0932\u0924\u093e', 
        '\u092a\u094d\u0930\u0915\u093e\u0936', '\u0906\u0936\u093e', '\u0906\u0928\u0902\u0926\u0940', 
        '\u0936\u093e\u0902\u0924', '\u092f\u0936', '\u0916\u0941\u0936', '\u092a\u094d\u092f\u093e\u0930', 
        '\u092a\u094d\u0930\u0947\u092e', '\u0938\u094d\u0928\u0947\u0939', '\u0926\u094b\u0938\u094d\u0924', 
        '\u092e\u093f\u0924\u094d\u0930', '\u092a\u0930\u093f\u0935\u093e\u0930', '\u0906\u0928\u0902\u0926',
        '\u0935\u093f\u091c\u092f', '\u092f\u0936'
    ],
    'love': [
        'love', 'affection', 'caring', 'together', 'friends', 'family', 'hug', 'kiss',
        'प्यार', 'प्रेम', 'स्नेह', 'दोस्त', 'परिवार', 'pyaar', 'dost', 'mitra', 'priya'
    ],
    'fear': [
        'scary', 'afraid', 'fear', 'dark', 'monster', 'ghost', 'danger', 'threat', 
        'running', 'chased', 'falling', 'lost', 'stunned', 'panic', 'dead', 'death',
        'blood', 'kill', 'attack', 'scream', 'hide', 'trapped', 'nightmare',
        'dar', 'bhaya', 'khatra', 'ghabrat', 'chinta', 'tension', 'bhoot', 'mare',
        'bhoota', 'ghabarat', 'ghabarlo', 'ghabarli', 'ghabarle', 'dhak', 'shinki',
        # Hindi/Marathi (Unicode)
        '\u0921\u0930', '\u092d\u092f', '\u0916\u0924\u0930\u093e', '\u092d\u0942\u0924', 
        '\u092d\u0940\u0924\u0940', '\u091a\u093f\u0902\u0924\u093e', '\u0918\u092c\u0930\u093e\u0939\u091f',
        '\u092e\u0943\u0924\u094d\u092f\u0941', '\u0915\u0942\u0928', '\u0939\u092e\u0932\u093e',
        '\u092d\u0942\u0924\u093e', '\u0918\u092c\u0930\u0932\u094b', '\u0918\u092c\u0930\u0932\u0940'
    ],
    'sadness': [
        'sad', 'crying', 'alone', 'lonely', 'broken', 'lost', 'miss', 'missing',
        'dukh', 'rona', 'akela',
        # Hindi/Marathi (Unicode)
        '\u0930\u094b\u0928\u093e', '\u0926\u0941\u0901\u0916', '\u0905\u0915\u0947\u0932\u093e'
    ]
}


def analyze_emotions(text):
    """
    Analyze emotions in the given text with strict validation rules and weighting.
    """
    if not text or not text.strip():
        return {
            'primary_emotion': 'neutral',
            'emotion_scores': {},
            'confidence': 0.0
        }
    
    classifier = get_emotion_classifier()
    text_lower = text.lower()
    
    # 1. HARD OVERRIDES (STRICT VALIDATION MODE)
    # These rules override transformer output to ensure common dream tropes are never misclassified.
    
    # Fear/Horror Override
    fear_triggers = REINFORCEMENT_KEYWORDS['fear']
    if any(f in text_lower for f in fear_triggers):
        # Additional check for "chase" and "dark" logic
        horror_context = ['dark', 'night', 'chased', 'threat', 'monster', 'ghost']
        if any(h in text_lower for h in horror_context) or sum(1 for f in fear_triggers if f in text_lower) >= 2:
            return {
                'primary_emotion': 'fear',
                'emotion_scores': {'fear': 0.95, 'joy': 0.0, 'neutral': 0.05},
                'confidence': 0.95,
                'override': 'horror_context'
            }

    # Success/Joy Override
    joy_triggers = REINFORCEMENT_KEYWORDS['joy']
    if any(j in text_lower for j in joy_triggers):
        success_context = ['won', 'passed', 'award', 'happy', 'success', 'divine', 'peaceful']
        if any(s in text_lower for s in success_context) or sum(1 for j in joy_triggers if j in text_lower) >= 2:
             # Ensure no horror elements exist before forcing joy
             if not any(f in text_lower for f in fear_triggers[:10]):
                return {
                    'primary_emotion': 'joy',
                    'emotion_scores': {'joy': 0.95, 'fear': 0.0, 'neutral': 0.05},
                    'confidence': 0.95,
                    'override': 'success_context'
                }

    # 2. TRANSFORMER-BASED ANALYSIS (FALLBACK)
    try:
        results = classifier(text)
        
        if results and len(results) > 0:
            raw_scores = {r['label'].lower(): r['score'] for r in results[0]}
            
            # Map raw scores to core sentiments
            core_scores = {
                'joy': 0.0, 'sadness': 0.0, 'anger': 0.0, 
                'fear': 0.0, 'surprise': 0.0, 'love': 0.0, 'neutral': 0.0
            }
            
            for raw_label, score in raw_scores.items():
                core_label = GO_EMOTIONS_MAPPING.get(raw_label, 'neutral')
                core_scores[core_label] = max(core_scores[core_label], score)
            
            # 3. CONTEXT WEIGHTING (Dynamic Scoring)
            context_boosts = {'joy': 0, 'love': 0, 'fear': 0, 'sadness': 0}
            for emo, kw_list in REINFORCEMENT_KEYWORDS.items():
                for kw in kw_list:
                    if kw in text_lower:
                        context_boosts[emo] += 0.2 # Significant boost
            
            # Apply boosts
            for emo, boost in context_boosts.items():
                if emo in core_scores:
                    core_scores[emo] += boost

            # Aggressive Dampening
            if context_boosts['joy'] > 0 or context_boosts['love'] > 0:
                core_scores['fear'] *= 0.1
                core_scores['sadness'] *= 0.2
            
            if context_boosts['fear'] > 0:
                core_scores['joy'] *= 0.1
                core_scores['love'] *= 0.1
                
            # Find the core emotion with the highest score
            primary_label = max(core_scores.items(), key=lambda x: x[1])[0]
            confidence = min(1.0, core_scores[primary_label])
            
            # Final threshold check
            if confidence < 0.25:
                primary_label = 'neutral'
            
            return {
                'primary_emotion': primary_label,
                'emotion_scores': {k: round(v, 4) for k, v in core_scores.items()},
                'confidence': round(confidence, 4)
            }
    except Exception as e:
        print(f"Emotion analysis error: {e}")
    
    return {
        'primary_emotion': 'neutral',
        'emotion_scores': {},
        'confidence': 0.0
    }


# Emotion descriptions for insights
EMOTION_DESCRIPTIONS = {
    'joy': 'happiness, contentment, or positive feelings',
    'sadness': 'grief, disappointment, or melancholy',
    'anger': 'frustration, irritation, or rage',
    'fear': 'anxiety, worry, or terror',
    'surprise': 'unexpected events or revelations',
    'love': 'affection, connection, or caring feelings'
}


def get_emotion_description(emotion):
    """Get a human-readable description of an emotion."""
    return EMOTION_DESCRIPTIONS.get(emotion.lower(), 'mixed or unclear emotions')

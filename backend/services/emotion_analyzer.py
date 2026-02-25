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
REINFORCEMENT_KEYWORDS = {
    'joy': [
        'happy', 'joy', 'wonderful', 'beautiful', 'pleasant', 'smiling', 'laughing', 
        'success', 'win', 'won', 'achievement', 'khush', 'sundar', 'sukhad', 'surakshit',
        'jeet', 'safalta', 'aanandi', 'asha', 'prakash', 'peaceful', 'calm', 'safe',
        '\u0936\u093e\u0902\u0924\u093f', '\u0938\u0941\u0902\u0926\u0930', '\u0938\u0941\u0916\u0926', '\u0938\u0941\u0930\u0915\u094d\u0937\u093f\u0924', '\u091c\u0940\u0924', '\u0938\u092b\u0932\u0924\u093e', '\u092a\u094d\u0930\u0915\u093e\u0936', '\u0906\u0936\u093e',
        '\u0906\u0928\u0902\u0926\u0940', '\u0936\u093e\u0902\u0924', '\u092f\u0936', '\u0916\u0941\u0936', 'shanti', 'shaanti', 'shant', 'acha', 'mazza', 'sakal',
        'victory', 'passed', 'award', 'graduating', 'jeet', 'maar'
    ],
    'love': [
        'love', 'affection', 'caring', 'together', 'friends', 'family', 'hug', 'kiss',
        'प्यार', 'प्रेम', 'स्नेह', 'दोस्त', 'परिवार', 'pyaar', 'dost', 'mitra', 'priya'
    ],
    'fear': [
        'scary', 'afraid', 'fear', 'dark', 'monster', 'ghost', 'danger', 'threat', 
        'running', 'chased', 'falling', 'lost', 'stunned', 'panic', 'डर', 'भय', 'खतरा', 'भूत', 
        'भीती', 'dar', 'bhaya', 'khatra', 'ghabrat', 'चिंता', 'chinta', 'tension'
    ]
}


def analyze_emotions(text):
    """
    Analyze emotions in the given text with context-weighted reinforcement.
    """
    if not text or not text.strip():
        return {
            'primary_emotion': 'neutral',
            'emotion_scores': {},
            'confidence': 0.0
        }
    
    classifier = get_emotion_classifier()
    text_lower = text.lower()
    
    # Truncate text if too long
    max_chars = 500
    if len(text) > max_chars:
        text = text[:max_chars]
    
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
            
            # CONTEXT WEIGHTING
            # 1. Calculate keyword-based boost
            context_boosts = {'joy': 0, 'love': 0, 'fear': 0}
            for emo, kw_list in REINFORCEMENT_KEYWORDS.items():
                for kw in kw_list:
                    if kw in text_lower:
                        context_boosts[emo] += 0.15 # Even more boost
            
            # High-confidence safety markers
            safety_markers = [
                'peace', 'light', 'bright', 'divinity', 'divine', 'divya',
                '\u0936\u093e\u0902\u0924\u093f', '\u092a\u094d\u0930\u0915\u093e\u0936', '\u0906\u0936\u093e', '\u0936\u093e\u0902\u0924', '\u0926\u093f\u0935\u094d\u092f'
            ]
            has_strong_safety = any(m in text_lower for m in safety_markers)
            
            # 2. Apply boosts and aggressive dampening
            core_scores['joy'] += context_boosts['joy']
            core_scores['love'] += context_boosts['love']
            
            # If safe context is present, suppress negative emotions aggressively
            if context_boosts['joy'] >= 0.1 or has_strong_safety:
                core_scores['fear'] *= 0.1
                core_scores['surprise'] *= 0.2
                core_scores['sadness'] *= 0.3
                core_scores['anger'] *= 0.1
                
            # Find the core emotion with the highest score
            primary_label = max(core_scores.items(), key=lambda x: x[1])[0]
            confidence = core_scores[primary_label]
            
            # SPECIAL CASE: Neutral home/house shouldn't boost to joy unless there are other strong markers
            is_house_mention = any(h in text_lower for h in ['home', 'house', 'ghar', '\u0918\u0930'])
            # VERY AGGRESSIVE: If it's a house and joy boost is weak (<0.2), force neutral
            is_lone_house = is_house_mention and context_boosts['joy'] < 0.2 and not has_strong_safety

            if is_lone_house:
                 # Force neutral for literal house dreams
                 primary_label = 'neutral'
                 confidence = max(core_scores.get('neutral', 0.5), 0.5)

            # CONSERVATIVE NEUTRAL BIAS: If joy/love lead is tiny and NO keywords were found, favor neutral
            if primary_label in ['joy', 'love'] and context_boosts[primary_label] == 0 and not has_strong_safety:
                neutral_score = core_scores.get('neutral', 0)
                if confidence - neutral_score < 0.2: 
                    primary_label = 'neutral'
                    confidence = neutral_score

            # Normalize scores back to max 1.0 (clamping)
            for k in core_scores:
                core_scores[k] = min(1.0, core_scores[k])
            
            # CRITICAL OVERRIDE: Safe context MUST NOT be negative or neutral if safety is strong
            neg_or_neutral = ['fear', 'sadness', 'anger', 'surprise', 'neutral']
            if primary_label in neg_or_neutral and (has_strong_safety or context_boosts['joy'] >= 0.2):
                # Ensure we don't override the forced literal neutral from above
                if not is_lone_house:
                    primary_label = 'joy'
                    confidence = max(core_scores['joy'], 0.5)
            
            # Final forced Literal check (Safety Net)
            if is_lone_house:
                primary_label = 'neutral'
            
            # Final threshold check
            if confidence < 0.2:
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

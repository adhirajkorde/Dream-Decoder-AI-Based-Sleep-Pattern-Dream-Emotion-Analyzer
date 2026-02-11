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
        print("🧠 Loading emotion detection model...")
        _emotion_classifier = pipeline(
            "text-classification",
            model=EMOTION_MODEL,
            top_k=None  # Return all emotion scores
        )
        print("✅ Emotion model loaded!")
    return _emotion_classifier


def analyze_emotions(text):
    """
    Analyze emotions in the given text.
    
    Args:
        text: The dream text to analyze
        
    Returns:
        dict with:
            - primary_emotion: The dominant emotion
            - emotion_scores: All emotion scores as a dict
            - confidence: Confidence of primary emotion
    """
    if not text or not text.strip():
        return {
            'primary_emotion': 'neutral',
            'emotion_scores': {},
            'confidence': 0.0
        }
    
    classifier = get_emotion_classifier()
    
    # Truncate text if too long (model has max token limit)
    max_chars = 500
    if len(text) > max_chars:
        text = text[:max_chars]
    
    try:
        results = classifier(text)
        
        # Results come as list of list of dicts
        if results and len(results) > 0:
            emotions = results[0]  # First (and only) batch result
            
            # Convert to dict
            emotion_scores = {e['label'].lower(): round(e['score'], 4) for e in emotions}
            
            # Get primary emotion (highest score)
            primary = max(emotions, key=lambda x: x['score'])
            
            return {
                'primary_emotion': primary['label'].lower(),
                'emotion_scores': emotion_scores,
                'confidence': round(primary['score'], 4)
            }
    except Exception as e:
        print(f"❌ Emotion analysis error: {e}")
    
    return {
        'primary_emotion': 'unknown',
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

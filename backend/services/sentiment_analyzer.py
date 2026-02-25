"""
Dream Decoder - Sentiment Analyzer
Uses HuggingFace transformers for sentiment classification
"""
from backend.config import SENTIMENT_MODEL

# Global model instance (lazy loaded)
_sentiment_classifier = None


def get_sentiment_classifier():
    """Get or initialize the sentiment classifier."""
    global _sentiment_classifier
    if _sentiment_classifier is None:
        from transformers import pipeline
        print("Loading sentiment analysis model...")
        _sentiment_classifier = pipeline(
            "text-classification",
            model=SENTIMENT_MODEL,
            top_k=None
        )
        print("Sentiment model loaded!")
    return _sentiment_classifier


def analyze_sentiment(text):
    """
    Analyze sentiment in the given text.
    
    Args:
        text: The dream text to analyze
        
    Returns:
        dict with:
            - sentiment: 'positive', 'negative', or 'neutral'
            - score: Confidence score (0-1)
    """
    if not text or not text.strip():
        return {
            'sentiment': 'neutral',
            'score': 0.5
        }
    
    classifier = get_sentiment_classifier()
    
    # Truncate text if too long
    max_chars = 500
    if len(text) > max_chars:
        text = text[:max_chars]
    
    try:
        results = classifier(text)
        text_lower = text.lower()
        
        # High-confidence safety markers
        safety_markers = [
            'peace', 'light', 'bright', 'divinity', 'divine', 'divya', '\u0926\u093f\u0935\u094d\u092f',
            'happy', 'wonderful', 'joy', 'beautiful', 'success', 'victory', 'safe',
            'khush', 'aanandi', 'sukhad',
            '\u0936\u093e\u0902\u0924\u093f', '\u092a\u094d\u0930\u0915\u093e\u0936', '\u0906\u0936\u093e', '\u0936\u093e\u0902\u0924'
        ]
        has_strong_safety = any(m in text_lower for m in safety_markers)
        
        if results and len(results) > 0:
            scores = {r['label'].lower(): r['score'] for r in results[0]}
            pos_score = scores.get('positive', 0)
            neg_score = scores.get('negative', 0)
            neutral_model_score = scores.get('neutral', 0)
            
            # If strong safety markers are present, suppress negative score
            if has_strong_safety:
                neg_score *= 0.2
                pos_score = max(pos_score, 0.4)
            
            # Special Case: Literal House dreams shouldn't be positive
            is_house_mention = any(h in text_lower for h in ['home', 'house', 'ghar', '\u0918\u0930'])
            if is_house_mention and not has_strong_safety:
                # Force neutral sentiment for literal house dreams
                sentiment = 'neutral'
                score = 0.5
            else:
                # If model itself is very confident in neutral, or difference is small
                diff = abs(pos_score - neg_score)
                
                # Conservative neutral threshold: if no safety markers, be more literal
                neutral_threshold = 0.1 if has_strong_safety else 0.25
                
                if neutral_model_score > max(pos_score, neg_score) and not has_strong_safety:
                    sentiment = 'neutral'
                    score = neutral_model_score
                elif diff < neutral_threshold:
                    sentiment = 'neutral'
                    score = 1.0 - diff # Measure of how "balanced" it is
                elif pos_score > neg_score:
                    sentiment = 'positive'
                    score = pos_score
                else:
                    sentiment = 'negative'
                    score = neg_score
            
            return {
                'sentiment': sentiment,
                'score': round(score, 4)
            }
    except Exception as e:
        print(f"Sentiment analysis error: {e}")
    
    return {
        'sentiment': 'neutral',
        'score': 0.5
    }


def get_sentiment_emoji(sentiment):
    """Get emoji representation of sentiment."""
    emojis = {
        'positive': '[Positive]',
        'negative': '[Negative]',
        'neutral': '[Neutral]'
    }
    return emojis.get(sentiment, '[Unknown]')

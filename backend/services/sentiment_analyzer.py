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
        print("🧠 Loading sentiment analysis model...")
        _sentiment_classifier = pipeline(
            "sentiment-analysis",
            model=SENTIMENT_MODEL
        )
        print("✅ Sentiment model loaded!")
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
        
        if results and len(results) > 0:
            result = results[0]
            label = result['label'].lower()
            score = result['score']
            
            # Map model labels to our standard labels
            if label == 'positive':
                sentiment = 'positive'
            elif label == 'negative':
                sentiment = 'negative'
            else:
                sentiment = 'neutral'
            
            # If confidence is low, consider it neutral
            if score < 0.6:
                sentiment = 'neutral'
            
            return {
                'sentiment': sentiment,
                'score': round(score, 4)
            }
    except Exception as e:
        print(f"❌ Sentiment analysis error: {e}")
    
    return {
        'sentiment': 'neutral',
        'score': 0.5
    }


def get_sentiment_emoji(sentiment):
    """Get emoji representation of sentiment."""
    emojis = {
        'positive': '😊',
        'negative': '😔',
        'neutral': '😐'
    }
    return emojis.get(sentiment, '❓')

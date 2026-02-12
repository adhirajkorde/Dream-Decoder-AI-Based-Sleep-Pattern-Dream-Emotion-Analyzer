"""
Dream Decoder - NLP Engine
Main orchestrator for all NLP analysis
"""
try:
    from backend.services.emotion_analyzer import analyze_emotions, get_emotion_description
    from backend.services.sentiment_analyzer import analyze_sentiment, get_sentiment_emoji
    from backend.services.keyword_extractor import extract_keywords, extract_entities, categorize_dream_theme
except ImportError as e:
    print(f"CRITICAL ERROR: Failed to import NLP services. {e}")
    print("This usually means dependencies are not installed correctly.")
    print("Please run 'setup.bat' to fix the virtual environment.")
    # Define placeholder functions to avoid NameError if imports fail
    def _error_handler(*args, **kwargs):
        raise RuntimeError(f"NLP Engine is not available because of missing dependencies: {e}")
    analyze_emotions = analyze_sentiment = extract_keywords = extract_entities = categorize_dream_theme = _error_handler
    get_emotion_description = get_sentiment_emoji = lambda *args: "Unknown"


def analyze_dream(text):
    """
    Perform complete NLP analysis on dream text.
    
    Args:
        text: The dream description text
        
    Returns:
        dict containing all analysis results:
            - sentiment: positive/negative/neutral
            - sentiment_score: confidence 0-1
            - primary_emotion: dominant emotion
            - emotion_scores: all emotion scores
            - keywords: list of extracted keywords
            - entities: list of named entities
            - themes: categorized dream themes
    """
    if not text or not text.strip():
        return {
            'sentiment': 'neutral',
            'sentiment_score': 0.5,
            'primary_emotion': 'neutral',
            'emotion_scores': {},
            'keywords': [],
            'entities': [],
            'themes': ['general'],
            'summary': 'No dream content to analyze.'
        }
    
    # Run all analyses
    emotion_result = analyze_emotions(text)
    sentiment_result = analyze_sentiment(text)
    keywords = extract_keywords(text)
    entities = extract_entities(text)
    themes = categorize_dream_theme(keywords)
    
    # 3. Add Psychological Interpretation (New)
    from backend.services.dream_interpreter import interpret_dream
    interpretation = interpret_dream(text, {
        'keywords': keywords,
        'entities': entities,
        'emotion': emotion_result,
        'sentiment': sentiment_result
    })
    
    # Generate a brief summary
    emoji = get_sentiment_emoji(sentiment_result['sentiment'])
    emotion_desc = get_emotion_description(emotion_result['primary_emotion'])
    
    summary = f"{emoji} This dream has a {sentiment_result['sentiment']} tone, "
    summary += f"with primary feelings of {emotion_result['primary_emotion']} ({emotion_desc}). "
    
    if keywords:
        summary += f"Key themes include: {', '.join(keywords[:5])}."
    
    return {
        'sentiment': sentiment_result['sentiment'],
        'sentiment_score': sentiment_result['score'],
        'primary_emotion': emotion_result['primary_emotion'],
        'emotion_scores': emotion_result['emotion_scores'],
        'emotion_confidence': emotion_result['confidence'],
        'keywords': keywords,
        'entities': entities,
        'themes': themes,
        'summary': summary,
        'interpretation': interpretation # Added interpretation field
    }


def preload_models():
    """
    Preload all NLP models to avoid first-request delay.
    Call this on application startup.
    """
    print("=" * 50)
    print("Preloading NLP models...")
    print("=" * 50)
    
    # Load each model by calling its getter
    from backend.services.emotion_analyzer import get_emotion_classifier
    from backend.services.sentiment_analyzer import get_sentiment_classifier
    from backend.services.keyword_extractor import get_nlp
    
    get_emotion_classifier()
    get_sentiment_classifier()
    get_nlp()
    
    print("=" * 50)
    print("All models loaded and ready!")
    print("=" * 50)

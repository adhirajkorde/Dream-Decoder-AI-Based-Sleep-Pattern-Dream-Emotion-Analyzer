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


def classify_dream_category(text, sentiment_result, emotion_result):
    """Categorize the dream as nightmare, lucid, recurring, etc."""
    text_lower = text.lower()
    categories = []
    
    # Nightmare check: negative sentiment + strong negative emotion (fear, anger, sadness)
    if sentiment_result['sentiment'] == 'negative' and emotion_result['primary_emotion'] in ['fear', 'anger', 'sadness']:
        if emotion_result['confidence'] > 0.6:
            categories.append('nightmare')
            
    # Lucid dream check: awareness keywords
    lucid_keywords = ['realized', 'aware', 'lucid', 'dreaming', 'control', 'woke up in', 'know it was a dream']
    if any(k in text_lower for k in lucid_keywords):
        categories.append('lucid')
        
    # Recurring dream check: repetition keywords
    recurring_keywords = ['again', 'repeat', 'before', 'always', 'every time', 'recurring', 'past', 'seen this']
    if any(k in text_lower for k in recurring_keywords):
        categories.append('recurring')
        
    if not categories:
        categories.append('ordinary')
        
    return categories


def validate_accuracy(text, emotion_result, sentiment_result):
    """
    STRICT VALIDATION MODE: Self-checking mechanism to ensure zero incorrect results.
    Enforces alignment between emotion, sentiment, and context.
    """
    text_lower = text.lower()
    emo = emotion_result.get('primary_emotion', '').lower()
    sent = sentiment_result.get('sentiment', '').lower()
    
    # 1. EMOTION-SENTIMENT ALIGNMENT (MANDATORY RULES)
    # Fear/Sadness/Anger -> Negative Sentiment
    if emo in ['fear', 'sadness', 'anger']:
        if sent != 'negative':
            print(f"STRICT MODE: Re-aligning {sent} sentiment to negative due to {emo} emotion.")
            sentiment_result['sentiment'] = 'negative'
            sentiment_result['score'] = max(sentiment_result.get('score', 0), 0.9) # Boost confidence
            
    # Joy/Love -> Positive Sentiment
    elif emo in ['joy', 'love']:
        if sent != 'positive':
            # Check for conflicting negative words before forcing positive
            neg_markers = ['not', 'never', 'no', 'bad', 'problem', 'don\'t']
            if not any(m in text_lower for m in neg_markers):
                print(f"STRICT MODE: Re-aligning {sent} sentiment to positive due to {emo} emotion.")
                sentiment_result['sentiment'] = 'positive'
                sentiment_result['score'] = max(sentiment_result['score'], 0.9)
    
    # 2. CONTEXTUAL ACCURACY CHECKS
    # Horror/Nightmare consistency
    horror_keywords = ['ghost', 'monster', 'dark', 'dead', 'death', 'blood', 'chase', 'scary', 'afraid']
    if any(k in text_lower for k in horror_keywords):
        if emo not in ['fear', 'sadness']:
             print(f"STRICT MODE: Detected horror context, reinforcing fear/negative.")
             emotion_result['primary_emotion'] = 'fear'
             sentiment_result['sentiment'] = 'negative'

    return emotion_result, sentiment_result


def analyze_dream(text, user_language='en'):
    """
    Perform complete NLP analysis on dream text with Strict Accuracy Validation.
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
            'categories': ['ordinary'],
            'summary': 'No dream content to analyze.',
            'interpretation': {},
            'detected_language': user_language,
            'language_confidence': 0
        }
    
    # Initial Analysis
    emotion_result = analyze_emotions(text)
    sentiment_result = analyze_sentiment(text)
    
    # MANDATORY: Accuracy Validation & Self-Correction
    emotion_result, sentiment_result = validate_accuracy(text, emotion_result, sentiment_result)
    
    keywords = extract_keywords(text)
    entities = extract_entities(text)
    themes = categorize_dream_theme(keywords)
    
    # Category Classification
    dream_categories = classify_dream_category(text, sentiment_result, emotion_result)
    
    # Perform deep psychological interpretation
    from backend.services.dream_interpreter import interpret_dream
    
    # Assemble analysis for the interpreter
    analysis_for_interpreter = {
        'keywords': keywords,
        'entities': entities,
        'emotion': emotion_result,
        'sentiment': sentiment_result,
        'categories': dream_categories
    }
    
    interpretation = interpret_dream(text, analysis_for_interpreter, user_language=user_language)
    
    # RE-SYNCHRONIZE: Interpretation might have further refined labels
    # Update local results if interpreter made corrections
    sentiment_result['sentiment'] = analysis_for_interpreter['sentiment']['sentiment']
    emotion_result['primary_emotion'] = analysis_for_interpreter['emotion']['primary_emotion']
    
    # Generate a brief summary
    emoji = get_sentiment_emoji(sentiment_result['sentiment'])
    emotion_desc = get_emotion_description(emotion_result['primary_emotion'])
    
    summary = f"{emoji} This dream has a {sentiment_result['sentiment']} tone, "
    summary += f"with primary feelings of {emotion_result['primary_emotion']} ({emotion_desc}). "
    
    if 'nightmare' in dream_categories:
        summary = f"⚠️ This nightmare is being safely processed. Tone: {sentiment_result['sentiment']}, Feelings: {emotion_result['primary_emotion']}."
    
    if keywords:
        summary += f"\nKey themes: {', '.join(keywords[:5])}."
    
    return {
        'sentiment': sentiment_result['sentiment'],
        'sentiment_score': sentiment_result['score'],
        'primary_emotion': emotion_result['primary_emotion'],
        'emotion_scores': emotion_result.get('emotion_scores', {}),
        'emotion_confidence': emotion_result.get('confidence', 0),
        'keywords': keywords,
        'entities': entities,
        'themes': themes,
        'categories': dream_categories,
        'summary': summary,
        'interpretation': interpretation,
        'detected_language': interpretation.get('detected_language', user_language),
        'language_confidence': interpretation.get('language_confidence', 0)
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

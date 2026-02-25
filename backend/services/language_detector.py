"""
Dream Decoder - Language Detection Service
Detects language of dream text and provides translation utilities
"""
from langdetect import detect, detect_langs, LangDetectException


# Language code mappings
SUPPORTED_LANGUAGES = {
    'en': 'English',
    'hi': 'Hindi',
    'mr': 'Marathi',
    'hinglish': 'Hinglish'  # Special case - mix of Hindi and English
}

# Language detection confidence threshold
CONFIDENCE_THRESHOLD = 0.7


def detect_language(text):
    """
    Detect the language of the input text.
    Returns language code ('en', 'hi', 'mr', 'hinglish') and confidence.
    """
    if not text or not text.strip():
        return 'en', 0.0
    
    try:
        # Get language probabilities
        langs = detect_langs(text)
        
        # Check for Hinglish (mix of English and Hindi)
        has_english = any(lang.lang == 'en' for lang in langs)
        has_hindi = any(lang.lang == 'hi' for lang in langs)
        
        # If both English and Hindi are detected with reasonable confidence, it's Hinglish
        if has_english and has_hindi:
            en_prob = next((lang.prob for lang in langs if lang.lang == 'en'), 0)
            hi_prob = next((lang.prob for lang in langs if lang.lang == 'hi'), 0)
            
            # If both have significant presence, classify as Hinglish
            if en_prob > 0.2 and hi_prob > 0.2:
                return 'hinglish', min(en_prob + hi_prob, 1.0)
        
        # Get the most probable language
        primary_lang = langs[0]
        
        # Map to supported languages
        if primary_lang.lang == 'en':
            return 'en', primary_lang.prob
        elif primary_lang.lang == 'hi':
            return 'hi', primary_lang.prob
        elif primary_lang.lang == 'mr':
            return 'mr', primary_lang.prob
        else:
            # Default to English for unsupported languages
            return 'en', 0.5
            
    except LangDetectException as e:
        print(f"Language detection error: {e}")
        return 'en', 0.0


def is_hinglish(text):
    """
    Check if text is Hinglish (mix of Hindi and English).
    """
    if not text:
        return False
    
    # Simple heuristic: check for both Latin and Devanagari scripts
    has_latin = any('\u0041' <= c <= '\u007A' or '\u0041' <= c <= '\u005A' for c in text)
    has_devanagari = any('\u0900' <= c <= '\u097F' for c in text)
    
    return has_latin and has_devanagari


def get_language_name(lang_code):
    """Get human-readable language name from code."""
    return SUPPORTED_LANGUAGES.get(lang_code, 'English')


def normalize_language_code(lang_code):
    """
    Normalize language code to supported format.
    """
    if not lang_code:
        return 'en'
    
    lang_code = lang_code.lower().strip()
    
    if lang_code in SUPPORTED_LANGUAGES:
        return lang_code
    
    # Handle variations
    if lang_code in ['eng', 'english']:
        return 'en'
    elif lang_code in ['hin', 'hindi']:
        return 'hi'
    elif lang_code in ['mar', 'marathi']:
        return 'mr'
    
    return 'en'  # Default to English


def detect_with_fallback(text, user_preference='en'):
    """
    Detect language with fallback to user preference.
    Returns (detected_lang, confidence, used_fallback)
    """
    detected_lang, confidence = detect_language(text)
    
    # If confidence is low, use user preference
    if confidence < CONFIDENCE_THRESHOLD:
        return user_preference, confidence, True
    
    return detected_lang, confidence, False

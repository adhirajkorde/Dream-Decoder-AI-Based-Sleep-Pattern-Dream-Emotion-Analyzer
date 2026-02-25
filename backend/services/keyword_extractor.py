"""
Dream Decoder - Keyword Extractor
Uses SpaCy for entity recognition and keyword extraction
"""
import sys
from backend.config import SPACY_MODEL, DREAM_THEMES

# Global model instance (lazy loaded)
_nlp = None


def get_nlp():
    """Get or initialize the SpaCy NLP model."""
    global _nlp
    if _nlp is None:
        import spacy
        print("Loading SpaCy language model...")
        try:
            _nlp = spacy.load(SPACY_MODEL)
            print("SpaCy model loaded!")
        except Exception:
            print(f"SpaCy model '{SPACY_MODEL}' not found. Attempting download...")
            try:
                import subprocess
                # Use current executable to ensure we use the venv
                subprocess.run([sys.executable, '-m', 'spacy', 'download', SPACY_MODEL], check=True)
                _nlp = spacy.load(SPACY_MODEL)
                print("SpaCy model downloaded and loaded!")
            except Exception as e:
                print(f"Failed to download SpaCy model: {e}")
                # Fallback to basic tokenizer if model fails
                print("Falling back to basic tokenization...")
                from spacy.lang.en import English
                _nlp = English()
    return _nlp


def extract_keywords(text):
    """
    Extract keywords and themes from dream text with improved phrase detection.
    
    Args:
        text: The dream text to analyze
        
    Returns:
        list of keywords/themes found
    """
    if not text or not text.strip():
        return []
    
    text_lower = text.lower()
    keywords_seen = set()
    final_keywords = []
    
    # Use SpaCy for intelligent keyword extraction
    nlp = get_nlp()
    doc = nlp(text)
    
    # 1. Check for common dream themes (defined in config)
    for theme in DREAM_THEMES:
        if theme in text_lower:
            if theme not in keywords_seen:
                keywords_seen.add(theme)
                final_keywords.append(theme)
    
    # 2. Extract noun chunks (key phrases) - IMPROVED
    # This handles "flying car", "dark forest", etc.
    for chunk in doc.noun_chunks:
        # Filter out stopwords within chunks and normalize
        chunk_words = [token.lemma_.lower() for token in chunk if not token.is_stop and len(token.text) > 1]
        if not chunk_words:
            continue
            
        chunk_text = " ".join(chunk_words)
        
        # Filter out very short or very long chunks
        if 2 <= len(chunk_text) <= 50:
            # Skip common uninteresting words and dream fillers
            skip_words = {
                'i', 'me', 'my', 'we', 'it', 'the', 'a', 'an', 'this', 'that', 'were', 'was',
                'dream', 'night', 'felt', 'thought', 'think', 'saw', 'see', 'going', 'went',
                'something', 'someone', 'everything', 'everyone', 'anything', 'around', 'back',
                'happened', 'looking', 'seemed', 'actually', 'really', 'started', 'could', 'would',
                'many', 'much', 'some', 'few', 'very', 'like', 'every', 'each', 'other', 'another'
            }
            if chunk_text not in skip_words and chunk_text not in keywords_seen:
                keywords_seen.add(chunk_text)
                final_keywords.append(chunk_text)
    
    # 3. Extract important nouns, verbs, and adjectives (Selective POS Filtering)
    for token in doc:
        # Only process if not already seen as part of a phrase or theme
        if token.is_stop or token.is_punct or token.is_space:
            continue
            
        # Prioritize Nouns, Proper Nouns, and Actions (Verbs)
        if token.pos_ in ['NOUN', 'PROPN', 'VERB', 'ADJ']:
            lemma = token.lemma_.lower()
            
            # Avoid single-character or very common dream fillers
            generic_fillers = {'get', 'take', 'make', 'come', 'go', 'see', 'look', 'know', 'think', 'feel'}
            
            if len(lemma) > 2 and lemma not in keywords_seen and lemma not in generic_fillers:
                keywords_seen.add(lemma)
                final_keywords.append(lemma)
    
    return final_keywords[:20]  # Limit to 20 keywords



def extract_entities(text):
    """
    Extract named entities from dream text.
    
    Args:
        text: The dream text to analyze
        
    Returns:
        list of dicts with entity text and label
    """
    if not text or not text.strip():
        return []
    
    nlp = get_nlp()
    doc = nlp(text)
    
    entities = []
    seen = set()
    
    for ent in doc.ents:
        # Avoid duplicates
        key = (ent.text.lower(), ent.label_)
        if key not in seen:
            seen.add(key)
            entities.append({
                'text': ent.text,
                'label': ent.label_,
                'description': get_entity_description(ent.label_)
            })
    
    return entities


def get_entity_description(label):
    """Get human-readable description of entity type."""
    descriptions = {
        'PERSON': 'Person',
        'NORP': 'Group/Nationality',
        'FAC': 'Building/Structure',
        'ORG': 'Organization',
        'GPE': 'Location/Place',
        'LOC': 'Location',
        'PRODUCT': 'Object/Product',
        'EVENT': 'Event',
        'DATE': 'Date/Time',
        'TIME': 'Time',
        'MONEY': 'Money',
        'QUANTITY': 'Quantity',
        'CARDINAL': 'Number'
    }
    return descriptions.get(label, 'Entity')


def categorize_dream_theme(keywords):
    """
    Categorize the dream based on detected keywords.
    
    Args:
        keywords: List of extracted keywords
        
    Returns:
        list of dream theme categories
    """
    categories = []
    keywords_set = set(k.lower() for k in keywords)
    
    theme_mapping = {
        'anxiety': ['falling', 'chased', 'chasing', 'running', 'trapped', 'lost', 'late', 'exam', 'test'],
        'freedom': ['flying', 'floating', 'free', 'sky', 'soaring'],
        'vulnerability': ['naked', 'exposed', 'teeth', 'losing'],
        'transformation': ['death', 'dying', 'born', 'baby', 'change'],
        'exploration': ['house', 'room', 'door', 'stairs', 'searching', 'found'],
        'travel': ['car', 'driving', 'road', 'journey', 'airplane'],
        'relationships': ['family', 'friend', 'mother', 'father', 'love', 'stranger'],
        'nature': ['water', 'ocean', 'drowning', 'animal', 'forest', 'mountain'],
        'conflict': ['monster', 'fight', 'war', 'weapon', 'attack'],
        'supernatural': ['ghost', 'demon', 'magic', 'flying', 'powers']
    }
    
    for category, theme_keywords in theme_mapping.items():
        if any(kw in keywords_set for kw in theme_keywords):
            categories.append(category)
    
    return categories if categories else ['general']

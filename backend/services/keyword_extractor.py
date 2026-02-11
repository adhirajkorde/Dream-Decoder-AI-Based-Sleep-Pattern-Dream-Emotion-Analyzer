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
        print("🧠 Loading SpaCy language model...")
        try:
            _nlp = spacy.load(SPACY_MODEL)
            print("✅ SpaCy model loaded!")
        except Exception:
            print(f"⚠️ SpaCy model '{SPACY_MODEL}' not found. Attempting download...")
            try:
                import subprocess
                # Use current executable to ensure we use the venv
                subprocess.run([sys.executable, '-m', 'spacy', 'download', SPACY_MODEL], check=True)
                _nlp = spacy.load(SPACY_MODEL)
                print("✅ SpaCy model downloaded and loaded!")
            except Exception as e:
                print(f"❌ Failed to download SpaCy model: {e}")
                # Fallback to basic tokenizer if model fails
                print("⚠️ Falling back to basic tokenization...")
                from spacy.lang.en import English
                _nlp = English()
    return _nlp


def extract_keywords(text):
    """
    Extract keywords and themes from dream text.
    
    Args:
        text: The dream text to analyze
        
    Returns:
        list of keywords/themes found
    """
    if not text or not text.strip():
        return []
    
    text_lower = text.lower()
    keywords = set()
    
    # Check for common dream themes
    for theme in DREAM_THEMES:
        if theme in text_lower:
            keywords.add(theme)
    
    # Use SpaCy for additional keyword extraction
    nlp = get_nlp()
    doc = nlp(text)
    
    # Extract noun chunks (key phrases)
    for chunk in doc.noun_chunks:
        # Filter out very short or very long chunks
        chunk_text = chunk.text.lower().strip()
        if 2 <= len(chunk_text) <= 30:
            # Skip common uninteresting words
            skip_words = {'i', 'me', 'my', 'we', 'it', 'the', 'a', 'an', 'this', 'that'}
            if chunk_text not in skip_words:
                keywords.add(chunk_text)
    
    # Extract important nouns and verbs
    for token in doc:
        if token.pos_ in ['NOUN', 'VERB'] and not token.is_stop:
            if len(token.text) > 2:
                keywords.add(token.lemma_.lower())
    
    return list(keywords)[:20]  # Limit to 20 keywords


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

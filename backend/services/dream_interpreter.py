"""
Dream Decoder - Multilingual Dream Interpreter Service
Provides deep psychological and symbolic analysis of dream content in multiple languages.
"""
import re
from backend.services.language_detector import detect_with_fallback
from backend.services.dream_symbols import find_symbols_in_text
from backend.services.translations import get_interpretation_template


# Multilingual interpretation templates
INTERPRETATION_TEMPLATES = {
    'en': {
        'intro': "Your dream weaves together symbols of {symbols} with a strong {emotion} emotional undercurrent.",
        'mid_positive': "The interaction of these elements reflects a positive emotional state in your dream.",
        'mid_negative': "The interaction of these elements reflects an area of emotional challenge in your dream.",
        'mid_neutral': "The interaction of these elements suggests a period of observation and balance.",
        'closing': "Your subconscious highlights these specific details to help you process your experiences.",
        'no_elements': "This dream reflects your current mental state, primarily characterized by a {emotion} tone.",
        'insight_fear': "Your mind is safely processing these anxieties while you sleep. You have the strength to navigate these feelings.",
        'insight_joy': "Your subconscious is capturing a moment of positivity. Carry this energy with you.",
        'insight_sadness': "Allow yourself to process these emotions. This dream is a step toward emotional clarity.",
        'insight_default': "Reflect on these symbols as they appear in your dream. Your inner mind is processing your daily experiences."
    },
    'hi': {
        'intro': "आपका स्वप्न {symbols} के प्रतीकों को एक मजबूत {emotion} भावनात्मक धारा के साथ बुनता है।",
        'mid_positive': "इन तत्वों की परस्पर क्रिया आपके सपने में एक सकारात्मक भावनात्मक स्थिति को दर्शाती है।",
        'mid_negative': "इन तत्वों की परस्पर क्रिया आपके सपने में भावनात्मक चुनौती के क्षेत्र को दर्शाती है।",
        'mid_neutral': "इन तत्वों की परस्पर क्रिया अवलोकन और संतुलन की अवधि का सुझाव देती है।",
        'closing': "आपका अवचेतन आपके अनुभवों को संसाधित करने में मदद करने के लिए इन विशिष्ट विवरणों को उजागर करता है।",
        'no_elements': "यह सपना आपकी वर्तमान मानसिक स्थिति को दर्शाता है, जो मुख्य रूप से {emotion} स्वर द्वारा विशेषता है।",
        'insight_fear': "जब आप सोते हैं तो आपका मन इन चिंताओं को सुरक्षित रूप से संसाधित कर रहा होता है। आपके पास इन भावनाओं को नेविगेट करने की ताकत है।",
        'insight_joy': "आपका अवचेतन सकारात्मकता के क्षण को कैद कर रहा है। इस ऊर्जा को अपने साथ रखें।",
        'insight_sadness': "स्वयं को इन भावनाओं को संसाधित करने दें। यह सपना भावनात्मक स्पष्टता की दिशा में एक कदम है।",
        'insight_default': "इन प्रतीकों पर विचार करें जैसे वे आपके सपने में दिखाई देते हैं। आपका आंतरिक मन आपके दैनिक अनुभवों को संसाधित कर रहा है।"
    },
    'mr': {
        'intro': "तुमचे स्वप्न {symbols} च्या प्रतीकांना एका मजबूत {emotion} भावनिक प्रवाहासह विणते.",
        'mid_positive': "या घटकांचा परस्परसंवाद तुमच्या स्वप्नातील सकारात्मक भावनिक स्थिती दर्शवतो.",
        'mid_negative': "या घटकांचा परस्परसंवाद तुमच्या स्वप्नातील भावनिक आव्हानाचे क्षेत्र दर्शवतो.",
        'mid_neutral': "या घटकांचा परस्परसंवाद निरीक्षण आणि संतुलनाचा काळ सूचित करतो.",
        'closing': "तुमचे अवचेतन तुमचे अनुभव प्रक्रिया करण्यासाठी हे विशिष्ट तपशील हायलाइट करते.",
        'no_elements': "हे स्वप्न तुमच्या सध्याच्या मानसिक स्थितीचे प्रतिबिंब आहे, जे प्रामुख्याने {emotion} स्वराद्वारे वैशिष्ट्यीकृत आहे.",
        'insight_fear': "तुम्ही झोपलेले असताना तुमचे मन या चिंतांवर सुरक्षितपणे प्रक्रिया करत आहे. या भावनांना सामोरे जाण्याची ताकद तुमच्यात आहे.",
        'insight_joy': "तुमचे अवचेतन सकारात्मकतेचा एक क्षण कॅप्चर करत आहे. ही ऊर्जा तुमच्यासोबत ठेवा.",
        'insight_sadness': "स्वत स्वतःला या भावनांवर प्रक्रिया करण्याची परवानगी द्या. हे स्वप्न भावनिक स्पष्टतेच्या दिशेने एक पाऊल आहे.",
        'insight_default': "तुमच्या स्वप्नात दिसणाऱ्या या प्रतीकांवर विचार करा. तुमचे आंतरिक मन तुमच्या दैनंदिन अनुभवांवर प्रक्रिया करत आहे."
    },
    'hinglish': {
        'intro': "Aapka dream {symbols} ke symbols ko ek strong {emotion} emotional undercurrent ke saath weave karta hai.",
        'mid_positive': "In elements ki interaction aapke dream mein ek positive emotional state ko reflect karti hai.",
        'mid_negative': "In elements ki interaction aapke dream mein emotional challenge ke area ko reflect karti hai.",
        'mid_neutral': "In elements ki interaction observation aur balance ka phase suggest karti hai.",
        'closing': "Aapka subconscious aapke experiences ko process karne mein help karne ke liye in specific details ko highlight kar raha hai.",
        'no_elements': "Ye dream aapki current mental state ka reflection hai, jo primarily {emotion} tone se characterized hai.",
        'insight_fear': "Aapka mind sote waqt in anxieties ko safely process kar raha hai. Aapke paas in feelings ko navigate karne ki strength hai.",
        'insight_joy': "Aapka subconscious positivity ke ek moment ko capture kar raha hai. Is energy ko apne saath rakho.",
        'insight_sadness': "Apne aap ko in emotions ko process karne ki ijazat do. Ye dream emotional clarity ki direction mein ek step hai.",
        'insight_default': "In symbols par reflect karo jaise ye aapke dream mein appear hote hain. Aapka inner mind aapke daily experiences ko process kar raha hai."
    }
}


# Emotion categories
POSITIVE_EMOTIONS = {'joy', 'love', 'surprise'}
NEGATIVE_EMOTIONS = {'fear', 'sadness', 'anger'}
FEAR_THEMES = {'fear', 'anxiety', 'chase', 'falling', 'flood', 'spider', 'snake', 'darkness', 'exam', 'teeth_falling', 'late'}

def interpret_dream(text, nlp_analysis, user_language='en'):
    """
    Generate a structured psychological interpretation with consistency checks.
    """
    # Detect language with fallback to user preference
    detected_lang, lang_conf, used_fallback = detect_with_fallback(text, user_language)
    interpretation_lang = detected_lang
    
    # Find symbols in the dream text
    found_symbols = find_symbols_in_text(text, interpretation_lang)
    
    # 0. Consistency & Polarity Reinforcement
    emo_data = nlp_analysis.get('emotion', {})
    primary_emotion = emo_data.get('primary_emotion', 'neutral')
    emo_confidence = emo_data.get('confidence', 0)
    
    sentiment_data = nlp_analysis.get('sentiment', {})
    sentiment_label = sentiment_data.get('sentiment')
    sent_confidence = sentiment_data.get('score', 0)
    
    # Calculate symbol-based counts and polarity
    symbol_score = 0
    symbol_emotions = {}
    for s in found_symbols:
        symbol_score += s.get('polarity', 0) * s.get('weight', 1)
        s_emo = s.get('emotion', 'neutral')
        symbol_emotions[s_emo] = symbol_emotions.get(s_emo, 0) + s.get('weight', 1)

    # HOUSE GUARD: Protection for literal dreams
    is_house_mention = any(h in text.lower() for h in ['home', 'house', 'ghar', '\u0918\u0930'])
    is_lone_house = is_house_mention and symbol_score < 0.5
    
    # EMOTION REINFORCEMENT
    final_emotion = primary_emotion
    if emo_confidence < 0.4 or primary_emotion == 'neutral' or (symbol_emotions.get(primary_emotion, 0) == 0 and symbol_emotions):
        if symbol_emotions and not is_lone_house:
            best_symbol_emo = max(symbol_emotions.items(), key=lambda x: x[1])[0]
            if best_symbol_emo != 'neutral' and symbol_emotions[best_symbol_emo] >= 2:
                final_emotion = best_symbol_emo

    # SENTIMENT REINFORCEMENT (The "Voting" System)
    final_sentiment = sentiment_label
    
    if not is_lone_house:
        # Rule 1: Joy/Love are powerful indicators. Force positive unless model is 98%+ sure of negative.
        if final_emotion in POSITIVE_EMOTIONS and final_sentiment != 'positive':
            if symbol_score >= -1 or sent_confidence < 0.98:
                final_sentiment = 'positive'

        # Rule 2: Symbols represent the core subconscious content. 
        # Strong positive symbols override Model's negative/neutral findings.
        if symbol_score >= 1.5 and final_sentiment != 'positive':
            if sent_confidence < 0.95:
                final_sentiment = 'positive'
        
        # Rule 3: Scary/Negative symbols are critical warnings. 
        # Override positive/neutral if any strong negative symbols are present.
        if symbol_score <= -1.5 and final_sentiment != 'negative':
            if sent_confidence < 0.95:
                final_sentiment = 'negative'
    
    # Rule 4: Handle "Neutral" correctly
    # If the transformer is low/mid confidence and primary emotion is neutral, force neutral
    if final_emotion == 'neutral' and final_sentiment != 'neutral':
        if sent_confidence < 0.85 and abs(symbol_score) < 1.0:
            final_sentiment = 'neutral'
            
    # Lone House Final Force
    if is_lone_house and abs(symbol_score) < 0.5:
        final_emotion = 'neutral'
        final_sentiment = 'neutral'
    
    # IMPORTANT: Update nlp_analysis in-place so nlp_engine returns reinforced labels
    emo_data['primary_emotion'] = final_emotion
    nlp_analysis['emotion'] = emo_data
    sentiment_data['sentiment'] = final_sentiment
    nlp_analysis['sentiment'] = sentiment_data
            
    # STRICT SYMBOL VERIFICATION (STRICT MODE)
    # Remove any symbol that is not explicitly found as a keyword (substring) in the original text
    original_text_lower = text.lower()
    verified_symbols = []
    for s in found_symbols:
        keyword = s['keyword'].lower()
        # Verify if the literal keyword or its lemma exists in the text
        if keyword in original_text_lower:
            verified_symbols.append(s)
    
    found_symbols = verified_symbols
    
    # Sort by weight
    found_symbols.sort(key=lambda x: (x.get('weight', 1), len(x['keyword'])), reverse=True)
    
    # Extract elements from NLP analysis
    keywords = nlp_analysis.get('keywords', [])
    
    # Build numbered elements
    numbered_elements = []
    for i, symbol_data in enumerate(found_symbols[:5], 1):
        numbered_elements.append({
            'number': i,
            'element': symbol_data['keyword'].capitalize(),
            'symbolic_meaning': symbol_data['meaning'],
            'subconscious_insight': symbol_data['interpretation'],
            'weight': symbol_data.get('weight', 1),
            'emotion': symbol_data.get('emotion', 'neutral')
        })
    
    # Generic element fallback (Only if NO verified symbols are found)
    if not numbered_elements and keywords:
        for i, keyword in enumerate(keywords[:3], 1):
            # Only include keywords that actually exist in the text
            if keyword.lower() in original_text_lower:
                numbered_elements.append({
                    'number': i,
                    'element': keyword.capitalize(),
                    'symbolic_meaning': _get_generic_meaning(interpretation_lang),
                    'subconscious_insight': _get_generic_insight(interpretation_lang),
                    'weight': 1,
                    'emotion': 'neutral'
                })
    
    overall_interpretation = _generate_overall_interpretation(
        numbered_elements, final_emotion, final_sentiment, keywords, interpretation_lang
    )
    
    # Generate final insight
    final_insight = _generate_final_insight(final_emotion, interpretation_lang)
    
    return {
        'numbered_elements': numbered_elements,
        'overall_interpretation': overall_interpretation,
        'final_insight': final_insight,
        'detected_language': detected_lang,
        'language_confidence': lang_conf,
        'interpretation_language': interpretation_lang
    }


def _get_generic_meaning(lang_code):
    """Get professional generic meaning for non-symbol keywords."""
    meanings = {
        'en': "This element represents a focal point of your subconscious attention, acting as a bridge between your internal thoughts and outward reality.",
        'hi': "यह तत्व आपके अवचेतन ध्यान के एक केंद्र बिंदु का प्रतिनिधित्व करता है, जो आपके आंतरिक विचारों और बाहरी वास्तविकता के बीच एक सेतु के रूप में कार्य करता है।",
        'mr': "हा घटक तुमच्या सुप्त मनाच्या एका केंद्रबिंदूचे प्रतिनिधित्व करतो, जो तुमच्या अंतर्गत विचारांना आणि बाह्य वास्तवाला जोडणारा दुवा म्हणून काम करतो.",
        'hinglish': "Ye element aapke subconscious dhyan ka ek focal point represent karta hai, jo aapke internal thoughts aur reality ke beech ek bridge ki tarah kaam karta hai."
    }
    return meanings.get(lang_code, meanings['en'])


def _get_generic_insight(lang_code):
    """Get professional generic insight for non-symbol keywords."""
    insights = {
        'en': "The appearance of this detail suggests that your mind is organizing impressions from your daily life into a meaningful psychological pattern.",
        'hi': "इस विवरण की उपस्थिति बताती है कि आपका मन आपके दैनिक जीवन के प्रभावों को एक सार्थक मनोवैज्ञानिक पैटर्न में व्यवस्थित कर रहा है।",
        'mr': "या तपशीलाचे स्वरूप सूचित करते की तुमचे मन तुमच्या दैनंदिन जीवनातील छापांना एका अर्थपूर्ण मनोवैज्ञानिक नमुन्यात व्यवस्थित करत आहे.",
        'hinglish': "Is detail ka dikhna suggest karta hai ki aapka mind daily life ke impressions ko ek meaningful psychological pattern mein organize kar raha hai."
    }
    return insights.get(lang_code, insights['en'])


def _generate_overall_interpretation(elements, emotion, sentiment, keywords, lang_code):
    """Combine analysis into a specific context-aware narrative."""
    templates = INTERPRETATION_TEMPLATES.get(lang_code, INTERPRETATION_TEMPLATES['en'])
    
    keywords_set = set([k.lower() for k in keywords])
    
    if not elements:
        return templates['no_elements'].format(emotion=emotion)
    
    # Get symbol names for intro
    primary_symbols = ", ".join([e['element'].lower() for e in elements[:2]])
    intro = templates['intro'].format(symbols=primary_symbols, emotion=emotion)
    
    # conflict context detection
    has_fear_context = any(kw in FEAR_THEMES for kw in keywords_set) or \
                      any(e.get('emotion') == 'fear' for e in elements)
    
    # Core Logic for section selection
    if emotion in POSITIVE_EMOTIONS and not has_fear_context:
        mid = templates['mid_positive']
    elif emotion in NEGATIVE_EMOTIONS or has_fear_context:
        mid = templates['mid_negative']
    elif sentiment == 'positive':
        mid = templates['mid_positive']
    elif sentiment == 'negative':
        mid = templates['mid_negative']
    else:
        mid = templates['mid_neutral']
    
    # Ensure interpretation is never empty or "weak"
    narrative = f"{intro} {mid} {templates['closing']}"
    if len(narrative) < 100: # Extra padding for completeness
         narrative += f" {templates['intro'].split('{symbols}')[0].strip()} elements often surface during times of mental processing."
         
    return narrative


def _generate_final_insight(emotion, lang_code):
    """Create a gentle reflective message in the specified language."""
    templates = INTERPRETATION_TEMPLATES.get(lang_code, INTERPRETATION_TEMPLATES['en'])
    
    if emotion == 'fear':
        return templates['insight_fear']
    elif emotion == 'joy' or emotion == 'love':
        return templates['insight_joy']
    elif emotion == 'sadness':
        return templates['insight_sadness']
    else:
        return templates['insight_default']

"""
Dream Decoder - Jungian Analyzer
Service for specialized Jungian Psychology dream analysis using Google Gemini API
"""
import os
from dotenv import load_dotenv

# Try to import Gemini AI, but don't fail the whole app if it's missing
try:
    import google.generativeai as genai
    HAS_GEMINI = True
except ImportError:
    HAS_GEMINI = False
    print("WARNING: google-generativeai not installed. Jungian analysis will be disabled.")

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if HAS_GEMINI and GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
elif not GEMINI_API_KEY:
    print("WARNING: GEMINI_API_KEY not found in environment variables.")

def analyze_jungian(dream_text):
    """
    Analyze dream text using Jungian Psychology via Google Gemini API.
    """
    if not HAS_GEMINI:
        return {
            "error": "Google Generative AI library is not installed. Please run setup.bat to install it."
        }
        
    if not GEMINI_API_KEY:
        return {
            "error": "Gemini API key not configured. Please add GEMINI_API_KEY to your .env file."
        }
    
    if not dream_text or len(dream_text.strip()) < 10:
        return {
            "error": "Dream text is too short for meaningful analysis."
        }

    try:
        # Initialize the model
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Structured prompt as requested
        prompt = f"""Analyze the following dream using Jungian Psychology. 
Focus on:
- Archetypes (Shadow, Anima/Animus, Self, Persona)
- Symbols and their deeper unconscious meanings
- Collective unconscious references
- Emotional interpretation
- Personal growth insight

Dream:
{dream_text}

Return output in simple, clear language.

Title: Jungian Interpretation
Sections:
1. Symbols Meaning: [Your analysis here]
2. Archetypes Identified: [Your analysis here]
3. Emotional Insight: [Your analysis here]
4. Personal Growth Message: [Your analysis here]
"""
        
        # Generate content
        response = model.generate_content(prompt)
        
        if not response.text:
            return {"error": "Received empty response from Gemini API."}
            
        return {
            "analysis": response.text,
            "provider": "Google Gemini"
        }
        
    except Exception as e:
        error_msg = str(e).lower()
        if "429" in error_msg or "quota" in error_msg or "exhausted" in error_msg:
            print("WARNING: Gemini API Quota Exceeded. Using fallback analysis.")
            fallback_text = (
                "1. Symbols Meaning: Your dream contains rich symbolism, but our AI is currently at maximum capacity. "
                "Commonly, symbols represent aspects of your waking life that need attention.\n\n"
                "2. Archetypes Identified: The characters in your dream often reflect parts of your own psyche—such as the Shadow "
                "(hidden fears) or the Anima/Animus (inner feminine/masculine).\n\n"
                "3. Emotional Insight: Your feelings during the dream are the most accurate guide to its meaning. "
                "Consider what emotions were strongest and how they relate to your current life.\n\n"
                "4. Personal Growth Message: Every dream is an opportunity to integrate hidden parts of yourself. "
                "Reflect on the symbols and how they might guide your waking choices."
            )
            return {
                "analysis": fallback_text,
                "provider": "Fallback (API Quota Exceeded)"
            }
            
        print(f"ERROR in Jungian Analysis: {str(e)}")
        return {
            "error": f"Failed to perform Jungian analysis: {str(e)}"
        }

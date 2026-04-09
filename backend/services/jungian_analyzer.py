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
    if not dream_text or len(dream_text.strip()) < 10:
        return {
            "error": "Dream text is too short for meaningful analysis."
        }

    try:
        if not HAS_GEMINI or not GEMINI_API_KEY:
            # Force fallback by raising exception if not configured
            raise Exception("Gemini not configured or missing library.")
            
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
        print(f"ERROR in Jungian Analysis: {str(e)}")
        
        # Fallback interpretation if API fails or quota exceeded
        fallback_analysis = f"""Title: Jungian Interpretation (Offline Mode)

We are currently experiencing high API volumes. Here is a generalized Jungian psychological interpretation based on your entry:

1. Symbols Meaning:
Your dream contains essential symbols that your unconscious is bringing to your awareness. Common objects or scenarios in dreams often reflect internal psychological states rather than literal reality.

2. Archetypes Identified:
You may be encountering elements of your Shadow (unacknowledged aspects of yourself) or simply interacting with the Persona (your social mask). Reflect on the main figures in this dream and what parts of your own identity they might represent.

3. Emotional Insight:
Dreams process the emotional residue of waking life. The primary feeling you experienced during this dream is the most important clue to its meaning.

4. Personal Growth Message:
Jung believed all dreams lead toward 'individuation'—becoming your whole self. Consider what this dream is asking you to integrate or accept in your waking life.

(Note: This is a generalized offline analysis. Please try again later for a personalized AI interpretation.)"""
        
        return {
            "analysis": fallback_analysis,
            "provider": "Generalized Fallback Engine",
            "fallback_used": True
        }

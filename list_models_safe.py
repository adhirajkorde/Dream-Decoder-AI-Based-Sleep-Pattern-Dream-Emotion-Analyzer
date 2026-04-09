import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

try:
    models = genai.list_models()
    with open('models_utf8.txt', 'w', encoding='utf-8') as f:
        f.write("Available models:\n")
        count = 0
        for m in models:
            count += 1
            if 'generateContent' in m.supported_generation_methods:
                f.write(m.name + "\n")
        f.write(f"Total models parsed: {count}\n")
except Exception as e:
    import traceback
    with open('models_utf8.txt', 'w', encoding='utf-8') as f:
        f.write("Error occurred:\n")
        f.write(str(e) + "\n")
        f.write(traceback.format_exc() + "\n")

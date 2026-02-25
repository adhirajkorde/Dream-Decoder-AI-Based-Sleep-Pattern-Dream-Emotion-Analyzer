import sys
import os
sys.path.append(os.getcwd())
from backend.services.nlp_engine import analyze_dream
from backend.services.dream_interpreter import FEAR_THEMES

d = "I was driving a flying car through a small city. I felt very happy and excited, everything was moving so fast!"
r = analyze_dream(d)
interp = r['interpretation']['overall_interpretation']
kws = r['keywords']
emo = r['primary_emotion']
sen = r['sentiment']
print(f"DEBUG_EMO: {emo}")
print(f"DEBUG_SEN: {sen}")
print(f"DEBUG_KWS: {kws}")
print(f"DEBUG_INTERP: {interp}")

no_conflict = "inner conflict" not in interp.lower()
print(f"RESULT_NO_CONFLICT: {no_conflict}")

has_fear_kw = any(kw.lower() in FEAR_THEMES for kw in kws)
print(f"RESULT_HAS_FEAR_KW: {has_fear_kw}")

print("---START---")
print(f"EMO:{emo}")
print(f"SEN:{sen}")
print(f"KWS:{','.join(kws)}")
print(f"INTERP:{interp}")
print(f"NO_CONFLICT_CHECK:{no_conflict}")
high_weight = [e['element'] for e in r['interpretation']['numbered_elements'] if e.get('weight', 0) >= 3]

print(f"HIGH_WEIGHT:{','.join(high_weight)}")
print("---END---")

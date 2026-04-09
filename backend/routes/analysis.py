"""
Dream Decoder - Analysis Routes
API endpoints for text analysis (without saving)
"""
from flask import Blueprint, request, jsonify
from backend.services.nlp_engine import analyze_dream
from backend.services.jungian_analyzer import analyze_jungian

analysis_bp = Blueprint('analysis', __name__)


@analysis_bp.route('/api/analyze', methods=['POST'])
def analyze_text():
    """
    Analyze dream text without saving.
    Useful for preview before saving.
    """
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({'error': 'Text is required'}), 400
    
    text = data['text'].strip()
    if not text:
        return jsonify({'error': 'Text cannot be empty'}), 400
    
    # Perform analysis
    analysis = analyze_dream(text)
    
    return jsonify(analysis)


@analysis_bp.route('/api/analyze/jungian', methods=['POST'])
def analyze_jungian_route():
    """
    Specialized Jungian analysis using Gemini API.
    """
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({'error': 'Text is required'}), 400
    
    text = data['text'].strip()
    if not text:
        return jsonify({'error': 'Text cannot be empty'}), 400
    
    # Perform Jungian analysis
    result = analyze_jungian(text)
    
    if 'error' in result:
        return jsonify(result), 500
        
    return jsonify(result)


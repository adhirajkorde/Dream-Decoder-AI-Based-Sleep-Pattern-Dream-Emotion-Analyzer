"""
Dream Decoder - Analysis Routes
API endpoints for text analysis (without saving)
"""
from flask import Blueprint, request, jsonify
from backend.services.nlp_engine import analyze_dream

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

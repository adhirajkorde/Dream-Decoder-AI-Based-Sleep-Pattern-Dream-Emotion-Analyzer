"""
Dream Decoder - Dream Routes
API endpoints for dream CRUD operations
"""
from flask import Blueprint, request, jsonify
from backend.models.dream import Dream
from backend.services.nlp_engine import analyze_dream

dreams_bp = Blueprint('dreams', __name__)


@dreams_bp.route('/api/dreams', methods=['POST'])
def create_dream():
    """Create a new dream entry with NLP analysis."""
    try:
        data = request.get_json()
        print(f"DEBUG: Received dream data: {data}")
        
        if not data or 'content' not in data:
            return jsonify({'error': 'Dream content is required'}), 400
        
        content = data['content'].strip()
        if not content:
            return jsonify({'error': 'Dream content cannot be empty'}), 400
        
        # Perform NLP analysis
        print("DEBUG: Starting NLP analysis...")
        analysis = analyze_dream(content)
        print("DEBUG: NLP analysis complete.")
        
        # Create dream object
        print("DEBUG: Creating Dream object...")
        dream = Dream(
            content=content,
            sentiment=analysis['sentiment'],
            sentiment_score=analysis['sentiment_score'],
            primary_emotion=analysis['primary_emotion'],
            emotion_scores=analysis['emotion_scores'],
            keywords=analysis['keywords'],
            entities=analysis['entities'],
            interpretation=analysis.get('interpretation', {}) 
        )
        
        # Save to database
        print("DEBUG: Saving to database...")
        dream.save()
        print(f"DEBUG: Saved dream with ID: {dream.id}")
        
        # Return dream with analysis
        response = dream.to_dict()
        response['analysis'] = {
            'themes': analysis['themes'],
            'summary': analysis['summary'],
            'emotion_confidence': analysis.get('emotion_confidence', 0)
        }
        
        print("DEBUG: Returning successful response.")
        return jsonify(response), 201
    except Exception as e:
        import traceback
        print(f"ERROR in create_dream: {e}")
        traceback.print_exc()
        return jsonify({'error': 'An internal error occurred during dream analysis'}), 500


@dreams_bp.route('/api/dreams', methods=['GET'])
def get_dreams():
    """Get all dreams with optional pagination."""
    limit = request.args.get('limit', 50, type=int)
    offset = request.args.get('offset', 0, type=int)
    
    # Validation
    if limit < 1 or limit > 100:
        limit = 50
    if offset < 0:
        offset = 0
        
    dreams = Dream.get_all(limit=limit, offset=offset)
    total = Dream.count()
    
    return jsonify({
        'dreams': [d.to_dict() for d in dreams],
        'total': total,
        'limit': limit,
        'offset': offset
    })


@dreams_bp.route('/api/dreams/<int:dream_id>', methods=['GET'])
def get_dream(dream_id):
    """Get a specific dream by ID."""
    dream = Dream.get_by_id(dream_id)
    
    if not dream:
        return jsonify({'error': 'Dream not found'}), 404
    
    return jsonify(dream.to_dict())


@dreams_bp.route('/api/dreams/<int:dream_id>', methods=['DELETE'])
def delete_dream(dream_id):
    """Delete a dream by ID."""
    deleted = Dream.delete(dream_id)
    
    if not deleted:
        return jsonify({'error': 'Dream not found'}), 404
    
    return jsonify({'message': 'Dream deleted successfully'})


@dreams_bp.route('/api/dreams/recent', methods=['GET'])
def get_recent_dreams():
    """Get dreams from the last N days."""
    days = request.args.get('days', 7, type=int)
    
    # Validation
    if days < 1 or days > 365:
        return jsonify({'error': 'Days must be between 1 and 365'}), 400
        
    dreams = Dream.get_recent(days=days)
    
    return jsonify({
        'dreams': [d.to_dict() for d in dreams],
        'count': len(dreams),
        'days': days
    })


@dreams_bp.route('/api/dreams/<int:dream_id>/export', methods=['GET'])
def export_dream_pdf(dream_id):
    """Export a dream as a PDF file."""
    from backend.services.pdf_generator import generate_dream_pdf
    from flask import send_file
    
    dream = Dream.get_by_id(dream_id)
    if not dream:
        return jsonify({'error': 'Dream not found'}), 404
        
    try:
        pdf_buffer = generate_dream_pdf(dream.to_dict())
    except Exception as e:
        print(f"Error generating PDF: {e}")
        return jsonify({'error': 'Failed to generate PDF report'}), 500
    
    filename = f"dream_export_{dream_id}.pdf"
    if dream.created_at:
        try:
            if isinstance(dream.created_at, str):
                from datetime import datetime
                dt = datetime.fromisoformat(dream.created_at.replace('Z', '+00:00'))
            else:
                dt = dream.created_at
            filename = f"Dream_{dt.strftime('%Y%m%d_%H%M%S')}.pdf"
        except:
            pass
            
    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name=filename,
        mimetype='application/pdf'
    )

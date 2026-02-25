"""
Dream Decoder - Insights Routes
API endpoints for insights and trends
"""
from flask import Blueprint, request, jsonify
from backend.services.insights_generator import generate_insights, get_trends

from backend.middleware.auth import require_auth

insights_bp = Blueprint('insights', __name__)


@insights_bp.route('/api/insights', methods=['GET'])
@require_auth
def get_insights():
    """Get personalized insights and recommendations."""
    days = request.args.get('days', 7, type=int)
    user = request.current_user
    user_id = user.id
    language = getattr(user, 'language_preference', 'en')
    
    insights = generate_insights(user_id, days=days, language=language)
    
    return jsonify(insights)


@insights_bp.route('/api/trends', methods=['GET'])
@require_auth
def get_trend_data():
    """Get trend data for charts."""
    days = request.args.get('days', 30, type=int)
    user_id = request.current_user.id
    
    trends = get_trends(user_id, days=days)
    
    return jsonify(trends)

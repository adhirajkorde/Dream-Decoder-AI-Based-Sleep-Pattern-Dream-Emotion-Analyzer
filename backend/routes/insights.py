"""
Dream Decoder - Insights Routes
API endpoints for insights and trends
"""
from flask import Blueprint, request, jsonify
from backend.services.insights_generator import generate_insights, get_trends

insights_bp = Blueprint('insights', __name__)


@insights_bp.route('/api/insights', methods=['GET'])
def get_insights():
    """Get personalized insights and recommendations."""
    days = request.args.get('days', 7, type=int)
    
    insights = generate_insights(days=days)
    
    return jsonify(insights)


@insights_bp.route('/api/trends', methods=['GET'])
def get_trend_data():
    """Get trend data for charts."""
    days = request.args.get('days', 30, type=int)
    
    trends = get_trends(days=days)
    
    return jsonify(trends)

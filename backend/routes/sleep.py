"""
Dream Decoder - Sleep Routes
API endpoints for sleep record operations
"""
from flask import Blueprint, request, jsonify
from backend.models.sleep import SleepRecord
from backend.middleware.auth import require_auth

sleep_bp = Blueprint('sleep', __name__)


@sleep_bp.route('/api/sleep', methods=['POST'])
@require_auth
def create_sleep_record():
    """Create a new sleep record for the authenticated user."""
    user = request.current_user
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Request body is required'}), 400
    
    # Validate date format
    try:
        from datetime import date as dt_date
        dt_date.fromisoformat(data['date'])
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400

    # Create sleep record
    try:
        record = SleepRecord(
            user_id=user.id,
            date=data['date'],
            sleep_time=data.get('sleep_time'),
            wake_time=data.get('wake_time'),
            duration_hours=float(data['duration_hours']),
            wakeups=int(data.get('wakeups', 0)),
            quality_rating=int(data['quality_rating']) if data.get('quality_rating') else None,
            notes=data.get('notes', '')
        )
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid duration or wakeup count'}), 400
    
    # Check if record already exists for this date and user
    existing = SleepRecord.get_by_date(user.id, data['date'])
    if existing:
        # Update existing record
        record.id = existing.id
    
    try:
        record.save()
        return jsonify(record.to_dict()), 201
    except Exception as e:
        # Log error internally, return sanitized message
        print(f"Error saving sleep record: {e}")
        return jsonify({'error': 'Failed to save sleep record'}), 500


@sleep_bp.route('/api/sleep', methods=['GET'])
@require_auth
def get_sleep_records():
    """Get all sleep records for the authenticated user with optional pagination."""
    user = request.current_user
    limit = request.args.get('limit', 50, type=int)
    offset = request.args.get('offset', 0, type=int)
    
    records = SleepRecord.get_all(user.id, limit=limit, offset=offset)
    
    return jsonify({
        'records': [r.to_dict() for r in records],
        'limit': limit,
        'offset': offset
    })


@sleep_bp.route('/api/sleep/<int:record_id>', methods=['GET'])
def get_sleep_record(record_id):
    """Get a specific sleep record by ID."""
    record = SleepRecord.get_by_id(record_id)
    
    if not record:
        return jsonify({'error': 'Sleep record not found'}), 404
    
    return jsonify(record.to_dict())


@sleep_bp.route('/api/sleep/<int:record_id>', methods=['DELETE'])
@require_auth
def delete_sleep_record(record_id):
    """Delete a sleep record by ID."""
    user = request.current_user
    deleted = SleepRecord.delete(record_id, user.id)
    
    if not deleted:
        return jsonify({'error': 'Sleep record not found or unauthorized'}), 404
    
    return jsonify({'message': 'Sleep record deleted successfully'})


@sleep_bp.route('/api/sleep/all', methods=['DELETE'])
@require_auth
def delete_all_sleep_records():
    """Delete all sleep records for the authenticated user."""
    user = request.current_user
    
    try:
        count = SleepRecord.delete_all(user.id)
        return jsonify({
            'message': f'Successfully deleted {count} sleep records',
            'count': count
        }), 200
    except Exception as e:
        print(f"Error deleting sleep records: {e}")
        return jsonify({'error': 'Failed to delete sleep records'}), 500


@sleep_bp.route('/api/sleep/recent', methods=['GET'])
@require_auth
def get_recent_sleep():
    """Get sleep records from the last N days for the authenticated user."""
    user = request.current_user
    days = request.args.get('days', 7, type=int)
    records = SleepRecord.get_recent(user.id, days=days)
    
    # Calculate averages
    avg_quality = SleepRecord.get_average_quality(user.id, days)
    avg_duration = SleepRecord.get_average_duration(user.id, days)
    
    return jsonify({
        'records': [r.to_dict() for r in records],
        'count': len(records),
        'days': days,
        'averages': {
            'quality': round(avg_quality, 1) if avg_quality else None,
            'duration': round(avg_duration, 1) if avg_duration else None
        }
    })


@sleep_bp.route('/api/sleep/stats', methods=['GET'])
@require_auth
def get_sleep_stats():
    """Get sleep statistics for the authenticated user."""
    user = request.current_user
    days = request.args.get('days', 7, type=int)
    
    avg_quality = SleepRecord.get_average_quality(user.id, days)
    avg_duration = SleepRecord.get_average_duration(user.id, days)
    records = SleepRecord.get_recent(user.id, days)
    
    return jsonify({
        'period_days': days,
        'total_records': len(records),
        'avg_quality': round(avg_quality, 1) if avg_quality else None,
        'avg_duration': round(avg_duration, 1) if avg_duration else None
    })

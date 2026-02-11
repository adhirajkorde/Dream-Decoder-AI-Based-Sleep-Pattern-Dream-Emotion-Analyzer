"""
Dream Decoder - Sleep Routes
API endpoints for sleep record operations
"""
from flask import Blueprint, request, jsonify
from backend.models.sleep import SleepRecord

sleep_bp = Blueprint('sleep', __name__)


@sleep_bp.route('/api/sleep', methods=['POST'])
def create_sleep_record():
    """Create a new sleep record."""
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Request body is required'}), 400
    
    # Validate required fields
    if 'date' not in data:
        return jsonify({'error': 'Date is required'}), 400
    if 'duration_hours' not in data:
        return jsonify({'error': 'Duration is required'}), 400
    
    # Create sleep record
    record = SleepRecord(
        date=data['date'],
        duration_hours=float(data['duration_hours']),
        wakeups=int(data.get('wakeups', 0)),
        quality_rating=int(data['quality_rating']) if data.get('quality_rating') else None,
        notes=data.get('notes', '')
    )
    
    # Check if record already exists for this date
    existing = SleepRecord.get_by_date(data['date'])
    if existing:
        # Update existing record
        record.id = existing.id
    
    record.save()
    
    return jsonify(record.to_dict()), 201


@sleep_bp.route('/api/sleep', methods=['GET'])
def get_sleep_records():
    """Get all sleep records with optional pagination."""
    limit = request.args.get('limit', 50, type=int)
    offset = request.args.get('offset', 0, type=int)
    
    records = SleepRecord.get_all(limit=limit, offset=offset)
    
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
def delete_sleep_record(record_id):
    """Delete a sleep record by ID."""
    deleted = SleepRecord.delete(record_id)
    
    if not deleted:
        return jsonify({'error': 'Sleep record not found'}), 404
    
    return jsonify({'message': 'Sleep record deleted successfully'})


@sleep_bp.route('/api/sleep/recent', methods=['GET'])
def get_recent_sleep():
    """Get sleep records from the last N days."""
    days = request.args.get('days', 7, type=int)
    records = SleepRecord.get_recent(days=days)
    
    # Calculate averages
    avg_quality = SleepRecord.get_average_quality(days)
    avg_duration = SleepRecord.get_average_duration(days)
    
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
def get_sleep_stats():
    """Get sleep statistics."""
    days = request.args.get('days', 7, type=int)
    
    avg_quality = SleepRecord.get_average_quality(days)
    avg_duration = SleepRecord.get_average_duration(days)
    records = SleepRecord.get_recent(days)
    
    return jsonify({
        'period_days': days,
        'total_records': len(records),
        'avg_quality': round(avg_quality, 1) if avg_quality else None,
        'avg_duration': round(avg_duration, 1) if avg_duration else None
    })

"""
Dream Decoder - Authentication Routes
API endpoints for user registration, login, and account management
"""
from flask import Blueprint, request, jsonify
from backend.models.user import User
from backend.middleware.auth import generate_token, require_auth

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/api/auth/signup', methods=['POST'])
def signup():
    """Register a new user account."""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Request body is required'}), 400
        
        # Extract fields
        username = data.get('username', '').strip()
        email = data.get('email', '').strip()
        password = data.get('password', '')
        language_preference = data.get('language_preference', 'en')
        
        # Validate required fields
        if not username or not email or not password:
            return jsonify({'error': 'Username, email, and password are required'}), 400
        
        # Create user
        user, error = User.create_user(username, email, password, language_preference)
        
        if error:
            return jsonify({'error': error}), 400
        
        # Generate token
        token = generate_token(user.id, user.username)
        
        return jsonify({
            'message': 'Account created successfully',
            'token': token,
            'user': user.to_dict()
        }), 201
        
    except Exception as e:
        print(f"Error in signup: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': 'Failed to create account'}), 500


@auth_bp.route('/api/auth/login', methods=['POST'])
def login():
    """Authenticate user and return token."""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Request body is required'}), 400
        
        # Extract fields (can be username or email)
        username_or_email = data.get('username') or data.get('email', '')
        password = data.get('password', '')
        
        if not username_or_email or not password:
            return jsonify({'error': 'Username/email and password are required'}), 400
        
        # Authenticate user
        user, error = User.authenticate(username_or_email.strip(), password)
        
        if error:
            return jsonify({'error': error}), 401
        
        # Generate token
        token = generate_token(user.id, user.username)
        
        return jsonify({
            'message': 'Login successful',
            'token': token,
            'user': user.to_dict()
        }), 200
        
    except Exception as e:
        print(f"Error in login: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': 'Login failed'}), 500


@auth_bp.route('/api/auth/logout', methods=['POST'])
@require_auth
def logout():
    """
    Logout user (client-side token removal).
    This endpoint exists for consistency, actual logout happens client-side.
    """
    return jsonify({'message': 'Logout successful'}), 200


@auth_bp.route('/api/auth/me', methods=['GET'])
@require_auth
def get_current_user():
    """Get current authenticated user information."""
    user = request.current_user
    return jsonify({'user': user.to_dict()}), 200


@auth_bp.route('/api/auth/account', methods=['DELETE'])
@require_auth
def delete_account():
    """Delete user account and all associated data."""
    try:
        user = request.current_user
        user_id = user.id
        username = user.username
        
        # Delete user (cascade will delete all dreams and sleep records)
        deleted = User.delete_user(user_id)
        
        if not deleted:
            return jsonify({'error': 'Failed to delete account'}), 500
        
        return jsonify({
            'message': f'Account "{username}" and all associated data deleted successfully'
        }), 200
        
    except Exception as e:
        print(f"Error deleting account: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': 'Failed to delete account'}), 500


@auth_bp.route('/api/auth/language', methods=['PUT'])
@require_auth
def update_language():
    """Update user's language preference."""
    try:
        data = request.get_json()
        
        if not data or 'language' not in data:
            return jsonify({'error': 'Language is required'}), 400
        
        language = data['language']
        
        # Validate language
        valid_languages = ['en', 'hi', 'mr', 'hinglish']
        if language not in valid_languages:
            return jsonify({'error': f'Invalid language. Must be one of: {", ".join(valid_languages)}'}), 400
        
        # Update user
        user = request.current_user
        user.update_language_preference(language)
        
        return jsonify({
            'message': 'Language preference updated',
            'user': user.to_dict()
        }), 200
        
    except Exception as e:
        print(f"Error updating language: {e}")
        return jsonify({'error': 'Failed to update language preference'}), 500

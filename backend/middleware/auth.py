"""
Dream Decoder - Authentication Middleware
JWT token validation and user authentication
"""
import jwt
import os
from functools import wraps
from flask import request, jsonify
from backend.models.user import User

# JWT Secret Key (should be in environment variable in production)
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-secret-key-change-in-production')
JWT_ALGORITHM = 'HS256'


def generate_token(user_id, username):
    """Generate a JWT token for a user."""
    import datetime
    
    payload = {
        'user_id': user_id,
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),  # Token expires in 7 days
        'iat': datetime.datetime.utcnow()
    }
    
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return token


def decode_token(token):
    """
    Decode and validate a JWT token.
    Returns (payload, error) tuple.
    """
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload, None
    except jwt.ExpiredSignatureError:
        return None, 'Token has expired'
    except jwt.InvalidTokenError:
        return None, 'Invalid token'


def get_token_from_request():
    """Extract JWT token from request headers."""
    auth_header = request.headers.get('Authorization')
    
    if not auth_header:
        return None
    
    # Expected format: "Bearer <token>"
    parts = auth_header.split()
    
    if len(parts) != 2 or parts[0].lower() != 'bearer':
        return None
    
    return parts[1]


def require_auth(f):
    """
    Decorator to protect routes that require authentication.
    Adds 'current_user' to the request context.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = get_token_from_request()
        
        if not token:
            return jsonify({'error': 'Authentication required'}), 401
        
        payload, error = decode_token(token)
        
        if error:
            return jsonify({'error': error}), 401
        
        # Get user from database
        user = User.get_by_id(payload['user_id'])
        
        if not user:
            return jsonify({'error': 'User not found'}), 401
        
        # Add user to request context
        request.current_user = user
        
        return f(*args, **kwargs)
    
    return decorated_function


def optional_auth(f):
    """
    Decorator for routes where authentication is optional.
    Adds 'current_user' to request context if authenticated, None otherwise.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = get_token_from_request()
        
        if token:
            payload, error = decode_token(token)
            
            if not error and payload:
                user = User.get_by_id(payload['user_id'])
                request.current_user = user if user else None
            else:
                request.current_user = None
        else:
            request.current_user = None
        
        return f(*args, **kwargs)
    
    return decorated_function

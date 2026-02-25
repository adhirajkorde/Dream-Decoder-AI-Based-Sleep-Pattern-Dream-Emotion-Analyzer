"""
Dream Decoder - User Model
Handles user authentication and account management
"""
import re
import bcrypt
from datetime import datetime
from backend.database.db import get_db_connection


class User:
    """User model for authentication and account management."""
    
    def __init__(self, id=None, username=None, email=None, password_hash=None, 
                 created_at=None, language_preference='en'):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at
        self.language_preference = language_preference
    
    def to_dict(self, include_sensitive=False):
        """Convert user to dictionary for JSON serialization."""
        data = {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at,
            'language_preference': self.language_preference
        }
        if include_sensitive:
            data['password_hash'] = self.password_hash
        return data
    
    @staticmethod
    def from_row(row):
        """Create User object from database row."""
        if row is None:
            return None
        
        # sqlite3.Row doesn't have .get(), so we check keys if needed
        # but language_preference has a default in the schema
        lang = 'en'
        if 'language_preference' in row.keys():
            lang = row['language_preference']
            
        return User(
            id=row['id'],
            username=row['username'],
            email=row['email'],
            password_hash=row['password_hash'],
            created_at=row['created_at'],
            language_preference=lang
        )
    
    @staticmethod
    def hash_password(password):
        """Hash a password using bcrypt."""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    
    def verify_password(self, password):
        """Verify a password against the stored hash."""
        if not self.password_hash:
            return False
        try:
            return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
        except (ValueError, Exception) as e:
            print(f"Password verification error: {e}")
            return False
    
    @staticmethod
    def validate_email(email):
        """Validate email format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def validate_username(username):
        """Validate username (alphanumeric, underscore, 3-20 chars)."""
        if not username or len(username) < 3 or len(username) > 20:
            return False
        pattern = r'^[a-zA-Z0-9_]+$'
        return re.match(pattern, username) is not None
    
    @staticmethod
    def validate_password(password):
        """
        Validate password strength.
        Requirements: At least 8 characters, 1 uppercase, 1 lowercase, 1 number
        """
        if not password or len(password) < 8:
            return False, "Password must be at least 8 characters long"
        
        if not re.search(r'[A-Z]', password):
            return False, "Password must contain at least one uppercase letter"
        
        if not re.search(r'[a-z]', password):
            return False, "Password must contain at least one lowercase letter"
        
        if not re.search(r'[0-9]', password):
            return False, "Password must contain at least one number"
        
        return True, "Password is valid"
    
    def save(self):
        """Save user to database (insert only, no updates for security)."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            if self.id is None:
                # Insert new user
                cursor.execute('''
                    INSERT INTO users (username, email, password_hash, language_preference)
                    VALUES (?, ?, ?, ?)
                ''', (
                    self.username,
                    self.email,
                    self.password_hash,
                    self.language_preference
                ))
                self.id = cursor.lastrowid
                
                # Get the created_at timestamp
                cursor.execute('SELECT created_at FROM users WHERE id=?', (self.id,))
                row = cursor.fetchone()
                if row:
                    self.created_at = row['created_at']
            else:
                # Update existing user (only language preference and email)
                cursor.execute('''
                    UPDATE users SET email=?, language_preference=?
                    WHERE id=?
                ''', (
                    self.email,
                    self.language_preference,
                    self.id
                ))
            
            conn.commit()
        
        return self
    
    @staticmethod
    def create_user(username, email, password, language_preference='en'):
        """
        Create a new user with validation.
        Returns (user, error_message) tuple.
        """
        # Validate username
        if not User.validate_username(username):
            return None, "Username must be 3-20 characters and contain only letters, numbers, and underscores"
        
        # Validate email
        if not User.validate_email(email):
            return None, "Invalid email format"
        
        # Validate password
        is_valid, message = User.validate_password(password)
        if not is_valid:
            return None, message
        
        # Check if username already exists
        if User.get_by_username(username):
            return None, "Username already exists"
        
        # Check if email already exists
        if User.get_by_email(email):
            return None, "Email already registered"
        
        # Create user
        user = User(
            username=username,
            email=email,
            password_hash=User.hash_password(password),
            language_preference=language_preference
        )
        
        try:
            user.save()
            return user, None
        except Exception as e:
            print(f"Error creating user: {e}")
            return None, "Failed to create user account"
    
    @staticmethod
    def get_by_id(user_id):
        """Get a user by ID."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE id=?', (user_id,))
            row = cursor.fetchone()
            return User.from_row(row)
    
    @staticmethod
    def get_by_username(username):
        """Get a user by username."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username=?', (username,))
            row = cursor.fetchone()
            return User.from_row(row)
    
    @staticmethod
    def get_by_email(email):
        """Get a user by email."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE email=?', (email,))
            row = cursor.fetchone()
            return User.from_row(row)
    
    @staticmethod
    def authenticate(username_or_email, password):
        """
        Authenticate a user by username/email and password.
        Returns (user, error_message) tuple.
        """
        # Try to find user by username or email
        user = User.get_by_username(username_or_email)
        if not user:
            user = User.get_by_email(username_or_email)
        
        if not user:
            return None, "Invalid username or password"
        
        if not user.verify_password(password):
            return None, "Invalid username or password"
        
        return user, None
    
    @staticmethod
    def delete_user(user_id):
        """
        Delete a user and all associated data (cascade delete).
        Returns True if successful, False otherwise.
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            # Delete user (cascade will handle dreams and sleep records)
            cursor.execute('DELETE FROM users WHERE id=?', (user_id,))
            deleted = cursor.rowcount > 0
            
            conn.commit()
            return deleted
    
    def update_language_preference(self, language):
        """Update user's language preference."""
        self.language_preference = language
        self.save()
        return self

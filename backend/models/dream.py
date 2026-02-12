"""
Dream Decoder - Dream Model
Handles CRUD operations for dream entries
"""
import json
from datetime import datetime
from backend.database.db import get_db_connection


class Dream:
    """Dream model for database operations."""
    
    def __init__(self, id=None, content=None, created_at=None, sentiment=None,
                 sentiment_score=None, primary_emotion=None, emotion_scores=None,
                 keywords=None, entities=None, interpretation=None):
        self.id = id
        self.content = content
        self.created_at = created_at
        self.sentiment = sentiment
        self.sentiment_score = sentiment_score
        self.primary_emotion = primary_emotion
        self.emotion_scores = emotion_scores or {}
        self.keywords = keywords or []
        self.entities = entities or []
        self.interpretation = interpretation or {}
    
    def to_dict(self):
        """Convert dream to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'content': self.content,
            'created_at': self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at,
            'sentiment': self.sentiment,
            'sentiment_score': self.sentiment_score,
            'primary_emotion': self.primary_emotion,
            'emotion_scores': self.emotion_scores,
            'keywords': self.keywords,
            'entities': self.entities,
            'interpretation': self.interpretation
        }
    
    @staticmethod
    def from_row(row):
        """Create Dream object from database row."""
        if row is None:
            return None
        
        return Dream(
            id=row['id'],
            content=row['content'],
            created_at=row['created_at'],
            sentiment=row['sentiment'],
            sentiment_score=row['sentiment_score'],
            primary_emotion=row['primary_emotion'],
            emotion_scores=json.loads(row['emotion_scores']) if row['emotion_scores'] else {},
            keywords=json.loads(row['keywords']) if row['keywords'] else [],
            entities=json.loads(row['entities']) if row['entities'] else [],
            interpretation=json.loads(row['interpretation']) if 'interpretation' in row.keys() and row['interpretation'] else {}
        )
    
    def save(self):
        """Save dream to database (insert or update)."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            if self.id is None:
                # Insert new dream
                cursor.execute('''
                    INSERT INTO dreams (content, sentiment, sentiment_score, primary_emotion,
                                       emotion_scores, keywords, entities, interpretation)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    self.content,
                    self.sentiment,
                    self.sentiment_score,
                    self.primary_emotion,
                    json.dumps(self.emotion_scores),
                    json.dumps(self.keywords),
                    json.dumps(self.entities),
                    json.dumps(self.interpretation)
                ))
                self.id = cursor.lastrowid
            else:
                # Update existing dream
                cursor.execute('''
                    UPDATE dreams SET content=?, sentiment=?, sentiment_score=?,
                           primary_emotion=?, emotion_scores=?, keywords=?, entities=?, interpretation=?
                    WHERE id=?
                ''', (
                    self.content,
                    self.sentiment,
                    self.sentiment_score,
                    self.primary_emotion,
                    json.dumps(self.emotion_scores),
                    json.dumps(self.keywords),
                    json.dumps(self.entities),
                    json.dumps(self.interpretation),
                    self.id
                ))
            
            conn.commit()
            
            # Get the created_at timestamp
            if self.created_at is None:
                cursor.execute('SELECT created_at FROM dreams WHERE id=?', (self.id,))
                row = cursor.fetchone()
                if row:
                    self.created_at = row['created_at']
        
        return self
    
    @staticmethod
    def get_all(limit=100, offset=0):
        """Get all dreams, ordered by most recent first."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT * FROM dreams ORDER BY created_at DESC LIMIT ? OFFSET ?
            ''', (limit, offset))
            
            rows = cursor.fetchall()
            return [Dream.from_row(row) for row in rows]
    
    @staticmethod
    def get_by_id(dream_id):
        """Get a dream by ID."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM dreams WHERE id=?', (dream_id,))
            row = cursor.fetchone()
            return Dream.from_row(row)
    
    @staticmethod
    def delete(dream_id):
        """Delete a dream by ID."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM dreams WHERE id=?', (dream_id,))
            deleted = cursor.rowcount > 0
            
            conn.commit()
            return deleted
    
    @staticmethod
    def get_recent(days=7):
        """Get dreams from the last N days."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT * FROM dreams 
                WHERE created_at >= datetime('now', '-' || ? || ' days')
                ORDER BY created_at DESC
            ''', (days,))
            
            rows = cursor.fetchall()
            return [Dream.from_row(row) for row in rows]
    
    @staticmethod
    def count():
        """Get total count of dreams."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('SELECT COUNT(*) as count FROM dreams')
            row = cursor.fetchone()
            return row['count'] if row else 0

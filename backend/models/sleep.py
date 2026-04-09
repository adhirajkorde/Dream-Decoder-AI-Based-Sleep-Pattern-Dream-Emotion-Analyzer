"""
Dream Decoder - Sleep Record Model
Handles CRUD operations for sleep data
"""
import json
from datetime import datetime, date
from backend.database.db import get_db_connection


class SleepRecord:
    """Sleep record model for database operations."""
    
    def __init__(self, id=None, user_id=None, date=None, sleep_time=None, wake_time=None,
                 duration_hours=None, wakeups=0, quality_rating=None, notes=None, created_at=None):
        self.id = id
        self.user_id = user_id
        self.date = date
        self.sleep_time = sleep_time
        self.wake_time = wake_time
        self.duration_hours = duration_hours
        self.wakeups = wakeups
        self.quality_rating = quality_rating
        self.notes = notes
        self.created_at = created_at
    
    def to_dict(self):
        """Convert sleep record to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'date': self.date.isoformat() if isinstance(self.date, (datetime, date)) else self.date,
            'sleep_time': self.sleep_time,
            'wake_time': self.wake_time,
            'duration_hours': self.duration_hours,
            'wakeups': self.wakeups,
            'quality_rating': self.quality_rating,
            'notes': self.notes,
            'created_at': self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at
        }
    
    @staticmethod
    def from_row(row):
        """Create SleepRecord object from database row."""
        if row is None:
            return None
        
        return SleepRecord(
            id=row['id'],
            user_id=row['user_id'],
            date=row['date'],
            sleep_time=row['sleep_time'],
            wake_time=row['wake_time'],
            duration_hours=row['duration_hours'],
            wakeups=row['wakeups'],
            quality_rating=row['quality_rating'],
            notes=row['notes'],
            created_at=row['created_at']
        )
    
    def save(self):
        """Save sleep record to database (insert or update)."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            if self.id is None:
                # Insert new record
                cursor.execute('''
                    INSERT INTO sleep_records (user_id, date, sleep_time, wake_time, duration_hours, wakeups, quality_rating, notes)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    self.user_id,
                    self.date,
                    self.sleep_time,
                    self.wake_time,
                    self.duration_hours,
                    self.wakeups,
                    self.quality_rating,
                    self.notes
                ))
                self.id = cursor.lastrowid
            else:
                # Update existing record
                cursor.execute('''
                    UPDATE sleep_records SET date=?, sleep_time=?, wake_time=?, duration_hours=?, 
                           wakeups=?, quality_rating=?, notes=?
                    WHERE id=?
                ''', (
                    self.date,
                    self.sleep_time,
                    self.wake_time,
                    self.duration_hours,
                    self.wakeups,
                    self.quality_rating,
                    self.notes,
                    self.id
                ))
            
            conn.commit()
            
            # Get the created_at timestamp
            if self.created_at is None:
                cursor.execute('SELECT created_at FROM sleep_records WHERE id=?', (self.id,))
                row = cursor.fetchone()
                if row:
                    self.created_at = row['created_at']
        
        return self
    
    @staticmethod
    def get_all(user_id, limit=100, offset=0):
        """Get all sleep records for a user, ordered by most recent first."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT * FROM sleep_records WHERE user_id=? ORDER BY date DESC LIMIT ? OFFSET ?
            ''', (user_id, limit, offset))
            
            rows = cursor.fetchall()
            return [SleepRecord.from_row(row) for row in rows]
    
    @staticmethod
    def get_by_id(record_id):
        """Get a sleep record by ID."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM sleep_records WHERE id=?', (record_id,))
            row = cursor.fetchone()
            return SleepRecord.from_row(row)
    
    @staticmethod
    def get_by_date(user_id, record_date):
        """Get sleep record for a specific date and user."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM sleep_records WHERE user_id=? AND date=?', (user_id, record_date))
            row = cursor.fetchone()
            return SleepRecord.from_row(row)
    
    @staticmethod
    def delete(record_id, user_id):
        """Delete a sleep record by ID, ensuring it belongs to the user."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM sleep_records WHERE id=? AND user_id=?', (record_id, user_id))
            deleted = cursor.rowcount > 0
            
            conn.commit()
            return deleted
    
    @staticmethod
    def get_recent(user_id, days=7):
        """Get sleep records from the last N days for a user."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT * FROM sleep_records 
                WHERE user_id=? AND date >= date('now', '-' || ? || ' days')
                ORDER BY date DESC
            ''', (user_id, days))
            
            rows = cursor.fetchall()
            return [SleepRecord.from_row(row) for row in rows]
    
    @staticmethod
    def get_average_quality(user_id, days=7):
        """Get average sleep quality for the last N days for a user."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT AVG(quality_rating) as avg_quality 
                FROM sleep_records 
                WHERE user_id=? AND date >= date('now', '-' || ? || ' days')
                AND quality_rating IS NOT NULL
            ''', (user_id, days))
            
            row = cursor.fetchone()
            return row['avg_quality'] if row and row['avg_quality'] else None
    
    @staticmethod
    def get_average_duration(user_id, days=7):
        """Get average sleep duration for the last N days for a user."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT AVG(duration_hours) as avg_duration 
                FROM sleep_records 
                WHERE user_id=? AND date >= date('now', '-' || ? || ' days')
            ''', (user_id, days))
            
            row = cursor.fetchone()
            return row['avg_duration'] if row and row['avg_duration'] else None
    
    @staticmethod
    def delete_all(user_id):
        """Delete all sleep records for a user."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM sleep_records WHERE user_id=?', (user_id,))
            deleted_count = cursor.rowcount
            conn.commit()
            return deleted_count

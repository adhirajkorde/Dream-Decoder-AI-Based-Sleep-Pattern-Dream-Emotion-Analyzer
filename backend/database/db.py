"""
Dream Decoder - Database Setup and Initialization
"""
import sqlite3
import os
from backend.config import DATABASE_PATH


from contextlib import contextmanager

@contextmanager
def get_db_connection():
    """Get a database connection with row factory enabled as a context manager."""
    # Ensure data directory exists
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


def init_db():
    """Initialize the database with required tables if they don't exist."""
    db_exists = os.path.exists(DATABASE_PATH)
    
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        if db_exists:
            # Quick check if tables actually exist
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='dreams'")
            if cursor.fetchone():
                # print("✅ Database already initialized.")
                return

        # Dreams table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dreams (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                sentiment TEXT,
                sentiment_score REAL,
                primary_emotion TEXT,
                emotion_scores TEXT,
                keywords TEXT,
                entities TEXT,
                interpretation TEXT
            )
        ''')
        
        # Sleep records table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sleep_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date DATE NOT NULL,
                duration_hours REAL NOT NULL,
                wakeups INTEGER DEFAULT 0,
                quality_rating INTEGER,
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
    print("✅ Database initialized successfully!")


if __name__ == '__main__':
    init_db()

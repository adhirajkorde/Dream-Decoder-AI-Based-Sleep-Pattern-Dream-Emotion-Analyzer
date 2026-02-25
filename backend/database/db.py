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
                # Check if users table exists (for migration)
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
                if not cursor.fetchone():
                    print("Migrating database to add authentication...")
                    # Add users table
                    _create_users_table(cursor)
                    # Migrate existing tables
                    _migrate_existing_tables(cursor)
                    conn.commit()
                    print("Database migration completed!")
                else:
                    # print("Database already initialized.")
                    pass
                return

        # Create all tables from scratch
        _create_users_table(cursor)
        _create_dreams_table(cursor)
        _create_sleep_records_table(cursor)
        
        conn.commit()
    print("Database initialized successfully!")


def _create_users_table(cursor):
    """Create users table."""
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            language_preference TEXT DEFAULT 'en',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')


def _create_dreams_table(cursor):
    """Create dreams table with user_id foreign key."""
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dreams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            sentiment TEXT,
            sentiment_score REAL,
            primary_emotion TEXT,
            emotion_scores TEXT,
            keywords TEXT,
            entities TEXT,
            interpretation TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    ''')


def _create_sleep_records_table(cursor):
    """Create sleep records table with user_id foreign key."""
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sleep_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            date DATE NOT NULL,
            duration_hours REAL NOT NULL,
            wakeups INTEGER DEFAULT 0,
            quality_rating INTEGER,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    ''')


def _migrate_existing_tables(cursor):
    """Migrate existing tables to add user_id column."""
    # Create a default user for existing data
    cursor.execute('''
        INSERT INTO users (username, email, password_hash, language_preference)
        VALUES (?, ?, ?, ?)
    ''', ('default_user', 'default@dreamdecoder.local', 
          '$2b$12$defaulthashforexistingdata', 'en'))
    
    default_user_id = cursor.lastrowid
    
    # Check if dreams table needs migration
    cursor.execute("PRAGMA table_info(dreams)")
    columns = [col[1] for col in cursor.fetchall()]
    
    if 'user_id' not in columns:
        # Backup existing dreams
        cursor.execute('''
            CREATE TABLE dreams_backup AS SELECT * FROM dreams
        ''')
        
        # Drop old table
        cursor.execute('DROP TABLE dreams')
        
        # Create new table with user_id
        _create_dreams_table(cursor)
        
        # Migrate data
        cursor.execute(f'''
            INSERT INTO dreams (user_id, content, created_at, sentiment, sentiment_score,
                              primary_emotion, emotion_scores, keywords, entities, interpretation)
            SELECT {default_user_id}, content, created_at, sentiment, sentiment_score,
                   primary_emotion, emotion_scores, keywords, entities, interpretation
            FROM dreams_backup
        ''')
        
        # Drop backup
        cursor.execute('DROP TABLE dreams_backup')
    
    # Check if sleep_records table needs migration
    cursor.execute("PRAGMA table_info(sleep_records)")
    columns = [col[1] for col in cursor.fetchall()]
    
    if 'user_id' not in columns:
        # Backup existing sleep records
        cursor.execute('''
            CREATE TABLE sleep_records_backup AS SELECT * FROM sleep_records
        ''')
        
        # Drop old table
        cursor.execute('DROP TABLE sleep_records')
        
        # Create new table with user_id
        _create_sleep_records_table(cursor)
        
        # Migrate data
        cursor.execute(f'''
            INSERT INTO sleep_records (user_id, date, duration_hours, wakeups,
                                      quality_rating, notes, created_at)
            SELECT {default_user_id}, date, duration_hours, wakeups,
                   quality_rating, notes, created_at
            FROM sleep_records_backup
        ''')
        
        # Drop backup
        cursor.execute('DROP TABLE sleep_records_backup')


if __name__ == '__main__':
    init_db()


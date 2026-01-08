import psycopg2
import os
from psycopg2.extras import RealDictCursor

# Database connection parameters
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', 'portfolio_db')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'postgres')
DB_PORT = os.environ.get('DB_PORT', '5432')

def update_database_schema():
    """Update the database schema to include missing columns"""
    conn = None
    cursor = None
    
    try:
        # Connect to the database
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        # Add the url column to certifications table if it doesn't exist
        cursor.execute("""
            DO $$
            BEGIN
                IF NOT EXISTS (SELECT 1 FROM information_schema.columns 
                               WHERE table_name='certifications' AND column_name='url') THEN
                    ALTER TABLE certifications ADD COLUMN url VARCHAR(500);
                END IF;
            END $$;
        """)
        
        # Add other missing columns for other tables if needed
        # Add features column to services table if it doesn't exist
        cursor.execute("""
            DO $$
            BEGIN
                IF NOT EXISTS (SELECT 1 FROM information_schema.columns 
                               WHERE table_name='services' AND column_name='features') THEN
                    ALTER TABLE services ADD COLUMN features TEXT[];
                END IF;
            END $$;
        """)
        
        # Add icon column to services table if it doesn't exist
        cursor.execute("""
            DO $$
            BEGIN
                IF NOT EXISTS (SELECT 1 FROM information_schema.columns 
                               WHERE table_name='services' AND column_name='icon') THEN
                    ALTER TABLE services ADD COLUMN icon VARCHAR(100);
                END IF;
            END $$;
        """)
        
        conn.commit()
        print("Database schema updated successfully!")
        
    except Exception as e:
        print(f"Error updating database schema: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    update_database_schema()
from app import create_app, db
from app.models import *
import os

# Create the Flask app
app = create_app()

def create_tables():
    with app.app_context():
        # Create all tables
        db.create_all()
        print("Tables created successfully!")

if __name__ == '__main__':
    create_tables()
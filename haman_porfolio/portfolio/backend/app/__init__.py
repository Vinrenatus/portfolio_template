from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from app.models import db
import os
import json
from datetime import datetime, date
from decimal import Decimal


class DateTimeEncoder(json.JSONEncoder):
    """Custom JSON encoder to handle datetime and other non-serializable objects"""
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        elif isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


def create_app():
    app = Flask(__name__)

    # Configuration for production
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@localhost/portfolio_db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

    # Set custom JSON encoder
    app.json_encoder = DateTimeEncoder

    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)

    # Enable CORS for all routes - allow frontend from port 3000
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:3000", "http://127.0.0.1:3000", "http://0.0.0.0:3000", os.environ.get('FRONTEND_URL', '*')]
        }
    })

    # Initialize API
    api = Api(app)

    # Import and register API routes
    from app.api import register_routes
    register_routes(api)

    return app

import jwt
from functools import wraps
from flask import request, jsonify
from datetime import datetime, timedelta
import os
from werkzeug.security import check_password_hash, generate_password_hash
from app.models import AdminUser, db


def generate_token(email):
    """Generate JWT token for admin user"""
    payload = {
        'email': email,
        'exp': datetime.utcnow() + timedelta(days=30),  # Token expires in 30 days
        'iat': datetime.utcnow()
    }
    secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')
    return jwt.encode(payload, secret_key, algorithm='HS256')


def verify_token(token):
    """Verify JWT token and return email if valid"""
    try:
        secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload['email']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def admin_required(f):
    """Decorator to require admin authentication"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(" ")[1]  # Bearer <token>
            except IndexError:
                return {'message': 'Invalid token format'}, 401

        if not token:
            return {'message': 'Token is missing'}, 401

        email = verify_token(token)
        if not email:
            return {'message': 'Token is invalid'}, 401

        # Check if the user exists and is active
        admin_user = AdminUser.query.filter_by(email=email, is_active=True).first()
        if not admin_user:
            return {'message': 'Access denied. Admin privileges required.'}, 403

        return f(*args, **kwargs)

    return decorated_function


def authenticate_user(email, password):
    """Authenticate admin user"""
    admin_user = AdminUser.query.filter_by(email=email).first()
    if admin_user and admin_user.is_active and admin_user.check_password(password):
        # Update last login time
        admin_user.last_login = datetime.utcnow()
        db.session.commit()
        return True
    return False


def create_admin_user(email, password):
    """Create a new admin user with hashed password"""
    password_hash = generate_password_hash(password)
    admin_user = AdminUser(email=email, password_hash=password_hash)
    db.session.add(admin_user)
    db.session.commit()
    return admin_user
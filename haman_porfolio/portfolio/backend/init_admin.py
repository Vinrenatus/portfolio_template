#!/usr/bin/env python
"""
Admin user initialization script
"""

from app import create_app
from app.models import db, AdminUser
from app.utils.auth import create_admin_user
import os

def init_admin_user():
    app = create_app()
    
    with app.app_context():
        # Check if an admin user already exists
        existing_admin = AdminUser.query.first()
        
        if not existing_admin:
            # Get admin credentials from environment or use defaults
            admin_email = os.environ.get('ADMIN_EMAIL', 'admin@example.com')
            admin_password = os.environ.get('ADMIN_PASSWORD', 'default_password')
            
            print(f"Creating admin user with email: {admin_email}")
            create_admin_user(admin_email, admin_password)
            print("Admin user created successfully!")
        else:
            print(f"Admin user already exists: {repr(existing_admin)}")

if __name__ == "__main__":
    init_admin_user()

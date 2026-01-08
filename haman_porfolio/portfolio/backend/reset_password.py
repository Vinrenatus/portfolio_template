#!/usr/bin/env python
"""
Reset admin password script
"""

from app import create_app
from app.models import db, AdminUser
from werkzeug.security import generate_password_hash

def reset_admin_password():
    app = create_app()

    with app.app_context():
        # Find the admin user
        admin_user = AdminUser.query.filter_by(email="admin@example.com").first()
        
        if admin_user:
            # Reset the password to a known value
            new_password = "admin123"
            admin_user.password_hash = generate_password_hash(new_password)
            db.session.commit()
            print(f"Password reset for admin user: {admin_user.email}")
            print(f"New password: {new_password}")
        else:
            print("No admin user found!")

if __name__ == "__main__":
    reset_admin_password()

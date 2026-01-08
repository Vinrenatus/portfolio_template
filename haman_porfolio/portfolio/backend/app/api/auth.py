from flask_restful import Resource
from flask import request, jsonify
from app.utils.auth import authenticate_user, generate_token
from app.models import AdminUser


class AuthAPI(Resource):
    def post(self):
        """Handle admin login"""
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if authenticate_user(email, password):
            token = generate_token(email)
            return {
                'message': 'Login successful',
                'token': token,
                'email': email
            }, 200
        else:
            return {'message': 'Invalid credentials'}, 401

    def get(self):
        """Get admin user information"""
        # This would typically require admin authentication to access
        # For demonstration purposes, we'll return a representation of the admin user
        # if they exist
        admin_user = AdminUser.query.first()
        if admin_user:
            return {
                'admin_info': repr(admin_user)
            }, 200
        else:
            return {'message': 'No admin user found'}, 404
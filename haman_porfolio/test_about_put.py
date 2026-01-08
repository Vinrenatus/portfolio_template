#!/usr/bin/env python3
import requests
import json

BASE_URL = "http://localhost:5000"

def test_about_get():
    print("Testing GET /api/about...")
    response = requests.get(f"{BASE_URL}/api/about")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    print()

def test_about_put():
    print("Testing PUT /api/about...")
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_ADMIN_TOKEN_HERE"
    }
    
    data = {
        "about": "Updated about me information for testing purposes."
    }
    
    try:
        response = requests.put(f"{BASE_URL}/api/about", headers=headers, json=data)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
    except requests.exceptions.ConnectionError:
        print("Could not connect to server. Make sure the Flask app is running.")
    except Exception as e:
        print(f"Error: {str(e)}")
    
    print()

if __name__ == "__main__":
    print("Testing AboutAPI endpoints...")
    test_about_get()
    test_about_put()

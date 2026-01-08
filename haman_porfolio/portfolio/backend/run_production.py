import os
from app import create_app

# Create the Flask app
app = create_app()

if __name__ == "__main__":
    # Production settings
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "False").lower() == "true"
    
    # In production, bind to all interfaces
    app.run(
        host="0.0.0.0",  # Bind to all interfaces in production
        port=port,
        debug=debug,
        threaded=True  # Enable threading for concurrent requests
    )
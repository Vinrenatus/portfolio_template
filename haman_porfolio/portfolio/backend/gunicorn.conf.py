# Gunicorn configuration file
bind = "0.0.0.0:5000"
workers = 4  # Number of worker processes
worker_class = "sync"  # Synchronous workers
worker_connections = 1000  # Max simultaneous connections per worker
timeout = 120  # Request timeout in seconds
keepalive = 5  # Keep-alive time for connections
max_requests = 1000  # Restart workers after this many requests
max_requests_jitter = 100  # Add jitter to max_requests
preload_app = True  # Preload application code
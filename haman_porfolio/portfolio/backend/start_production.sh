#!/bin/bash
# Production startup script

# Activate virtual environment
source venv/bin/activate

# Install production requirements
pip install -r requirements_prod.txt

# Start the application with Gunicorn
exec gunicorn --config gunicorn.conf.py run:app
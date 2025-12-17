#!/bin/bash
# Startup script for Railway deployment

# Use PORT from environment, default to 8000 if not set
PORT=${PORT:-8000}

# Start uvicorn
exec uvicorn api.main:app --host 0.0.0.0 --port $PORT

#!/bin/bash
# Activate the virtual environment if any
source venv/bin/activate

# Export environment variables (for Linux/Mac users)
export $(cat .env | xargs)

# Run the FastAPI application with Uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

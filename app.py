#!/usr/bin/env python3

"""
OpenTimeTracker API backend application.

This module initializes and starts the OpenTimeTracker backend application.

Usage:
    gunicorn app:app
"""

from fastapi import FastAPI
from backend.api import api_router # pylint: disable=no-name-in-module, import-error

app = FastAPI()

app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000) # nosec B104

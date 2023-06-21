#!/usr/bin/env python3

"""
API module for the OpenTimeTracker backend application.

This module contains the API endpoints and their respective models.
"""

from fastapi import APIRouter

# from backend.api.endpoints import users, projects, tasks, time_entries
from .endpoints import users

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
# api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
# api_router.include_router(time_entries.router, prefix="/time_entries", tags=["time_entries"])

@api_router.get("/")
def read_root():
    """Display API Hello World."""

    return {"status": "ok", "message": "OpenTimeTracker API"}

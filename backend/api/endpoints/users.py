#!/usr/bin/env python3

"""
Users endpoint for the OpenTimeTracker backend application.
"""

from fastapi import APIRouter
from ...models.user import UserModel
from ...utils.database import DatabaseConnector


# Create a new APIRouter instance
router = APIRouter()

# Create an instance of the DatabaseConnector
database = DatabaseConnector(host="localhost", port=5432, username="your_username", password="your_password", database="your_database")

# Connect to the database
database.connect()

def get_users():
    """Returns a dict of all users."""

    # Create an empty dict to store the users
    users = {}

    # Execute a SQL query to retrieve user data
    sql_query = "SELECT id, name, email FROM users"
    query_result = database.query(sql_query)

    # Process the query result using the UserModel class
    for row in query_result:
        user_id, name, email, clocked_in, status = row
        user = UserModel(user_id=user_id, name=name, email=email,
                        clocked_in=clocked_in, status=status)

        # Add the user to the list of users
        users[user_id] = user
    # Return the list of users
    return users

@router.get("/")
def read_users():
    """Returns a list of all users."""

    response = {
        "status": "ok",
        "message": "Users retrieved successfully.",
        "data": get_users()
    }

    return response

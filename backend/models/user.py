#!/usr/bin/env python3

"""
User model for the OpenTimeTracker backend application.
"""

from json import JSONEncoder

class UserModel():
    """
    Represents a user in the OpenTimeTracker application.

    Attributes:
        id (int): User ID.
        name (str): User name.
        email (str): User email address.

    Methods:
        __init__(id: int, name: str, email: str): Initializes a new UserModel object.
        save(): Saves the user's data to the database.
        update(): Updates the user's data in the database.
        delete(): Deletes the user's data from the database.
    """

    def __init__(self, user_id: int, name: str, email: str, clocked_in: bool, status: str):
        """
        Initializes a new UserModel object.
        
        Args:
            id (int): User ID.
            name (str): User name.
            email (str): User email address.
        """

        self.user_id = user_id
        self.name = name
        self.email = email
        self.clocked_in = clocked_in
        self.status = status

    def __iter__(self):
        """
        Returns an iterator for the UserModel object.

        Returns:
            iter: An iterator for the UserModel object.
        """

        return iter(self.__dict__)

    def save(self):
        """
        Saves the user's data to the database.
        """

        pass

    def update(self):
        """
        Updates the user's data in the database.
        """

        pass

    def delete(self):
        """
        Deletes the user's data from the database.
        """

        pass

class UserEncoder(JSONEncoder):
    """
    UserEncoder class provides methods for encoding a UserModel object to JSON.
    """

    def default(self, o):
        """
        Encodes a UserModel object to JSON.

        Args:
            o (UserModel): The UserModel object to encode.

        Returns:
            str: The JSON-encoded UserModel object.
        """

        return o.__dict__

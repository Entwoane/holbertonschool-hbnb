#!/usr/bin/python3
""" Defining the aminity class, its attributes and relationships """


import uuid
from datetime import datetime

class Amenity:
    def __init__(self, name: str):
        if len(name) > 50:
            raise ValueError("Equipment name must not exceed 50 characters")

        # Generate a unique ID
        self.id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def update(self, new_name):
        """ Update equipment name """
        if not isinstance(new_name, str):
            raise TypeError("new_name must be a string")
        
        if len(new_name) > 50:
            raise ValueError("Equipment name must not exceed 50 characters")

        self.name = new_name
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Convert the object into a JSON serializable dictionary """
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    def __str__(self):
        return f"Amenity(id={self.id}, name={self.name}, created_at={self.created_at}, updated_at={self.updated_at})"

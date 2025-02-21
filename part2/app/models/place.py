#!/usr/bin/python3
""" Define Class Place """


import re
import uuid
from datetime import datetime

class place:
    def __init__(self, title, description, price, latitude, longitude, owner):
        # Generate a unique ID
        self.id = str(uuid.uuid4())

        # Field Check
        self.title = self.validate_title(title, "name")
        self.description = str(description)
        self.price = (price)
        self.latitude = (latitude)
        self.longitude = (longitude)

        self.owner = owner
        self.created_at = datetime.now
        self.updated_at = datetime.now
#!/usr/bin/python3
""" Define Class Place """


import uuid
from datetime import datetime

class place:
    def __init__(self, title, description, price, latitude, longitude, owner):
        # Generate a unique ID
        self.id = str(uuid.uuid4())

        # Field Check
        self.title = self.validate_title(title)
        self.description = description if description else ""
        self.price = self.validate_price(price)
        self.latitude = self.validate_latitude(latitude)
        self.longitude = self.validate_longitude(longitude)
        self.owner = self.validate_owner(owner)
        self.created_at = datetime.now
        self.updated_at = self.created_at

    def validate_title(self, title):
        """ Validate Title """
        if not title or len(title) > 100:
            raise ValueError("The title is mandatory and must not exceed 100 characters.")
        return title

    def validate_price(self, price):
        """ Validate Price """
        if price < 0:
            raise ValueError("The price must be a positive value.")
        return price

    def validate_latitude(self, latitude):
        """ Validate Latitude """
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be between -90.0 and 90.0.")
        return latitude

    def validate_longitude(self, longitude):
        """ Validate Longitude """
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0")
        return longitude

    def validate_owner(self, owner):
        """ Validates the owner's existence """
        if not owner:
            raise ValueError("A valid owner is required.")
        return owner

    def update(self, **kwargs):
        """ Updates location attributes and timestamp """
        for key, value in kwargs.items():
            if hasattr(self, key) and key != "id" and key != "created_at":
                setattr(self, key, value)
        self.updated_at = datetime.now()

    def __str__(self):
        return f"{self.title} - {self.price}€/night, {self.latitude}, {self.longitude} (Owner: {self.owner})"

#!/usr/bin/python3
""" Defining the place class, its attributes and relationships """

import uuid
from datetime import datetime
from app.models.review import Review
from app.models.user import User

class Place:
    def __init__(self, id, title, price, latitude, longitude, owner_id, description=None):
        """ Initialization of a location with input validation """
        super().__init__()

        self.id = id

        # Field Check
        self.title = self.validate_title(title)
        self.description = description if description else ""
        self.price = self.validate_price(price)
        self.latitude = self.validate_latitude(latitude)
        self.longitude = self.validate_longitude(longitude)
        self.owner_id = self.validate_owner(owner_id)
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        # Relations
        self.amenities = []  # Equipment list
        self.reviews = []  # List of reviews associated with this location

        # Recover owner object
        owner = self.get_owner(owner_id)
        if owner:
            owner.add_place(self)  # Add this location to the owner's list

    def get_owner(self, owner_id):
        """ Récupérer l'objet User correspondant à owner_id """
        owner = User.query.filter_by(id=owner_id).first()
        if not owner:
            raise ValueError("Owner not found")
        return owner

    def add_aminity(self, aminity):
        """ Associate an amenity with this location """
        from app.models.amenity import Amenity
        if isinstance(aminity, Amenity):
            self.amenities.append(aminity)
        else:
            raise TypeError("The object added must be an instance of Amenity")

    def add_review(self, review):
        """ Associates a review with this location """
        if isinstance(review, Review):
            self.reviews.append(review)
            review.place = self  # Associate review with this location
        else:
            raise TypeError("The object added must be an instance of Review")

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

    def validate_owner(self, owner_id):
        """ Validates the owner's existence """
        if not owner_id:
            raise ValueError("A valid owner is required.")
        return owner_id

    def update(self, **kwargs):
        """ Updates location attributes and timestamp """
        for key, value in kwargs.items():
            if hasattr(self, key) and key not in ["id", "created_at"]:
                setattr(self, key, value)
        self.updated_at = datetime.now()

    def __str__(self):
        return f"{self.title} - {self.price}€/night, {self.latitude}, {self.longitude} (Owner ID: {self.owner_id})"

from .basemodel import BaseModel
from .user import User
from app.db import db

place_amenity = db.Table(
    'place_amenity',
    db.Column('place_id', db.Integer, db.ForeignKey('place.id'), primary_key=True),
    db.Column('amenity_id', db.Integer, db.ForeignKey('amenity.id'), primary_key=True)
    )

class Place(BaseModel):
    __tablename__ = 'places'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    amenities = db.relationship('Amenity', secondary='place_amenity', lazy=db.subquery, backref=db.backref('places', lazy=True))
    
    user_id = db.relationship('User', backref='places')
    reviews = db.relationship('Review', backref='places')

    def __init__(self, title: str, price: float, latitude: str, longitude, owner, description=None):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty")
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        super().is_max_length('title', value, 100)
        self.__title = value

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError("Price must be a float")
        if value < 0:
            raise ValueError("Price must be positive.")
        self.__price = value

    @property
    def latitude(self):
        return self.__latitude
    
    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, float):
            raise TypeError("Latitude must be a float")
        super().is_between("latitude", value, -90, 90)
        self.__latitude = value
    
    @property
    def longitude(self):
        return self.__longitude
    
    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, float):
            raise TypeError("Longitude must be a float")
        super().is_between("longitude", value, -180, 180)
        self.__longitude = value

    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise TypeError("Owner must be a user instance")
        self.__owner = value

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)
    
    def delete_review(self, review):
        """Add an amenity to the place."""
        self.reviews.remove(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner.id
        }
    
    def to_dict_list(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner': self.owner.to_dict(),
            'amenities': self.amenities,
            'reviews': self.reviews
        }

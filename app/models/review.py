from .basemodel import BaseModel
from .place import Place
from .user import User
from app.db import db

class Review(BaseModel):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(128), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('places.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    place = db.relationship('Place', back_populates='reviews', lazy=True)
    user = db.relationship('User', back_populates='reviews', lazy=True)

    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
    
    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self, value):
        if not value:
            raise ValueError("Text cannot be empty")
        if not isinstance(value, str):
            raise TypeError("Text must be a string")
        self.__text = value

    @property
    def rating(self):
        return self.__rating
    
    @rating.setter
    def rating(self, value):
        if not isinstance(value, int):
            raise TypeError("Rating must be an integer")
        super().is_between('Rating', value, 1, 6)
        self.__rating = value

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
            'place_id': self.place.id,
            'user_id': self.user.id
        }

from .basemodel import BaseModel
from app.db import db

class Amenity(BaseModel):
    __tablename__ = 'amenities'
    
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(64))

    def __init__(self, name):
        super().__init__()	
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not value:
            raise ValueError("Name cannot be empty")
        super().is_max_length('Name', value, 50)
        self._name = value

    def update(self, data):
        return super().update(data)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

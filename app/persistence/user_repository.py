from app.models.user import User
from app.db import db
from app.persistence.repository import SQLAlchemyRepository
from flask_sqlalchemy import SQLAlchemy


class UserRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(User)

    def get_user_by_email(self, email):
        return self.model.query.filter_by(email=email).first()
    
    def get_user_by_username(self, username):
        return self.model.query.filter_by(username=username).first()
    
    def get_users_by_role(self, role):
        return User.query.filter_by(role=role).all()
    
    def get_all_users(self, users):
        return self.model.query.all()
    
    def deactivate_user(self, user_id):
        user = self.get_by_attribute(user_id)
        if user:
            user.is_active = False
            db.session.commit()
            return True
        return False
    
    def authenticate_user(self, email, password):
        user = self.get_user_by_email(email)
        if user and user.verify_password(password):
            return user
        return None

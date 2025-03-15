import os
basedir = os.path.abspath(os.path.dirname(__file__)) #Absent sur le guide


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True #True selon le guide
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "hbnb_database.db")}'#SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db' selon le guide
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

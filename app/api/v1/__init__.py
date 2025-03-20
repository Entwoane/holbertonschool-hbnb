from flask import Blueprint

blueprint = Blueprint('api_v1', __name__, url_prefix='/api/v1')

# Import routes after blueprint is defined
from . import users

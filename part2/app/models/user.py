#!/usr/bin/python3
"""Define class user"""


import re
import uuid
from datetime import datetime

class user:
    def __init__(self, first_name, last_name, email, is_admin=False):
        self.id = str(uuid.uuid4())
        self.first_name = self.validate_name(first_name, "Prénom")
        self.last_name = self.validate_name(last_name, "Nom de famille")
        self.email = self.validate_email(email)
        self.is_admin = is_admin
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
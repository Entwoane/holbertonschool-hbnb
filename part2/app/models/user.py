#!/usr/bin/python3
"""Define class user"""


import uuid
from datetime import datetime

class user:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.first_name = str()
        self.last_name = str()
        self.email = str()
        self.is_admin = ()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
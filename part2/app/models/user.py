#!/usr/bin/python3
"""Define class user"""


import re
import uuid
from datetime import datetime

class User:
    def __init__(self, first_name, last_name, email, is_admin=False):
        # Generate a unique ID
        self.id = str(uuid.uuid4())

        # Field checks
        self.first_name = self.validate_name(first_name, "first name")
        self.last_name = self.validate_name(last_name, "last name")
        self.email = self.validate_email(email)

        self.is_admin = is_admin
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @staticmethod
    def validate_name(name, field_name):
        """ Checks that the name is a string of max 50 characters. """
        if not isinstance(name, str) or len(name) > 50:
            raise ValueError(f"{field_name} must be a string of max 50 characters.")
        return name.strip()

    @staticmethod
    def validate_email(email):
        """ Checks that the email is valid. """
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-9-.]+$"
        if not re.match(pattern, email):
            raise ValueError("Invalid e-mail address.")
        return email.strip().lower()

    def update(self, first_name=None, last_name=None, email=None, is_admin=None):
        """ Updates user information. """
        if first_name:
            self.first_name = self.validate_name(first_name, "first name")
        if last_name:
            self.last_name = self.validate_name(last_name, "last name")
        if email:
            self.email = self.validate_email(email)
        if is_admin is not None:
            self.is_admin = is_admin

        self.update_at = datetime.now()

    def show_info(self):
        """ Displays user information. """
        return (f"ID: {self.id}\n"
                f"Name: {self.first_name} {self.last_name}\n"
                f"Email: {self.email}\n"
                f"Admin: {'Yes' if self.is_admin else 'No'}\n"
                f"Created_at: {self.created_at}\n"
                f"Update_at: {self.update_at}")

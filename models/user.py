#!/usr/bin/python3
"""
User Class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This is a user class, a derived class of BaseModel class

    Attributes:
        email
        password
        firstname
        lastname
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

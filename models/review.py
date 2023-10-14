#!/usr/bin/python3
"""
Review Class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This is a Review class, a derived class of BaseModel class

    Attributes:
        place_id
        user_id
        text
    """

    place_id = ""
    user_id = ""
    text = ""

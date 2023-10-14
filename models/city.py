#!/usr/bin/python3
"""
City Class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This is a City class, a derived class of BaseModel class

    Attributes:
        state_id
        name
    """

    state_id = ""
    name = ""

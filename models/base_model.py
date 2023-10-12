#!/usr/bin/python3
"""
The Base model for the AirBnB
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    The base model of all other classes
    """

    def __init__(self):
        """
        Initialization of the BaseModel class

        Attributes:
            Public Instance attributes
            id - assign with an uuid when an instance is created
            created_at - The current datetime when an instance is created
            updated_at - The current datetime when an instance is updated
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        The modified str for BaseModel

        Return:
            The String
        """

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        A public instance methods that updates the public instance attribute
        with the current datetime
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        A public instance methods that returns a dictionary
        containing all keys/values of the instance
        """

        dicto = self.__dict__.copy()
        dicto["__class__"] = self.__class__.__name__
        dicto["created_at"] = self.created_at.isoformat()
        dicto["updated_at"] = self.updated_at.isoformat()
        return dicto




















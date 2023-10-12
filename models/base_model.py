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

    def __init__(self, *args, **kwargs):
        """
        Initialization of the BaseModel class

        Attributes:
            Public Instance attributes
            args: Arguments(list)
            kwargs: Key worded arguments(dict)
            id: Assign with an uuid when an instance is created
            created_at: The current datetime when an instance is created
            updated_at: The current datetime when an instance is updated
        """

        if len(kwargs) > 0:
            timeformat = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(kwargs[key], timeformat)
                if key != "__class__":
                    setattr(self, key, value)
        else:
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




















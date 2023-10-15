#!/usr/bin/python3
"""
Unittest for the BaseModel class
"""

import json
import models
import os
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class
    """
    model = BaseModel()

    def test_init(self):
        """
        Test the initialization of the base model
        """

        model = BaseModel()
        self.model.name = "My Model"
        self.model.my_number = 9
        self.model.save()
        model_json = self.model.to_dict()

        self.assertEqual(self.model.name, model_json["name"])
        self.assertEqual(self.model.my_number, model_json["my_number"])
        self.assertEqual("BaseModel", model_json["__class__"])
        self.assertEqual(self.model.id, model_json["id"])

    def test_str(self):
        """
        Test the _str__ method of BaseModel
        """
        
        model = BaseModel()
        model1 = model.id
        model2 = model.__dict__
        self.assertEqual(str(model), "[BaseModel] ({}) {}".format(model1, model2))

    def test_save(self):
        """
        Test the save method of BaseModel
        """

        model = BaseModel()
        previous_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(previous_updated_at, model.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel
        """

        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["id"], model.id)
        self.assertEqual(model_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], model.updated_at.isoformat())
        self.assertEqual(model_dict["__class__"], "BaseModel")


if __name__ == "__main__":
    unittest.main()

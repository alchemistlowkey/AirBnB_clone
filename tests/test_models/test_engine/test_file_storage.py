#!/usr/bin/python3
"""
Test suite for FileStorage
"""

import json
import os
import unittest
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    """
    Test cases for FileStorage class
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup class for the testing environment
        """
        cls.storage = FileStorage()

    def tearDown(self):
        """
        Teardown class for the clean up after each test
        """
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        """
        Test the all method
        """
        all_obj = self.storage.all()
        self.assertIsInstance(all_obj, dict)

    def test_new(self):
        """
        Test the new method
        """
        new_obj = BaseModel()
        self.storage.new(new_obj)
        self.assertTrue("BaseModel.{}".format(new_obj.id) in self.storage.all())

    def test_save_reload(self):
        """
        Test the save and reload methods
        """
        new_obj = BaseModel()
        self.storage.new(new_obj)

        new_storage = FileStorage()
        new_storage.reload()

        loaded_objects = new_storage.all()
        self.assertTrue("BaseModel.{}".format(new_obj.id) in loaded_objects)
        loaded_model = loaded_objects["BaseModel.{}".format(new_obj.id)]
        self.assertEqual(loaded_model.id, new_obj.id)
        self.assertEqual(loaded_model.created_at, new_obj.created_at)

    def test_reload(self):
        """
        Test reloading with an unrecognized class name
        """
        obj = {
            "BaseModel.1234": {
                "__class__": "BaseModel",
                "id": "1234"
            }
        }
        with open(FileStorage._FileStorage__file_path, 'w') as file:
            json.dump(obj, file)

        self.storage.reload()

        loaded_obj = self.storage.all()
        self.assertTrue("BaseModel.1234" in loaded_obj)
        loaded_model = loaded_obj["BaseModel.1234"]
        self.assertIsInstance(loaded_model, BaseModel)
        self.assertEqual(loaded_model.id, "1234")


if __name__ == "__main__":
    unittest.main()

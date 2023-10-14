#!/usr/bin/python3
"""
File Storage class
"""
import json
from os.path import exists


class FileStorage:
    """
    A class that serializes/deserializes instances to a JSON file viz-a-vis
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """

        serial_json = {}
        for key, value in FileStorage.__objects.items():
            serial_json[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(serial_json, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """

        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        class_names = {
                "BaseModel": BaseModel,
                "User": User,
                "Place": Place,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review,
                }

        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                load_file = json.load(f)
                for key, value in load_file.items():
                    name = value["__class__"]
                    FileStorage.__objects[key] = class_names[name](**value)

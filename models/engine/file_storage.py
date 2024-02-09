#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    @classmethod
    def all(cls):
        """Return the dictionary __objects."""
        return cls.__objects

    @classmethod
    def new(cls, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        cls.__objects[key] = obj

    @classmethod
    def save(cls):
        """Serialize __objects to the JSON file __file_path."""
        objdict = {key: obj.to_dict() for key, obj in cls.__objects.items()}
        with open(cls.__file_path, "w") as f:
            json.dump(objdict, f)

    @classmethod
    def reload(cls):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(cls.__file_path) as f:
                objdict = json.load(f)
                for key, value in objdict.items():
                    cls_name = value["__class__"]
                    del value["__class__"]
                    cls.new(getattr(models, cls_name)(**value))
        except FileNotFoundError:
            return
        except json.JSONDecodeError:
            return
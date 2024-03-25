#!/usr/bin/python3
"""File storage class"""

import json
import os


class FileStorage:

    def __init__(self):
        """Initialize FileStorage"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objs = {}
        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objs, file)

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User

        classes = {"BaseModel": BaseModel,
                   "User": User
                   }
        return classes

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    theclassname, theid = key.split(".")
                    classname = eval(theclassname)
                    self.__objects[key] = classname(**value)

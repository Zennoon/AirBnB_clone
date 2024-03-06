#!/usr/bin/python3
"""
contains

classes:
    FileStorage - Responsible for serializing and deserializing
"""
import json


class FileStorage:
    """
    Serializes instances to a JSON file, and deserializes JSON strings to
    instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the __objects private attribute which contains the currently
        available instances.
        """
        return (FileStorage.__objects)

    def new(self, obj):
        """
        Inserts an instance in the __objects private attribute.

        Args:
            obj: The object to insert in the dictionary.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the instances in the __objects attributes and stores them in
        the file '__file_path'.
        """
        to_store = FileStorage.__objects.copy()
        for key in to_store.keys():
            to_store[key] = to_store[key].to_dict()
        with open(FileStorage.__file_path, 'wt', encoding="utf-8") as f:
            json.dump(to_store, f)

    def reload(self):
        """
        Deserializes the json file and inserts the instances to __objects.
        """
        try:
            with open(FileStorage.__file_path, "rt", encoding="utf-8") as f:
                from models.base_model import BaseModel
                FileStorage.__objects = {}
                stored_dict = json.load(f)
                for key in stored_dict.keys():
                    FileStorage.__objects[key] = BaseModel(**(stored_dict[key]))
        except FileNotFoundError:
            pass

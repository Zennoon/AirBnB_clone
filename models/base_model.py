#!/usr/bin/python3
"""
contains

classes:
    BaseModel - A base class to be inherited by the other models/classes of the
                project
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    Base class for other class to inherit from.
    """
    def __init__(self):
        """
        Initializes a newly created instance of the class.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns an informal representation of an instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute of an instance to the current time.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary of all necessary attributes of an instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return (obj_dict)

#!/usr/bin/python3
"""
contains

classes:
    BaseModel - A base class to be inherited by the other models/classes of the
                project
"""
from datetime import datetime
from models import storage
import uuid


class BaseModel:
    """
    Base class for other class to inherit from.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a newly created instance of the class.

        Args:
            args: tuple of positional arguments.
            kwargs: dictionary of keyword/named arguments.
        """
        if kwargs:
            for key in kwargs.keys():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        new_datetime = datetime.fromisoformat(kwargs[key])
                        self.__dict__[key] = new_datetime
                    else:
                        self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

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
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary of all necessary attributes of an instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return (obj_dict)

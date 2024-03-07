#!/usr/bin/python3
"""
contains

classes:
    User - Inherits from BaseModel, represents a user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user of the service, inherits from BaseModel.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

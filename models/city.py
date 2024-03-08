#!/usr/bin/python3
"""
contains

classes:
    City - represents a real-life city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a real-life city, inherits from BaseModel.
    """
    state_id = ""
    name = ""

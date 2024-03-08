#!/usr/bin/python3
"""
contains

classes:
    Amenity - represents an amenity of a place
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents some amenity (quality) of a place, inherits from BaseModel.
    """
    name = ""

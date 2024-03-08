#!/usr/bin/python3
"""
contains

classes:
    Review - represents a review left by a user
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review of a place left by a user, inherits from BaseModel.
    """
    place_id = ""
    user_id = ""
    text = ""

#!/usr/bin/python3
"""
contains

classes:
    State - Inherits from BaseModel, represents a real-life state
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a real-life state.
    """
    name = ""

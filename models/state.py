#!/usr/bin/python3
"""Contains the State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class to create state instance
    Args:
        BaseModel: Mother class
    Attributes:
        name: the state name"""

    name = ""

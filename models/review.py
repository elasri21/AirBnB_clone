#!/usr/bin/python3
"""Contains class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review to create review instances
    Args:
        BaseModel: Mother class
    Attributes:
        place_id: the place if
        user_id: the user id
        text: the review a user typed"""

    place_id = ""
    user_id = ""
    text = ""

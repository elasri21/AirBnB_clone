#!/usr/bin/python3
"""Contains Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """class Place to create place instances
    Args:
        BaseModel: Mother class
    Attributes:
        city_id: the city id
        user_id: the user id
        name: the lpace name
        description: place description
        number_rooms: the number of the rooms
        max_guest: the maximum number of guests
        price_by_night: the price of the room
        latitude: positive coords
        longitude: negative coords
        amenity_ids: the amenity ids"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = -0.0
    amenity_ids = []

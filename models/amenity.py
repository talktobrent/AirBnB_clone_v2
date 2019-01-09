#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import String, Integer, Column
import os

class Amenity(BaseModel):
    """This is the class for Amenity
    Attributes:
        name: input name
    """

    name = ""

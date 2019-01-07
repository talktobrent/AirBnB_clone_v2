#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
import os

class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """

    # declare tablename regardless ????? confirm
    __tablename__ = 'cities'

    # check if environmental variable from cmd, please confirm if state_id is correct
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    else:

        # original codebase
        state_id = ""
        name = ""

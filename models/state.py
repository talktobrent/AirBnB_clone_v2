#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = "states"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="state", cascade="all, delete-orphan")
    else:
        name = ""

    @property
    def cities(self):
        """ return list of all objects in storage"""
        return [v for k, v in models.storage.all() if self.id == v.state_id]

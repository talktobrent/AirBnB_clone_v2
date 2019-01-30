#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", passive_deletes=True, backref="states")
    else:
        name = ""

    @property
    def cities(self):
        """ return list of all city objects in storage"""
        return [v for k, v in models.storage.all(City).items()
                if self.id == v.state_id]

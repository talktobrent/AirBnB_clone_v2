#!/usr/bin/python3
"""This is the DBStorage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os


class DBStorage:
    """ Database storage class """

    __engine = None
    __session = None

    def __init__(self):
        """ initialization """

        engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                               os.getenv('HBNB_MYSQL_USER'),
                               os.getenv('HBNB_MYSQL_PWD'),
                               os.getenv('HBNB_MYSQL_HOST'),
                               os.getenv('HBNB_MYSQL_DB')),
                               pool_pre_ping=True)

        session = Session(engine)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=engine)

    def all(self, cls=None):
        """ get dictionary of all objects """

        if cls == None:
            return {"{}.{}".format(type(obj).__name__, obj.id): obj
                    for obj in self.__session.query(User, State,
                    City, Amenity, Place, Review).all()}

        return {"{}.{}".format(type(obj).__name__, obj.id): obj
                for obj in self.__session.query(cls).all()}

    def new(self, obj):
        """ insert new object in current database session """

        __session.add(obj)

    def save(self):
        """ commit changes to database """

        __session.commit()

    def delete(self, obj=None):
        """ delete from current database session """

        if obj:
            __session.delete(obj)

    def reload(self):
        """ reload database """






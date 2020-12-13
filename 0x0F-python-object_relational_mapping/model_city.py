#!/usr/bin/python3
"""
Contains the class definition of a City and an
instance Base = declarative_base()
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """ City class inherits forma base """
    __tablename__ = 'cities'

    id = Column(Integer,
                unique=True,
                primary_key=True,
                nullable=False,
                autoincrement="auto")
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)

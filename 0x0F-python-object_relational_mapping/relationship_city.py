#!/usr/bin/python3
''' first script using model for cities'''

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
        """ Class for table city """
        __tablename__ = 'cities'
        id = Column(Integer, unique=True, primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
        state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

#!/usr/bin/python3
''' first script using model for cities'''


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
        """ Class for table city """
        __tablename__ = 'cities'
        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
        state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

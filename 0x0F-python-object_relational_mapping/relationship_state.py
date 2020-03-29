#!/usr/bin/python3
'''model for states'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
        """ Class for table state  """
        __tablename__ = 'states'
        id = Column(Integer, primary_key=True)
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='State', cascade='all, delete')

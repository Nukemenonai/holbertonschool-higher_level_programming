#!/usr/bin/python3
''' first script using sqlalchemy'''


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
        """ Class for table city """
        __tablename__ = 'cities'
        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
        state_id = Column(Integer, nullable=False, ForeignKey('states'))

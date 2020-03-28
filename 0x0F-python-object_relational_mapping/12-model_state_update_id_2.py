#!/usr/bin/python3
""" This script lists all state object from database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy.sql import select
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(a,
                                                                       b,
                                                                       c),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    other_state = session.query(State).get(2)
    other_state.name = 'New Mexico'
    session.add(other_state)
    session.commit()

#!/usr/bin/python3
"""
City Relationship
"""

import sys
from relationship_state import Base, State
from relationship_city import City
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    scity = 'San Francisco'
    sstate = 'California'
    state = State(name=sstate)
    city = City(name=scity, state=state)
    session.add(city)
    session.commit()
    session.close()

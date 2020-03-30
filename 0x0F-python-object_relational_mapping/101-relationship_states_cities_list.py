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

    Session = sessionmaker(bind=engine)
    session = Session()
    q = session.query(State).outerjoin(City).order_by(State.id, City.id)
    a = q.all()
    for state in a:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print( "    {}: {}".format(city.id, city.name))

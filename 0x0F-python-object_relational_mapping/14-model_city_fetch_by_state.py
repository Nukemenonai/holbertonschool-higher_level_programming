#!/usr/bin/python3
""" This script lists all city objects from database hbtn_0e_14_usa"""

import sys
from model_state import Base, State
from model_city import City
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
    sq = session.query(State.name, City.id, City.name).\
        join(City, State.id == City.state_id).\
        order_by(City.id)
    res = sq.all()

    for row in res:
        print("{:s}: ({:d}) {:s}".format(*row))

    session.close()

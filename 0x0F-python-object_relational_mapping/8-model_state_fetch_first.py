#!/usr/bin/python3
""" This script lists first  object from database hbtn_0e_6_usa"""

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

    sq = session.query(State)
    res = sq.first()

    if res:
        print("{}: {}".format(res.id, res.name))
    else:
        print("Nothing")

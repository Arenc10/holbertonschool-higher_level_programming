#!/usr/bin/python3
"""Start link class to table in database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1],
                                  sys.argv[2],
                                  sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    for state in session.query(State).filter(State.id == 1).all():
        if state:
            print(f"{state.id}: {state.name}")
        print("Nothing")
    session.close()
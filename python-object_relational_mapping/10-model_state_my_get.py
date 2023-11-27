#!/usr/bin/python3
"""Prints the State object with the name passed as argument from hbtn_0e_6_usa database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}')

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.name == sys.argv[4]).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()

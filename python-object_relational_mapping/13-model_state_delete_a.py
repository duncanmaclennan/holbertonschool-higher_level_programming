#!/usr/bin/python3
"""
Script that deletes all State objects with a name contain the letter a from the
database hbtn_0e_6_usa
"""
import MySQLdb
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    new_state = State(name="Louisiana")
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    state_delete = session.query(State).filter(State.name.like("%a%")).all()
    for state in state_delete:
        session.delete(state)
    session.commit()
    session.close()

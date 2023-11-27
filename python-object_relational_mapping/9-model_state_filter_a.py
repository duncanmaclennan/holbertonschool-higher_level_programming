#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' from hbtn_0e_6_usa database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import State and Base

if __name__ == "__main__":
    # Create engine
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all States that contain 'a', sorted by id
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id)

    # Print states
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

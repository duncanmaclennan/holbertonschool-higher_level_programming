#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Create engine
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all cities joined with states, ordered by city id
    cities = session.query(City).options(
        joinedload(City.state)).order_by(City.id).all()

    # Print each city
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()

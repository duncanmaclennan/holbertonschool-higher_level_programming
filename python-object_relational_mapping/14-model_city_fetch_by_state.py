#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""
import MySQLdb
import sys
from sqlalchemy import create_engine
from model_city import Base, City
from model_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    city_print = session.query(City, State).join(State)
    for city, state in city_print:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()

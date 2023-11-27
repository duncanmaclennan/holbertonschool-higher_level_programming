#!/usr/bin/python3
"""
Scripts that lists all State objects that contain an 'a' from
the database hbtn_0e_6_usa
"""
import MySQLdb
import sys
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '%a%' \
                   ORDER BY id;")
    rows = cursor.fetchall()
    for row in rows:
        print("{}: {}".format(row[0], row[1]))
    cursor.close()
    database.close()

#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument from the
database hbtn_0e_6_usa
"""
import MySQLdb
import sys
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3])
    cursor = database.cursor()
    search_term = sys.argv[4]
    cursor.execute("SELECT id FROM states WHERE name LIKE %s ORDER BY id;",
                   (search_term,))
    rows = cursor.fetchall()
    if not rows:
        print("Not found")
    else:
        for row in rows:
            print("{}".format(row[0]))
    cursor.close()
    database.close()

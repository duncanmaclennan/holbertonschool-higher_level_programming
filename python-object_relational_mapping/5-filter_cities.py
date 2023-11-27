#!/usr/bin/python3
"""Lists all cities of a specified state from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":

    mydb = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3])

    cursorObj = mydb.cursor()

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """

    cursorObj.execute(query, (sys.argv[4],))

    myresult = cursorObj.fetchall()

    print(", ".join([city[0] for city in myresult]))

    cursorObj.close()
    mydb.close()

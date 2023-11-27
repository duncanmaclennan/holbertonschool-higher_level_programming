#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

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
    SELECT cities.id, cities.name, states.name 
    FROM cities 
    LEFT JOIN states ON cities.state_id = states.id 
    ORDER BY cities.id ASC
    """
    cursorObj.execute(query)

    myresult = cursorObj.fetchall()

    for row in myresult:
        print(row)
    cursorObj.close()
    mydb.close()

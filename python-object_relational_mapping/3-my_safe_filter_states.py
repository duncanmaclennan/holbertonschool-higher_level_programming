#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    # mydb is connection object
    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3])

    # cursorObj is object to execute queries
    cursorObj = mydb.cursor()

    query = "SELECT * FROM states WHERE BINARY name LIKE %s ORDER BY id ASC"
    name = (sys.argv[4],)

    # Execute SQL query to fetch all the states in the database
    cursorObj.execute(query, name)

    # Fetch all the rows and display them
    myresult = cursorObj.fetchall()

    for row in myresult:
        print(row)

    # shut cursor and database connection
    cursorObj.close()
    mydb.close()

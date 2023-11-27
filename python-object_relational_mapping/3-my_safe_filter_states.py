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

    # Prepared statement with placeholder for state name, limit to 1 result
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC LIMIT 1"

    # Execute the query with the state name as a parameter (safe from injection)
    cursorObj.execute(query, (sys.argv[4],))

    # Fetch the row and display it
    myresult = cursorObj.fetchone()

    if myresult:
        print(myresult)

    # shut cursor and database connection
    cursorObj.close()
    mydb.close()

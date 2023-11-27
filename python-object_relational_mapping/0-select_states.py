#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

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

    # cursor object execute SQL query but not return value
    cursorObj.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows and display them
    myresult = cursorObj.fetchall()

    for row in myresult:
        print(row)

    # shut cursor and database connection
    cursorObj.close()
    mydb.close()

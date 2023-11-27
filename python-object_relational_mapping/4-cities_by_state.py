#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

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

    # SQL query to fetch cities data
    query = """
    SELECT cities.id, cities.name, states.name 
    FROM cities 
    JOIN states ON cities.state_id = states.id 
    ORDER BY cities.id ASC
    """

    # Execute SQL query
    cursorObj.execute(query)

    # Fetch all the rows and display them
    myresult = cursorObj.fetchall()

    for row in myresult:
        print(row)

    # shut cursor and database connection
    cursorObj.close()
    mydb.close()

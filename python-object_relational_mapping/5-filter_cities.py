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

    # Prepared statement with placeholder for state name
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """

    # Execute the query with the state name as a parameter (safe from injection)
    cursorObj.execute(query, (sys.argv[4],))

    # Fetch all the rows
    myresult = cursorObj.fetchall()

    # Print the cities in one line, separated by commas
    print(", ".join([city[0] for city in myresult]))

    cursorObj.close()
    mydb.close()

#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all three required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <username> <password> <database>")
        sys.exit(1)

    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SQL query to retrieve states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch and print the results
        results = cursor.fetchall()
        for row in results:
            print(row)

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)

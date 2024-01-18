#!/usr/bin/python3
import MySQLdb
from sys import argv

if name == "__main__":
    # Check if all four arguments are provided
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(argv[0]))
        exit(1)

    # Extracting command line arguments
    username, password, database, state_name = argv[1], argv[2], argv[3], argv[4]

    # Connect to MySQL server
    try:
        connection = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = connection.cursor()

        # Execute query for specified state name
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC".format(state_name)
        cursor.execute(query)

        # Fetch and display results
        results = cursor.fetchall()
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("Error {}: {}".format(e.args[0], e.args[1]))
    finally:
        # Close the connection
        if 'connection' in locals():
            connection.close()
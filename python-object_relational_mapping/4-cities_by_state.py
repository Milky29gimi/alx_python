#!/usr/bin/python3
import MySQLdb
from sys import argv

if name == "__main__":
    # Check if all three arguments are provided
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    # Extracting command line arguments
    username, password, database = argv[1], argv[2], argv[3]

    # Connect to MySQL server
    try:
        connection = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = connection.cursor()

        # Execute query for listing all cities
        query = "SELECT * FROM cities ORDER BY cities.id ASC"
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
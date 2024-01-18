# A script that takes in the name of a state as an argument and lists all cities of that state, 
import MySQLdb
import sys

def list_cities(username, password, database, state_name):
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve cities of the specified state sorted by id
    cursor.execute("SELECT cities.id, cities.name FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %s \
                    ORDER BY cities.id ASC", (state_name,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()

if name == "__main__":
    # Check if all four arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL credentials and state name from command line arguments
    username, password, database, state_name = sys.argv[1:5]

    # Call the function to list cities of the specified state
    list_cities(username, password, database, state_name)
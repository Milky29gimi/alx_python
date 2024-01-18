# A script that takes in the name of a state as an argument and lists all cities of that state, 

import MySQLdb
import sys

# Get MySQL username, password, database name, and state name from command-line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]

# Connect to the MySQL server
db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Define the SQL query with parameterized query
query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
"""

# Execute the query with the state name as a parameter
cursor.execute(query, (state_name,))

# Fetch all the results
results = cursor.fetchall()

# Print the cities
for row in results:
    city_id, city_name, state_name = row
    print(f"{city_id}: {city_name} ({state_name})")

# Close the cursor and connection
cursor.close()
db.close()
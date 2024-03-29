#A script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!
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
query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

# Execute the query with the state name as a parameter
cursor.execute(query, (state_name,))

# Fetch all the results
results = cursor.fetchall()

# Print the states
for state in results:
    print(state)

# Close the cursor and connection
cursor.close()
db.close()
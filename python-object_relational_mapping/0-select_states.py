# A  script that lists all states from the database hbtn_0e_0_usa:
import MySQLdb
import sys

# Get MySQL username, password, and database name from command-line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# Connect to the MySQL server
db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Define the SQL query
query = "SELECT * FROM states ORDER BY id ASC"

# Execute the query
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Print the states
for state in results:
    print(state)

# Close the cursor and connection
cursor.close()
db.close()
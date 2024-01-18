# A script that takes in the name of a state as an argument and lists all cities of that state, 
import sys
import MySQLdb


# Connect to the MySQL server
db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

# Create a cursor
cursor = db.cursor()


cursor.execute(query, (state_name,))

# Fetch all the results
results = cursor.fetchall()

# Check if any results were found
if len(results) == 0:
    print(f"No cities found for the specified state '{state_name}'.")
else:
    # Print the cities
    cities = [row[0] for row in results]
    print(', '.join(cities))

# Close the cursor and database connection
cursor.close()
db.close()

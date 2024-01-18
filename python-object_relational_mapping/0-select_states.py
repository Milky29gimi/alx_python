# A script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(
    host='<localhost>',
    user='<milkly kerenso>',
    password='<Abdi29gimi!>',
    database='hbtn_0d_usa'
)

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()

# Define the SQL query
query = "SELECT cities.name FROM cities, states WHERE cities.state_id = states.id AND states.name = 'California' ORDER BY cities.id ASC"

# Execute the query
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Print the cities
for city in results:
    print(city[0])

# Close the cursor and connection
cursor.close()
cnx.close()
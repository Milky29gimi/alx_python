#A  script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
import MySQLdb
from sys import argv

#connecting to mysqldb
db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

#getting a cursor 
cur = db.cursor()

# executing a script that lists all cities from the database
cur.execute("SELECT cities.id, cities.name, ")

#printing result 
myresult = cur.fetchall()
for state in myresult:
  print(state)


# Closing all cursors and databases 
cur.close()
db.close() 

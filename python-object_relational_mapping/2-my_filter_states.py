# A script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
import MySQLdb
from sys import argv

#connecting to mysqldb
db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

#getting a cursor 
cur = db.cursor()

#executing a script that takes in an argument and displays all values in the states table
cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC".format(argv[4]))

#printing result
myresult = cur.fetchall()
for state in myresult:
  print(state)


# Closing all cursors and databases
cur.close()
db.close()
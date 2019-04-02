import mysql.connector
mydb = mysql.connector.connect(
  host="remotemysql.com",
  user="ykX5PLVyZY",
  passwd="MVRlvaVxjR",
  database="ykX5PLVyZY"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM student")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


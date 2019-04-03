import pymysql.cursors
mydb = pymysql.Connect(
  host="remotemysql.com",
  user="ykX5PLVyZY",
  passwd="MVRlvaVxjR",
  database="ykX5PLVyZY"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM student")

myresult = mycursor.fetchall()

for x in myresult:
  print(x[0])


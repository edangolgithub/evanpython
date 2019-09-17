import pymysql.cursors
mydb = pymysql.Connect(
  host="remotemysql.com",
  user="ykX5PLVyZY",
  passwd="MVRlvaVxjR",
  database="ykX5PLVyZY"
)
mycursor = mydb.cursor()
sql = "INSERT INTO student (name,roll, address) VALUES (%s,%s, %s)"
val = [
  ('Peter',3, 'Lowstreet 4'),
  ('Amy',4, 'Apple st 652'),
  ('Hannah',6, 'Mountain 21'),
  ('Michael', 7,'Valley 345'),
  ('Sandy', 8,'Ocean blvd 2'),
  ('Betty',9, 'Green Grass 1'),
  ('Richard',45, 'Sky st 331'),
  ('Susan', 123,'One way 98'),
  ('Vicky', 67,'Yellow Garden 2'),
  ('Ben', 77,'Park Lane 38'),
  ('William',56, 'Central st 954'),
  ('Chuck',65, 'Main Road 989'),
  ('Viola',34 ,'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
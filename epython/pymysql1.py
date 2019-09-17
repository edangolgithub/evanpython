import pymysql

conn = conn = pymysql.connect('localhost', 'root', '', 'school')

with conn:
    
    cur = conn.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()
    
    print("Database version: {}".format(version[0]))
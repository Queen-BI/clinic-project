import sqlite3

conn=sqlite3.connect("hospital.db")
cursor=conn.cursor()

cursor.execute("SELECT * FROM Appointment LIMIT 10")
rows=cursor.fetchall()

for row in rows:
    print(row)
conn.close()



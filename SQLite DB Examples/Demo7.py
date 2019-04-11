
# Example to read all records
# (rows/cols)from Employee Table

import sqlite3 as sql
conn = sql.connect("sathya.sqlite")
curs = conn.cursor()

curs.execute("select * from employee")
result = curs.fetchall()

for x in result:
    print(x)

conn.close()


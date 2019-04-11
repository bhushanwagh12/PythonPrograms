# Example to read all names
# from Employee Table

import sqlite3 as sql
conn = sql.connect("sathya.sqlite")
curs = conn.cursor()
curs.execute("select name from employee")
result = curs.fetchall()
print(result)
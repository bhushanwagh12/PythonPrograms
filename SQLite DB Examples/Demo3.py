# Example to create a table

import sqlite3 as sql
conn = sql.connect("sathya.sqlite")
curs = conn.cursor() # To Do Opertions on DB (CRUD)
curs.execute("create table employee(idno number primary key ,name text,salary real )")
conn.close()

print("Table is Created")



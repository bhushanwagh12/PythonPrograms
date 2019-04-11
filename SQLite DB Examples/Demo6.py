
# Example to insert 1 row into Employee table

import sqlite3 as sql
conn = sql.connect("sathya.sqlite")
curs = conn.cursor()

idno = int(input("IDNO : "))
name = input("NAME : ")
sal = float(input("SALARY : "))

curs.execute("insert into employee values (?,?,?)",(idno,name,sal))

conn.commit() # Save
conn.close()
print("1 Row inserted")

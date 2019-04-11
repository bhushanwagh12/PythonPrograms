
# Example to insert 1 row into Employee table

import sqlite3 as sql
conn = sql.connect("sathya.sqlite")
curs = conn.cursor()
curs.execute("insert into employee values (101,'Ravi',125000.00)")
conn.commit() # Save
conn.close()
print("1 Row inserted")

# Example to read 1 Employee Details

import sqlite3 as sql
conn = sql.connect("sathya.sqlite")
curs = conn.cursor()
idno = int(input("Enter IDNO : "))
curs.execute("select * from employee where idno = ?",(idno,))
result = curs.fetchone()
if result == None:
    print("Invalid IDNO")
else:
    print(result)
conn.close()

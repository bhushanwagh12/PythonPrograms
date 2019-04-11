

# Example to Delete

import sqlite3 as sql

conn = sql.connect("sathya.sqlite")
curs = conn.cursor()

id = int(input("Enter IDNO : "))

curs.execute("select * from employee where idno = ?",(id,))
result = curs.fetchone()
if result == None:
    print("Invalid IDNO")
else:
    curs.execute("delete from employee where idno = ?",(id,))
    conn.commit()
    print("Employee Deleted")

conn.close()
print("Thanks")




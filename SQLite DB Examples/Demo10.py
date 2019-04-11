
# Example to Update

import sqlite3 as sql

conn = sql.connect("sathya.sqlite")
curs = conn.cursor()

id = int(input("Enter IDNO : "))

curs.execute("select * from employee where idno = ?",(id,))
result = curs.fetchone()
if result == None:
    print("Invalid IDNO")
else:
    print(result)
    na = input("Enter New Name : ")
    sa = float(input("Enter New Salary : "))
    curs.execute("update employee set name = ?,salary = ? where idno = ?",(na,sa,id))
    conn.commit()
    print("New Details are Updated")

conn.close()
print("Thanks")






import sqlite3 as sql
try:
    conn = sql.connect("sample.sqlite")
    curs = conn.cursor()
    curs.execute("insert into Employee values (101,'Ravi')")
    conn.commit()
    print("Data Inserted")
finally:
    conn.close()
    print("Connection Closed")

print("Thanks")

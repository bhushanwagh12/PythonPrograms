
import sqlite3 as sql
try:
    conn = sql.connect("sample.sqlite")
    curs = conn.cursor()
    curs.execute("create table Employee(idno number primary key,name text)")
    print("Table is Created")
    curs.execute("insert into Employee values (101,'Ravi')")
    conn.commit()
    print("Data Inserted")
except sql.OperationalError as oe:
    print(oe)
finally:
    conn.close()
    print("Connection Closed")

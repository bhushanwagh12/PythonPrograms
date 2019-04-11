
import sqlite3 as sql

conn = sql.connect("sathya.sqlite")
curs = conn.cursor()
curs.execute("create table if not exists employee( idno number primary key ,name text,salary real )")
conn.close()
print("Table Created")
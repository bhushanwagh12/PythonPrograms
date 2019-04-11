
import psycopg2 as post

conn = post.connect(database="sathya",user="postgres",password="admin",
             port="5432",host="127.0.0.1")

print(conn)
curs = conn.cursor()
print(curs)

curs.execute("create table employee(idno int primary key,name text,salary real )")
conn.commit()
print("Table created")



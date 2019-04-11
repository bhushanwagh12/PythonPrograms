
import psycopg2 as sql

conn = sql.connect(database="icici",
                   user="postgres",
                   password="admin",
                   port="5432",
                   host="127.0.0.1")
curs = conn.cursor()
curs.execute("create table if not exists employee (idno int primary key,name text,salary real)")

id = int(input("IDNO : "))
name = input("Name : ")
sal = float(input("Salary : "))

curs.execute("insert into employee values (%s,%s,%s)",(id,name,sal))
conn.commit()
conn.close()
print("Table Created")
print("Data Inserted")
print("Thanks")

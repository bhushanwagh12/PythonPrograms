
import psycopg2 as post
conn = post.connect(database="sathya",
             user="postgres",
             password="admin",
             port="5432",
             host="127.0.0.1")
curs = conn.cursor()
curs.execute("insert into employee values (101,'Ravi',125000.00)")
conn.commit()
print("101 is inserted")
import psycopg2 as post
conn = post.connect(database="sathya",
             user="postgres",
             password="admin",
             port="5432",
             host="127.0.0.1")
curs = conn.cursor()
curs.execute("select * from employee")
f = curs.fetchall()
for x in f:
    print(x)
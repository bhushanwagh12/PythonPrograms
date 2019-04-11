import psycopg2 as post
conn = post.connect(database="sathya",
             user="postgres",
             password="admin",
             port="5432",
             host="127.0.0.1")

idno = int(input("Enter IDNO : "))
name = input("Enter Name :")
salary = float(input("Enter Salary :"))

curs = conn.cursor()
curs.execute("insert into employee values (%s,%s,%s)",(idno,name,salary))
conn.commit()
conn.close()
print(idno," Employee is inserted")

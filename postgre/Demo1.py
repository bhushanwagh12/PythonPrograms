
import psycopg2

conn = psycopg2.connect(database="sathya",
                        user = "postgres",
                        password = "admin",
                        host = "127.0.0.1",
                        port = "5432")
print(conn)
print("Opened database successfully")
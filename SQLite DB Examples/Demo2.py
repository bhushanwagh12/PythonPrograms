

# Example to get Connection from sqlite database
# file using path

import sqlite3 as sql

conn = sql.connect(r"C:\Users\android\Desktop\mydb\sathya.db")

print(conn)
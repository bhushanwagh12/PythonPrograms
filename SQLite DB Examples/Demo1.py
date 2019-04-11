
# Example to get Connection from
# sqlite database file

import sqlite3 as sql

conn = sql.connect("sathya.sqlite")

print(conn) # sqlite3.Connection object


from pymongo import MongoClient

mc = MongoClient()
db = mc.sathya
d1 = {"_id":104,"name":"Krishna","salary":185000.00}
res = db.employee.insert_one(d1)
print(res)
print("Data Inserted")
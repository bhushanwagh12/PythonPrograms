
from pymongo import MongoClient
mc = MongoClient()
db = mc.sathya

res = db.employee.delete_one({"_id":104})
print(res)
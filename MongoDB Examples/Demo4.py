
from pymongo import MongoClient
mc = MongoClient()
db = mc.sathya

filter = {"_id":104}
update_data = {
        "$set":{"name":"Krishna Mohan","salary":115000.00}
      }

up = db.employee.update_one(filter,update_data)
print(up)
print("Employee Details Updated")
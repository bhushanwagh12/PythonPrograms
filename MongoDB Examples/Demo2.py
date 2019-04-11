
from pymongo import MongoClient
mc = MongoClient()
db = mc.sathya
res = db.employee.find()
for x in res:
    print(x)
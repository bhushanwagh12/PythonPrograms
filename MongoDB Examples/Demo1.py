
from pymongo import MongoClient
# Connecting to MongoDB
mc = MongoClient('localhost:27017')
print(mc)
# Connecting to MyDatabase in Mongo
db = mc.sathya
print(db)

# Reading all Documents from employee
res = db.employee.find()

for x in res:
    print(x)


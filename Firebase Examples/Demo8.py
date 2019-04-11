
from firebase.firebase import FirebaseApplication
fire = FirebaseApplication("https://advancepython-8a7fd.firebaseio.com/merchant/employee/")
d1 = {"username":"abc","password":"123"}
res = fire.put("admin",102,d1)
if res:
    print("Data is added")
else:
    print("Data not added")
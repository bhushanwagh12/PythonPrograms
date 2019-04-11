
from firebase.firebase import FirebaseApplication
fire = FirebaseApplication("https://advancepython-8a7fd.firebaseio.com/merchant/employee/")
d1 = {"username":"s1","password":"Ravi1"}
res = fire.put("stocker",1001,d1)
if res:
    print("Data is Added")
else:
    print("Data not Added")


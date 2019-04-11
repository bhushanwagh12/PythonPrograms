
from firebase.firebase import FirebaseApplication

fire = FirebaseApplication("https://advancepython-8a7fd.firebaseio.com/")
d1 = {"username":"abc","password":"xyz"}
res = fire.put("merchant/employee/admin",101,d1)
if res:
    print("Data Added")
else:
    print("Data not Added")
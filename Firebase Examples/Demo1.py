
from firebase.firebase import FirebaseApplication
fire = FirebaseApplication("https://advancepython-8a7fd.firebaseio.com/")
d1 = {
    "name":"Ravi",
    "salary":125000.00,
    "contact":9052492329}

res = fire.put("employee",101,d1)
print(res)
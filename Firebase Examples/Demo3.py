
from firebase.firebase import FirebaseApplication
fire = FirebaseApplication("https://advancepython-8a7fd.firebaseio.com/")
res = fire.get("employee",None)
if res == None:
    print("Sorry Data Not Found")
else:
    print(res)

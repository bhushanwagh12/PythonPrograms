


e_id = int(input("IDNO :"))

from firebase.firebase import FirebaseApplication
fire = FirebaseApplication("https://advancepython-8a7fd.firebaseio.com/")

res = fire.get("employee",e_id)

if res != None:
    fire.delete("employee",e_id)
    print("Employee is Deleted")
else:
    print("Employee not Found")
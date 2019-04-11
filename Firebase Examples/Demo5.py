
e_idno = int(input("IDNO : "))
e_name = input("NAME : ")
e_salary = float(input("SALARY : "))
e_contact = int(input("CONTACT NO :"))

d1 = {
    "name":e_name,
    "salary":e_salary,
    "contact":e_contact}

from firebase.firebase import FirebaseApplication
fire = FirebaseApplication("https://advancepython-8a7fd.firebaseio.com/")

res = fire.get("employee",e_idno)

if res == None:
    fire.put("employee",e_idno,d1)
    print("Employee ", e_idno, " is Created")
else:
    print(e_idno," is Available")



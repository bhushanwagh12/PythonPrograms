
from Exceptions.Demo12 import MyException

def checkAge(age):
    if age >= 23:
        return "Valid Age"
    else:
        raise MyException("Please Enter Valid Age")

try:
    age = int(input("Enter AGE :"))
    res = checkAge(age)
    print(res)
except MyException as me:
    #print(me)
    me.displayMyError()
print("Thanks")
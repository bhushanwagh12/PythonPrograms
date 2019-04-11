

def checkAge(age):
    assert age >= 23,"Invalid Age"
    return "Valid Age"


try:
    age = int(input("Enter AGE :"))
    res = checkAge(age)
    print(res)
except AssertionError as ae:
    print(ae)
except ValueError:
    print("Invalid Input")
print("Thanks")

def checkAge(age):
    if age >= 23:
        return "Valid Age"
    else:
        raise ValueError("Invalid Age")

try:
    age = int(input("Enter AGE :"))
    res = checkAge(age)
    print(res)
except ValueError as ve:
    print(ve)
print("Thanks")
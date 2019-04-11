# Using multi except blocks
try:
    no1 = int(input("1st no : "))
    no2 = int(input("2nd no : "))
    print("The sum = ",(no1+no2))
    print("The div = ",(no1/no2))
    print("The mul = ",(no1*no2))
    print("The sub = ",(no1-no2))
    print("Thanks")
except ZeroDivisionError as zde:
    print(zde)
except ValueError:
    print("Invalid input")

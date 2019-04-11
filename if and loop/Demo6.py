
for x in range(3):
    pin = int(input("Enter PIn No : "))
    if pin == 5475:
        print("Welcome")
        break
    else:
        print("Invalid Pin No")
        if x == 2:
            print("Account is Blocked")
            break
        else:
            ans = input("To Continue press 1 : ")
            if ans == "1":
                continue
            else:
                break
print("Thanks")
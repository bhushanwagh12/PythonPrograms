
balance = 100
pin = int(input("PIN No : "))
if pin == 5475:
    print("Welcome MR/MISS : RAMA")
    wamount = int(input("Withdraw Amount : "))
    if wamount%100 == 0:
        if wamount <= 10000:
            if wamount <= balance:
                balance-=wamount # balance = balance - wamount
                print("Withdrawl is Done")
                print("Available Balance is ",balance)
            else:
                print(" No Balance")
        else:
            print("Max withdrawl is 10000/- only")
    else:
        print("Invalid Amount")
else:
    print("Invalid Pin")
print("Thanks")
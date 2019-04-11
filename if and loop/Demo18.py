
no = int(input("Enter a NO : "))
no1 = no%10
no = no//10
no2=0
while no != 0:
    no2 = no%10
    no = no//10

print("The sum = ",no1+no2)
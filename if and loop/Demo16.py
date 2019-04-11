
no = int(input("Enter a NO : "))
rev = 0
while no != 0:
    rem = no%10
    no = no//10
    rev = (rev*10)+rem

print("Given No in Reverse Order",rev)
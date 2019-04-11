
no = int(input("Enter a NO : ")) # 45
sum = 0
while no != 0:
    rem = no%10
    no = no//10
    sum = sum+rem

print("Sum of the Given No : ",sum)
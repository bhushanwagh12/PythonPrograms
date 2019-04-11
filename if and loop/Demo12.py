
for x in range(1,4):
    for z in range(x-1):
        print(" ",end=" ")
    for y in range(4,x,-1):
        print("*",end=" ")
    print()
print("========================")

for x in range(1,4):
    for z in range(x-1):
        print(" ",end=" ")
    for y in range(4,x,-1):
        print("*  ",end=" ")
    print()
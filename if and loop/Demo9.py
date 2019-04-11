import time

for x in range(1,4):
    for z in range(3,x,-1):
        print(" ",end=" ")
    for y in range(x):
        print("*",end=" ")
    print()
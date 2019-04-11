
# Example to check list is Iterable or not
l1 = [10,20,30,40,50]
i = iter(l1)
print(next(i)) # 10
print(next(i)) # 20
print(next(i)) # 30
print(next(i)) # 40
print(next(i)) # 50
# print(next(i)) # StopIteration Exception

print("------------------------")

# using while loop on a Iterator object
l1 = [10,20,30,40,50,60,70,80,90,100]
i = iter(l1)
while True:
    try:
        print(next(i))
    except StopIteration:
        break

print("------------------------")

# using for loop on a Iterator object
l1 = [10,20,30,40,50,60]
for x in l1:
    print(x)





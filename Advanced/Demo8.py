# Defining Generator Function with loop
def count(max=0):
    no=0
    while no < max:
        no+=1
        yield no

# Calling Generator Function
i = count(3)
print(next(i))
print(next(i))
print(next(i))
# print(next(i)) Exception
print("-------------------")

i = count(10)
while True:
    try:
        print(next(i))
    except StopIteration:
        break

print("-------------------")

for x in count(100):
    print(x,end=" ")
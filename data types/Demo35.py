
s1 = {10,20,30,40,50,60,70,80,90,100}
print(s1)

# Example of add method
s1.add(110)
print(s1)

# Example of clear method
s1.clear()
print(s1) # set()

print("-----------------------")
# Example of difference
s1 = {10,20,30,40}
s2 = {30,40,50,60}
s3 = s1.difference(s2)
print(s3) # {10,20}
s3 = s2.difference(s1)
print(s3) # {50,60}

print("-----------------------")
# Example on difference_update
s1 = {10,20,30,40}
s2 = {30,40,50,60}

print(s1) # {10,20,30,40}
print(s2) # {30,40,50,60}
s1.difference_update(s2)
print(s1) # {10,20}
print(s2) # {30,40,50,60}


print("-----------------------")
# Example on intersection
s1 = {10,20,30,40}
s2 = {30,40,50,60}

s3 = s1.intersection(s2)
print(s3) # {30,40}

print("-----------------------")
# Example on
s1 = {10,20,30,40}
s2 = {30,40,50,60}
print(s1.issubset(s2)) # False
print(s1.issuperset(s2)) # False
print("-----------------------")
s1 = {10,20,30,40}
s2 = {30,40,10,20}
print(s1.issubset(s2)) # True
print(s1.issuperset(s2)) # True
print("-----------------------")

s1 = {10,20,30,40,50,60,70}
s2 = {30,40,10,20}
print(s1.issubset(s2)) # False
print(s1.issuperset(s2)) # True
print("-----------------------")

s1 = {10,20,30,40,50,60,70}
s2 = {30,40,10,20}
print(s2.issubset(s1)) # True
print(s2.issuperset(s1)) # False
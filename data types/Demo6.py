
# Using builtin Functions on a list

l1 = [10,20,30,40,50,60,70,80,90,100]

# finding the length of list
length = len(l1)
print(length) # 10

# finding max element of list
max_element = max(l1)
print(max_element) # 100

# finding min element of list
min_element = min(l1)
print(min_element) # 10

# finding sum of a list
total = sum(l1)
print(total) # 550

print("--------------------------")

# type conversion functions

l1 = [10,20,30,10,20]
print(l1) # [10,20,30,10,20]
print(type(l1)) # <class list>

# converting list to tuple
t1 = tuple(l1)
print(t1)
print(type(t1))

# converting list to set
s1 = set(l1)
print(s1)
print(type(s1))

# converting list to string(str)
s1 = str(l1)
print(s1)
print(type(s1))
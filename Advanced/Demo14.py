
d1 = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5
}

# Print only keys
for x in d1:
    print(x,end="   ")
print("\n-----------------")
# or
print(d1.keys()) # List
print("\n-----------------")
# only Values
print(d1.values())
print("\n-----------------")
# key and value's
print(d1.items())
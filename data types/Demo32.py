
d1 = {1:"A",2:"B",3:"C",4:"D",5:"E"}

print(d1.items()) # key and values in list format
print(d1.keys()) # will return only keys in list format
print(d1.values()) # will return only values in list format

print("----------------")

print(d1) # {1:"A",2:"B",3:"C",4:"D",5:"E"}
d1.clear()
print(d1) # {}

print("----------------")

d1 = {1:"A",2:"B",3:"C",4:"D",5:"E"}

val = d1.get(30)

if val == None:
    print("Invalid Key")
else:
    print(val)

print("----------------")

d1 = {1:"A",2:"B",3:"C",4:"D",5:"E"}

print(d1)
try:
    d1.pop(30)
except KeyError:
    print("Invalid Key")

print(d1)










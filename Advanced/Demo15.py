
d1 = {"a":1,"b":2,"c":3,"d":4,"e":5}
print(d1)

d2 = {k:v*2 for k,v in d1.items()}
print(d2)

d3 = {k*2:v for k,v in d1.items()}
print(d3)

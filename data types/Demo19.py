
t1 = 10,20,30 # packing
print(t1) # (10,20,30)
print(type(t1)) # <class 'tuple'>

t2 = 1,00,000 # Packing
print(t2) # (1,0,0)

print("---------------------")



# packing
t1 = 10,"Sathya",True,10.25
print(t1) # (10,"Sathya",True,10.25)
print(type(t1)) # <class 'tuple'>

# unpacking
a,b,c,d = t1
print(a,type(a)) # 10 <class 'int'>
print(b,type(b)) # Sathya <class 'str'>
print(c,type(c)) # True <class 'bool'>
print(d,type(d)) # 10.25 <class 'float'>








# use (:) slice operator on a tuple
# =================================

t1 = (10,"Sathya",False,10.25,"Ravi",9000)

print(t1) # (10,"Sathya",False,10.25,"Ravi",9000)

print(t1[0]) # 10

print(t1[0:3]) # (10, Sathya, False)

print(t1[0:6:2]) # (10, Fasle, Ravi)

print(t1[::-1]) #
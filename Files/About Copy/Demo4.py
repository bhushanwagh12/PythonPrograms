
import copy as cp

a = [[10,20,30],[40,50,60],[70,80,90]]
b = cp.copy(a)
print(a)
print(b)
b[0] = "Ravi"
print("After Modification")
print(a)
print(b)
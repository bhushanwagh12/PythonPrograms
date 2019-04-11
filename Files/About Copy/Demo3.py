
import copy as cp

a = [10,20,30,40]
b = cp.copy(a)

print(a)
print(b)

b[0] = "Ravi"
print("After Modifications")
print(a)
print(b)



x = [[0]*6]
print(x) # [[0,0,0,0,0,0]]

y = [[0]*3]*5
print(y) # [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

z = [len(("Sathya"))*3]*2
print(z)

z = [len(("Sathya"),)*3]*2
print(z)

z = [len(("Sathya",))*3]*2
print(z)

z = [[len(("Sathya",))]*3]*2
print(z)


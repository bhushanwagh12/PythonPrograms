
l1 = [56,89,45,78,62,13,-50,"Sathya"]
l = len(l1)
l2 = []
for x in range(l,0,-1):
    l2.append(l1[x-1])

print(l2)
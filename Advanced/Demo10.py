
l1 = [1,2,3,4,5]
g = (x*2 for x in l1)
print(next(g)) # 2
print(next(g)) # 4
print(next(g)) # 6
print(next(g)) # 8
print(next(g)) # 10
print(next(g)) # StopIteration


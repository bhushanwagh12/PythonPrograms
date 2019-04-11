
import functools as fn

l = [10,20,30,40,50]

res = fn.reduce(lambda x,y : x+y,l)

print(res)


res = lambda a=0,b=0 : a+b
print(res()) # 0
print(res(20)) # 20
print(res("Sathya","Tech")) # SathyaTech

# Calling with param name

print(res(b=5,a=10.25))

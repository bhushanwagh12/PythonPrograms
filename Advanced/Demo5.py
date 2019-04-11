
print(int()) # 0
print(float()) # 0.0
print(bool()) # False

i = iter(int,1)
for x in i:
    print(x)
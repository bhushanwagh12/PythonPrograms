# Page No 15
# Q:NO : 41

def common_end(a,b):
    if a[0]==b[0] or a[-1]==b[-1]:
        return True
    else:
        return False

res = common_end([1,2,3],[7,3])
print(res)

res = common_end([1,2,3],[7,3,2])
print(res)

res = common_end([1,2,3],[1,3])
print(res)

res = common_end(['A','B','C'],['A','B'])
print(res)


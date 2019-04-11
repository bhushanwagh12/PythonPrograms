
def rotate_left(l1):
    no = l1.pop(0)
    l1.append(no)
    return l1

print(rotate_left([1,2,3]))
print(rotate_left([11,9,5]))
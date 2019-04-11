# Defining Generator Function
def count():
    no = 1
    yield no

    no+=1
    yield no

    no+=1
    yield no

# Calling Generator Function
# it is returning Iterator Object
i = count()
print(next(i))
print(next(i))
print(next(i))
print(next(i))
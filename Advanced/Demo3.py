
class MyIterator:
    def __init__(self,max=0):
        self.max = max

    def __iter__(self):
        self.no = 0
        return self

    def __next__(self):
        if self.no < self.max:
            self.no = self.no+1
            return self.no
        else:
            raise StopIteration

# Example to check MyIterator is Iterable or not
m1 = MyIterator(3)
i = iter(m1)
print(next(i)) # 1
print(next(i)) # 2
print(next(i)) # 3
# print(next(i)) # Exception
print("--------------------------")

# using while loop on a Iterator object
m1 = MyIterator(100)
i = iter(m1)
while True:
    try:
        print(next(i))
    except StopIteration:
        break
print("--------------------------")

# using for loop on a Iterator object
for x in MyIterator(25):
    print(x)
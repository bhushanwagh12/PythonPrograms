
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

my = MyIterator(3)
i = iter(my)
print(next(i))
print(next(i))
print(next(i))
# print(next(i)) Exception
print("--------------------")

my1 = MyIterator(10)
i = iter(my1)
while True:
    try:
        print(next(i))
    except StopIteration:
        break
print("----------------")

for x in MyIterator(20):
    print(x,end=" ")
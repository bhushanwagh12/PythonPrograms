
class A:
    def __init__(self):
        print("A class Constructor")

class B(A):
    def show(self):
        print("B class Show")

x = B()
x.show()
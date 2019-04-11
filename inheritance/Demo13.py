class A:
    def __init__(self):
        '''A Class Constructor'''
        print("Default Constructor of A")
class B:
    def __init__(self):
        '''B Class Constructor'''
        print("Default Constructor of B")
class C(A,B):
    def show(self):
        print("Show of C")

x = C()
x.show()

help(C)
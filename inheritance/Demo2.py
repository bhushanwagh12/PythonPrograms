class A:
    def m1(self):
        print("m1 of class A")
    def m2(self):
        print("m2 of class A")

class B(A):
    def m3(self):
        print("m3 of class B")

x = B()
x.m3()
x.m1()
x.m2()

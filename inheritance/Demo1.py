class A:
    def m1(self):
        print("M1 of class A")

class B(A):
    def m2(self):
        print("M2 of class B")

x = B()
x.m2() # Calling B class Method
x.m1() # Calling A class Method

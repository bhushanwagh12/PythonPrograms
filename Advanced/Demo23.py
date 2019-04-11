class RBI:
    def about(self):
        print("This is RBI")

    @classmethod
    def show(cls):
        print("I am class Method")
        if cls == SBI:
            print("SBI is using RBI")
        if cls == ICICI:
            print("ICICI is using RBI")

class SBI(RBI):
    def tell(self):
        print("This is SBI")

class ICICI(RBI):
    def tell(self):
        print("This is ICICI")

class Paytm:
    def tell(self):
        print("I am paytm")

SBI.show() # show(SBI)
ICICI.show() # show(ICICI)
Paytm.show() # Error


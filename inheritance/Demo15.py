
class RBI:
    def __init__(self,acno,name):
        '''RBI Constructor'''
        self.acno = acno
        self.name = name

class ICICI(RBI):
    def __init__(self,acno,name,amount):
        '''ICICI Constructor'''
        super().__init__(acno,name)
        self.amount = amount
    def display(self):
        print("Account No = ",self.acno)
        print("Name = ",self.name)
        print("Balance = ",self.amount)

i = ICICI(1212,"Ravi",25000.00)
i.display()

help(ICICI)
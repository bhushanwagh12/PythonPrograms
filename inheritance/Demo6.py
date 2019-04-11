
class Employee:
    '''
    This is a Employee class
    '''
    def __init__(self,id,na,sal):
        self.idno = id
        self.name = na
        self.salary = sal

class TemEmployee(Employee):
    def display(self):
        print(self.idno)
        print(self.name)
        print(self.salary)

#t = TemEmployee(101,"Ravi",125000.00)
#t.display()

help(TemEmployee)
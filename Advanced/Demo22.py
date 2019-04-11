
class Employee:
    def __init__(sathya,idno,name,sal=0.0):
        sathya.idno = idno
        sathya.name = name
        sathya.salary = sal
    def display(self):
        print(self.idno)
        print(self.name)
        print(self.salary)

e1 = Employee(101,"Ravi",125000.00)
e1.display()

e2 = Employee(102,"Kumar",185000.00)
e2.display()

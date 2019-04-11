
class Employee:
    def __init__(self,idno,name):
        self.idno = idno
        self.name = name
    def display(self):
        print("IDNO = ",self.idno)
        print("NAME = ",self.name)

class TempEmployee(Employee):
    def __init__(self,idno,name,salary):
        super().__init__(idno,name)
        self.salary = salary
    def display(self):
        super().display()
        print("Temp Employee Salary = ",self.salary)

class PerEmployee(Employee):
    def __init__(self, idno, name, salary):
        super().__init__(idno, name)
        self.salary = salary

    def display(self):
        super().display()
        print("Per Employee Salary = ", self.salary)


t1 = TempEmployee(101,"Ravi",125000.00)
t1.display()

print("--------------------------------")

p1 = PerEmployee(102,"kumar",185000.00)
p1.display()
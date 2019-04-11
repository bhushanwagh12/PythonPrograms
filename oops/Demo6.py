
class Employee:
    def assign(emp,idno,name,salary=0.0):
        emp.idno = idno
        emp.name = name
        emp.salary = salary

    def display(self):
        print(self.idno)
        print(self.name)
        print(self.salary)

e1 = Employee()
e1.assign(101,"Ravi",125000.00)
e1.display()


class Employee:
    def assign(self,idno,name,salary):
        self.idno = idno
        self.name = name
        self.salary = salary

class TEmployee(Employee):
    def display(self):
        print(self.idno)
        print(self.name)
        print(self.salary)

te = TEmployee()
te.assign(101,"Ravi",125000.00)
te.display()
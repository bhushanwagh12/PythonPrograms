
class Employee:
    def assign(self):
        self.idno = 101
        self.name = "Ravi"
    def display(self):
        print(self.idno)
        print(self.name)

a = Employee()
a.assign()
a.display()

b = Employee()
b.assign()
b.display()
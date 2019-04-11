class Employee:
    def __init__(self):
        self.idno = 101
        self.name = "Ravi"

    def display(self):
        print(self.idno)
        print(self.name)

e1 = Employee()

e2 = Employee()

print(e1 is e2)

e3 = e2

print(e2 is e3)



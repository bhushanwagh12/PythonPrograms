class Employee:
    def __init__(self):
        self.idno = 101
        self.name = "Ravi"

    def display(self):
        print(self.idno)
        print(self.name)

e = Employee()

e1 = None

if not e:
    print("Object Not Available")
else:
    print("Object Available")


class Employee:
    def assign(self,id,na):
        self.idno = id
        self.name = na
    def display(self):
        print(self.idno)
        print(self.name)

e1 = Employee()
e1.assign(101,"Ravi")
e1.display()

e2 = Employee()
e2.assign(102,"Kumar")
e2.display()



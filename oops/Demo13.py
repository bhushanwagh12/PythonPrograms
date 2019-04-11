class Employee:
    def assign(self):
        print("I am assign Method")
    def assign(self,idno):
        self.idno=idno
    def assign(self,idno,name):
        self.idno=idno
        self.name=name
    def assign(self,idno,name,salary):
        self.idno=idno
        self.name=name
        self.salary=salary
    def display(self):
        print(self.idno)
        print(self.name)
        print(self.salary)


e1 = Employee()
e1.assign()
e1.display()
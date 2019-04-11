
class Employee:
    def assign(self,id=0,na="",sal=0.0):
        self.idno = id
        self.name = na
        self.salary = sal

e1 = Employee()
e1.assign()
e1.assign(id=101)
e1.assign(id=102,sal=125000.00)

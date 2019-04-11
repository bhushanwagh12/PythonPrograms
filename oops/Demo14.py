class Employee:
    def assign(self,idno=0,name=None,salary=0.0):
        self.idno = idno
        self.name = name
        self.salary = salary
    def display(self):
        print(self.idno,self.name,self.salary)

e1 = Employee()
e1.assign()
e1.display() # 0,None,0.0
e1.assign(101)
e1.display() # 101,None,0.0
e1.assign(101,"Ravi")
e1.display() # 101,Ravi,0.0
e1.assign(101,"Ravi",125000.00)
e1.display() # 101,Ravi,125000.00
print("-----------------------------------")
# Named args (Keyword args)
e1.assign(name="Kumar")
e1.display()
e1.assign(salary=185000.00,idno=102)
e1.display()


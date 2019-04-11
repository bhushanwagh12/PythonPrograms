
class Employee:
    comp_name = "sathya"
    comp_cno = 905249329
    @staticmethod
    def displayCompInfo():
        print(Employee.comp_name)
        print(Employee.comp_cno)

    def assign(self,idno,name,salary=0.0):
        self.idno = idno
        self.name = name
        self.salary = salary

    def display(self):
        print(self.idno)
        print(self.name)
        print(self.salary)

# # # Calling static method
# Employee.displayCompInfo()
# print("------------------------------------")
# # # Creating Object
e1 = Employee()
e1.assign(101,"Ravi",125000.00)
e1.display()
print("------------------------------------")
# print(e1.idno)
# print(e1.name)
# print(e1.salary)

# print(e1.Employee.sal) # Error
# print(e1.Employee.comp_cno) # Error
# e1.assign() # Error
# e1.display() # 101 Ravi 125000.00
# e1.displayCompInfo()
# print(Employee.idno) # Error
# print(e1.comp_cno)
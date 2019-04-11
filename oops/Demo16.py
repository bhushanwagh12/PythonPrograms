class Employee:
    def __init__(self,id,name,sal):
        self.idno =id
        self.name = name
        self.salary = sal
    def display(self):
        print(self.idno)
        print(self.name)
        print(self.salary)

my_emp = []
for x in range(3):
    i = int(input("IDNO : "))
    n = input("NAME : ")
    s = float(input("SALARY : "))
    my_emp.append(Employee(i,n,s))

print("-----------------------")
# display 102 Employee Details
my_emp[1].display()
print("-----------------------")
# display 103 Employee Salary
print(my_emp[2].salary)
print("-----------------------")
# compare 101 and 103 salary's and
# display big salary employee id no
if my_emp[0].salary > my_emp[2].salary:
    print(my_emp[0].idno,"Is Big Salary")
else:
    print(my_emp[2].idno,"Is Big Salary")

print("-----------------------")
for x in my_emp:
    x.display()
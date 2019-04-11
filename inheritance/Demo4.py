
class Employee:
    comp_name = "sathya"
    comp_cno = 9052

class TemEmployee(Employee):
    def display(self):
        print(TemEmployee.comp_name)
        print(TemEmployee.comp_cno)

print(TemEmployee.comp_cno)
#          (or)
print(Employee.comp_cno)
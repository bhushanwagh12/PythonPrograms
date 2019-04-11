
# Example to check Employee is Iterable or not
class Employee:
    def show(self):
        print("I am Show")

e1 = Employee()

i = iter(e1) # 'Employee' object is not iterable
print(i)

class Employee:
    def __init__(self):
        print("I am Constructor")
    def display(self):
        print("This is display")
    def __del__(self):
        print("I am Destructor")

e1 = Employee()
e1.display()

del e1


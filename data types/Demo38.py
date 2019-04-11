
# Example on function documentation

def display():
    '''
    This function will display employee
    information like idno,name,salary and
    this function never return
    :return: No return
    '''
    print("IDNO = 101")
    print("NAME = RAVI")
    print("SALARY = 125000.00")

print(display.__doc__)
print("--------------------------")
print(input.__doc__)
print("--------------------------")
print(type.__doc__)
print("--------------------------")

help(display)

import sqlite3 as sql
help(sql.connect)

help(list)

fname = input("Enter File Name : ")
try:
    f = open(fname)
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Sorry No File")
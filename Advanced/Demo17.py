
def outer():
    print("I am Outer")
    a = 100
    def inner():
        print("I am Inner")
        print(a)
    return inner

inn = outer()
del outer
print("Outer is Deleted")
inn()

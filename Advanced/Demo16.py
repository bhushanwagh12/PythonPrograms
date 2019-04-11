
def outer():
    print("I am Outer")
    a = 100
    def inner():
        print("I am Inner")
        print(a)
    inner()

outer()
del outer
outer() # Exception (Because outer is deleted)

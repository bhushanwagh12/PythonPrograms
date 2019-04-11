a = 1000 # Global Variable
def outer():
    a = 1500 # local variable of outer function
    print(a)
    def inner():
        a = "sathya" # local variable of inner funtion
        print(a)
    inner()# inner function calling
    print(a)


print(a)
outer() # outer function calling
print(a)
a = 500
def outer():
    a = 1000
    print(a)
    def inner():
        global a
        a = "sathya"
        print(a)
    inner()
    print(a)
print(a)
outer()
print(a)
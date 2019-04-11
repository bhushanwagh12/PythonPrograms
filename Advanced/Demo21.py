
def mydec(fun):
    def inner():
        fun()
        print("This statement is extra")
    return inner

@mydec
def sample():
    print("This is Sample Function")

sample()
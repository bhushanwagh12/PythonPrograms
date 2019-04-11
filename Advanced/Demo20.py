
def sample():
    print("I am Function sample")

def outer(fun):
    def inner():
        fun() # sample()
        print("I am Inner Function")
    return inner

inn = outer(sample)
inn()



def outer():
    print("I am Outer Function")
    def inner():
        print("I am Inner Function")
    inner() # Calling inner Function

# Calling Outer Function
outer()



# Example to use local variable of outer
# function .v

def outer():
    a = 1000 # local Variable
    print("Outer :",a)

    def inner():
        print("Inner :",a)
    inner() # Calling inner Function

# Calling Outer Function
outer()
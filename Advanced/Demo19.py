
def inc(no):
    return no+1

def dec(no):
    return no-1

def operation(fun,no):
    x = fun(no)
    print(x)

operation(inc,100)
operation(dec,50)


g = (x*2 for x in range(1,6))
while True:
    try:
        print(next(g))
    except StopIteration:
        break
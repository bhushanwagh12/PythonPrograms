
try:
    f = open("sample.txt","r")
    v = f.readline() # Read 1st Line
    print(v)
    v1 = f.readline() # Read 2nd line
    print(v1)
    f.close()
except FileNotFoundError:
    print("File Not Found")
    

try:
    f = open("sample.txt","r")
    v = f.read()
    print(v)
    f.close()
except FileNotFoundError:
    print("File Not Found")


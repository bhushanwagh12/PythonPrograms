
try:
    f = open("sample.txt","r")
    v = f.readlines()
    print(v)
    f.close()
except FileNotFoundError:
    print("File Not Found")

try:
    f = open(r"C:\Users\android\Desktop\10 am adv python.txt","r")
    v = f.read()
    print(v)
    f.close()
except FileNotFoundError:
    print("Please Check the Given File Name")
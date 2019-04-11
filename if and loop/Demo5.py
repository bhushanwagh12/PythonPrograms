
tno = int(input("Enter Table No : "))
sno = int(input("Enter Table Start No : "))
eno = int(input("Enter Table End No : "))

if sno<eno:
    for i in range(sno,eno+1):
        print(tno, " X ", i, " = ", (tno * i))
elif sno>eno:
    for i in range(sno,eno-1,-1):
        print(tno, " X ", i, " = ", (tno * i))
else:
    print("Invalid Table")
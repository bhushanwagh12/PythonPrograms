
import os.path as pa
fname = input("Enter File name : ")
res = pa.exists(fname)
if res == True:
    print("File Available")
else:
    print("File Not Available")
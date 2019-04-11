
import csv
try:
    f = open("one.csv")
    l = csv.reader(f)
    for x in l:
        print(x)
except FileNotFoundError:
    print("File Not Found")
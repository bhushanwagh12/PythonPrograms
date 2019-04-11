d1 = {
    101:{"name":"A","class":10,"marks":[65,95,85,50,45,99]},
    102:{"name":"B","class":10,"marks":[55,85,45,90,46,90]},
    103:{"name":"C","class":10,"marks":[15,75,45,80,56,80]},
    104:{"name":"D","class":10,"marks":[85,65,55,70,66,70]},
    105:{"name":"E","class":10,"marks":[65,55,65,60,76,60]}
}

# print only keys
for x in d1:
    print(x)
print("-------------")

# print only values
for x in d1.values():
    print(x)
print("-------------")

# print all Students marks
for x in d1:
    print("Student ",x," marks = ",d1[x]["marks"])
    print("Total Marks = ",sum(d1[x]["marks"]))
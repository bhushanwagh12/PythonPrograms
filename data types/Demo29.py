
s1 = {"101":
          {"name":"A","marks":[10,20,30,40,50,60]},
      "102":
          {"name":"B","marks":[11,12,13,14,15,16]},
      "103":
          {"name":"C","marks":[17,18,19,20,21,22]}
     }

# 1st Student Name
print(s1["101"]["name"])

# 2nd Student Subject 3 Marks
print(s1["102"]["marks"][2])

# 3rd student Total marks
print(sum(s1["103"]["marks"]))


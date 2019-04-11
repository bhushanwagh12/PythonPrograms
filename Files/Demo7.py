
fname = input("Enter File Name : ")
f = open(fname,"w")
text = input("Enter Some text :")
f.write(text)
f.close() # Save and Close
print("Text Written to File")
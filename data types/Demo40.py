
s1 = "sathya tech"
s2 = s1.split('a')
print(s2) # ['s', 'thy', ' tech']

# Read 5 nos from user
nos = input("Enter 5 nos by giving space")
print(nos)
res = nos.split(" ")
sum=0
for x in res:
    sum = sum+int(x)
print(sum)

my_friends=["Ravi","Kumar","Krisna","Mohan","Prasad","Babu","Deepak","Naveen"]

ur_friends=["Krish","Prasad","Krisna","Mohan","Prasad","Ganesh","Ravi","Deepak","Mohan Krihna"]

comm_friends = [] # Empty list

for x in my_friends:
    if x in ur_friends:
        comm_friends.append(x)

print(comm_friends)


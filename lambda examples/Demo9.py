
l1 = [10,20,30,40,50]
l2 = [1,2,3,4,5]
l3 = list(map(lambda x,y : x*y,l1,l2))
print(l3)
print("-------------------------")

l1 = [35,46,17,-73,92.2]
l2 = [20,139,-4,55,280]
l3 = list(map(lambda x,y :x if x>=y else 0,l1,l2))
print(l3)

print("----------")

l3 = list(map(lambda x,y :"Big" if x>=y else "Small",l1,l2))
print(l3)

print("---------------------")

marks = [45,75,35,12,19,36]
result = list(map(lambda x :"Pass" if x>=35 else "Fail",marks))
print(result)





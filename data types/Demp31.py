
merchant = {
           "admin":{
               "uname":"admin",
               "upass":"admin123"},
           "product":{
               101:{
                   "name":"A",
                   "price":12000.00},
               102:{
                   "name":"B",
                   "price":15000.00}
           },
           "stocker":{
               "login":{
                   "uname":"stock",
                   "upass":"stock"},
               "add":{
                   "pid":101,
                   "name":"A",
                   "price":12000.00}
           }
}

# WAP to validate admin username and password
# un = input("Username : ")
# pa = input("Password : ")
#
# if un == merchant["admin"]["uname"] and pa == merchant["admin"]["upass"]:
#     print("Valid User")
# else:
#     print("Invalid User")


un = input("Stocker Username : ")
pa = input("Stocker Password : ")

if un == merchant["stocker"]["login"]["uname"] and pa == merchant["stocker"]["login"]["upass"]:
    print("Valid")
else:
    print("Invalid")


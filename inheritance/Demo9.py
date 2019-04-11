
class First:
    def calc(self,no1,no2):
        print("The sum = ",no1+no2)
        print("The sub = ",no1-no2)
class Second(First):
    def calc(self,no1,no2):
        super().calc(no1,no2)
        print("The mul = ",no1*no2)
        print("The div = ",no1/no2)
class Third(Second):
    def calc(self,no1,no2):
        super().calc(no1,no2)
        print("The Mod = ",no1%no2)

# t = Third()
# t.calc(10,2)

help(Third)
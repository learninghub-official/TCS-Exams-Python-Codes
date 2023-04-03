class Area:
    def __init__(self,id,name,type):
        self.id = id
        self.name = name 
        self.type = type 
class Solution:
    def __init__(self,list):
        self.list = list
    def c1(self,userType):
        l1 = []
        for i in list:
            if i.type.lower() == userType.lower():
                l1.append(i)
            l2 = sorted(l1 ,key=lambda x:x.id ,reverse=True)
        for j in l2:
            print(f"{j.id} {j.name} {j.type}")
    def c2(self,string1):
        c1 = 0
        c2 = 0
        for i in string1:
            if i.isdigit():
                c1 +=1
            elif i.isalpha():
                c2 +=1
        if c1>c2:
            print(f"Numbers:{c1}")
            print(f"Alphabets{c2}")
        else:
            print(f"Alphabets{c2}")
            print(f"Numbers:{c1}")

list = []
for i in range(int(input())):
    id = int(input())
    name = input()
    type = input()
    obj1 = Area(id,name,type)
    list.append(obj1)
userType = input()
string1 = input()
obj2 = Solution(list)
ans1 = obj2.c1(userType)
print("\n#########################\n")
ans2 = obj2.c2(string1)


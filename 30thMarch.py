def countn(n):
    count1 = 0
    count2 = 0
    for i in n:
        if i.isdigit():
            count1+=1
        elif i.isalpha():
            count2 +=1
    if count1>count2:
        print("Number:", count1)
        print("Alphabets:", count2)
    else:
        print("Alphabets:", count2)
        print("Number:", count1)
n = input()
ans = countn(n)
if ans:
    print(ans)

'''
Input 1:
Sachin1234

Output 1:
Alphabets: 6
Number: 4

###############

12345678Sachi

Number: 8
Alphabets: 5

'''

'''

class area:
    def __init__(self,id,name,type):
        self.id = id
        self.name = name
        self.type = type
class Solution:
    def __init__(self,list):
        self.list = list
    def Ssort(self,userType):
        l1 = []
        for i in list:
            if i.type.lower() == userType.lower():
                l1.append(i)
        l2 = sorted(l1,key=lambda x:x.id ,reverse=True)
        for j in l2:
            print(f"{j.id} {j.name} {j.type}")
list = []
for i in range(int(input())):
    id = int(input())
    name = input()
    type = input()
    obj1 = area(id,name,type)
    list.append(obj1)
userType = input()
obj2 = Solution(list)
ans = obj2.Ssort(userType)

'''
'''
Input:
3
101
Mayank
beach
2
Nupur
Mountain   
104
Gavish
beach
beach

Output:
104 Gavish beach
101 Mayank beach
'''

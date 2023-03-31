'''class Area:
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
            l2 = sorted(l1,key = lambda x:x.id , reverse=True)
        for i in l2:
            print(f"{i.id} {i.name} {i.type}")
list=[]
for i in range(int(input())):
    id = int(input())
    name = input()
    type = input()
    objArea = Area(id,name,type)
    list.append(objArea)
userType = input()
objSol = Solution(list)
ans = objSol.c1(userType)
'''
'''

Input:
5
101
Mayank
Beach
102
Sachin
beach
103
Nidhi
mountain
104
Gavish
beach
105
tanishq
desert
beach

Output:
104 Gavish beach
102 Sachin beach
101 Mayank Beach
'''


def count(n):
    c1 = 0
    c2 = 0
    for i in n:
        if i.isdigit():
            c1 +=1
        elif i.isalpha():
            c2 +=1
    if c1 > c2 :
        print(f"Number:{c1}")
        print(f"Alphabets:{c2}")
    else:
        print(f"Alphabets:{c2}")
        print(f"Numbers:{c1}")
n = input()
ans = count(n)

'''
Input 1:
Sachin123Attkan

Output:
Alphabets:12
Numbers:3

Input 2:
123456sac

Output:
Number:6
Alphabets:3
'''
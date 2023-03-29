class sim:
    def __init__(self,id,cname,balance,rateperSec,circle):
        self.id = id
        self.cname = cname
        self.balance = balance
        self.rateperSec = rateperSec
        self.circle = circle
class Solution :
    def __init__(self,list):
        self.list = list
    def TransferCustomerCircle(self,userCircle1,userCircle2):
        l1 = []
        for i in list:
            if i.circle.lower() == userCircle1.lower():
                i.circle = userCircle2
                l1.append(i)
        if l1 ==[]:
            return 0
        else:
            l1.sort(key = lambda x:x.rateperSec , reverse=True)
            for i in l1:
                print(f"{i.id} {i.cname} {i.circle} {i.rateperSec}")
            
list = []
for i in range(int(input())):
    id = int(input())
    cname = input()
    balance = float(input())
    rateperSec = float(input())
    circle = input()
    objsim = sim(id,cname,balance,rateperSec,circle)
    list.append(objsim)
userCircle1 = input()
userCircle2 = input()
objsol = Solution(list)
ans1 = objsol.TransferCustomerCircle(userCircle1,userCircle2)



'''
5
1
raj
100
1.5
KOL
2
chetan
200
1.6
AHD
3
asha
150
1.7
MUM
4
kiran
50
2.2
AHD
5
vijay
130
1.8
AHD
AHD
KOL


Output:
4 kiran KOL 2.2
5 vijay KOL 1.8
2 chetan KOL 1.6
'''
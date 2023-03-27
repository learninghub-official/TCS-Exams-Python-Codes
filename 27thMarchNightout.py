
class Player:
    def __init__(self,id,name,runs,playerType,matchType):
        self.id = id 
        self.name= name
        self.runs = runs 
        self.playerType= playerType
        self.matchType = matchType
class Solution:
    def __init__(self,list):
        self.list = list

    def findPlayerWithLowestRun(self,userPlayerType):
        l=[]
        for i in list:
            if i.playerType.lower() == userPlayerType.lower():
                l.append(i.runs)
            # m = min(l)
        if l == []:
            print("Not Found")
        else:
            m = min(l)
            return m
    def findPlayerbyMatchType(self,userMatchType):
        l1 = []
        for i in list:
            if i.matchType.lower() == userMatchType.lower():
                l1.append(i.id)
            l1.sort()
        return l1

list = []
for i in range(int(input())):
    id = int(input())
    name = input()
    runs = int(input())
    playerType  = input()
    matchType = input()
    objPlayers = Player(id,name,runs,playerType,matchType)
    list.append(objPlayers)

userPlayerType = input()
userMatchType = input()
objSol = Solution(list)
ans1 = objSol.findPlayerWithLowestRun(userPlayerType)
ans2 = objSol.findPlayerbyMatchType(userMatchType)
if ans1:
    print("Lowest Run Player :",ans1)
else:
    print("All are Equal")
if ans2:
    for i in ans2:
        print(i)
else:
    print("Player Not Found")


'''
4
11
Sachin
100
International
one Day
12
Shewag
133
International
Test
13 
Varun
78
State
Test
14
Ashwin
67
State
One Day
State
One Day

Output:
Lowest Run Player : 67
11
14

'''


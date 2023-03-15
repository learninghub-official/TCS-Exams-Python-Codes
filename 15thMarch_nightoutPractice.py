class CricketPlayer:
    def __init__(self,cplayerName , cplayedCountry , cplayerAge,cpCountryFrom):
        self.cplayerName = cplayerName
        self.cplayedCountry = cplayedCountry
        self.cplayerAge = cplayerAge
        self.cpCountryFrom = cpCountryFrom

class Solution:
    def __init__(self,listOfPlayers):
        self.listOfPlayers = listOfPlayers
    def countPlayers(self,country):
        count = 0
        for i in listOfPlayers:
            if i.cpCountryFrom.lower() == country.lower():
                count+=1
        return count
    def getPlayerPlayedForMaxCountry(self):
        dic = {}
        for i in listOfPlayers:
            dic[i.cplayerName] = len(i.cplayedCountry)
        # return (dic)
        m = max(dic.values())
        l2 = []
        for j in dic:
            if dic[j] == m:
                l2.append(j)
        l2.sort()
        print(l2)
        if len(l2)>0:
            return l2[0]
        else:
            return "no players found"
        
n = int(input())
listOfPlayers = []
for i in range(n):
    cplayerName = input()
    cplayedCountry = []
    for j in range(int(input())):
        cplayedCountry.append(input())
    cplayerAge = int(input())
    cpCountryFrom = input()
    objCricketPlayer = CricketPlayer(cplayerName , cplayedCountry , cplayerAge,cpCountryFrom)
    listOfPlayers.append(objCricketPlayer)
country = input()
objSolution = Solution(listOfPlayers)
ans = objSolution.countPlayers(country)

if ans:
    print(ans) 
else:
    print("No Country Found !")
# print(objSolution.countPlayers(country))
print(objSolution.getPlayerPlayedForMaxCountry())


'''
Input 1:
2
Mayank
2
Af
Br
21
India
Nupur
1
br
22
India
af   

Output:
No Country Found !
['Mayank']
Mayank

Input 2:
2
Mayank
2
Af
Br
21
India
Nupur
1
br
22
India
india   

Output:
2
['Mayank']
Mayank
'''

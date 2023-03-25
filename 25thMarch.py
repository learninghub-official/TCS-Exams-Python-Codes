# practice 

class Sponsor:
    def __init__(self,sName,sCompany,stieup,sCategory):
        self.sName = sName
        self.sCompany = sCompany
        self.stieup = stieup
        self.sCategory = sCategory
def getSponsor(listSponsor,usCategory):
    for i in listSponsor:
        if i.sCategory.lower() == usCategory.lower():
            print(i.sName)
def maxTieup(listSponsor):
    l1 =[]
    for i in listSponsor:
        l = len(i.stieup)
        l1.append(l)
    # print(l1)
    m = max(l1)
    # print(m)
    for i in listSponsor:
        if len(i.stieup) == m:
            print(i.sName)
listSponsor = []
for i in range(int(input())):
    sName = input()
    sCompany = input()
    stieup = []
    for j in range(int(input())):
        stieup.append(input())
    sCategory = input()
    obj = Sponsor(sName,sCompany,stieup,sCategory)
    listSponsor.append(obj)
usCategory = input()
ans = getSponsor(listSponsor,usCategory)
ans2 = maxTieup(listSponsor)

'''

Input:
2     
Mayank
TCS
2      
google
apple
IT
Nupur
cogniant
1
microsoft
Education  
education

Output:
Nupur
Mayank

'''

'''

#Another Question for practice

n = input()     
l = n.split("$")
countSpace =0
countLower =0
countNumber=0
for i in range(len(l)):
    for j in l[i]:
        if j.isspace():
            countSpace +=1
        elif j.islower():
            countLower +=1
        elif j.isdigit():
            countNumber +=1
print(f"{countLower} {countNumber} {countSpace}")

'''
'''
Input:
abc def4 5$

Output:
6 2 2
'''

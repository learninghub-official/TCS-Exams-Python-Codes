
# Icecream Question to find minimum icecream by price and to return sorted list of id's of icecreams 

class Icecream:
    def __init__(self,id,price,name,quantityInGms,category):
        self.id = id
        self.price = price
        self.name = name
        self.qualityInGms = quantityInGms
        self.category = category

class IcecreamStore:
    def __init__(self,IcecreamList):
        # self.IcecreamStoreName = IcecreamStoreName
        self.IcecreamList = IcecreamList
    def findMinimumIcecreambyprice_list(self,IcecreamList):
        dic = {}
        for i in IcecreamList:
            dic[i.name] = i.price
        print(dic)
        m = min(dic.values())
        names=[]
        for k in dic:
            if(dic[k] == m):
                names.append(k)
        names.sort()
        if(len(names)>0):
            return names[0]
        else:
            return "no icecream found"

    def sortIcecreamByid(self):
       l = []
       flag = 0
       for i in IcecreamList:
           l.append(i.id)
           flag = 1
       l.sort()
       if flag ==0:
           return None
       else:
           return l

n = int(input())
IcecreamList = []
for i in range(n):
    id = int(input())
    price = int(input())
    name = input()
    quantityInGms = int(input())
    category = input()
    icecreamObj = Icecream(id,price,name,quantityInGms,category)
    IcecreamList.append(icecreamObj)

ans1 = IcecreamStore(IcecreamList)
print(ans1.findMinimumIcecreambyprice_list(IcecreamList))
print(ans1.sortIcecreamByid())

'''
Input:
02
01
10
vanila
200
indian
02
20
chocobar
300
italian

Output:
vanila
[1, 2]

'''

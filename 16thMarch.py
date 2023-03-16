class Container:
    def __init__(self,id,length,breadth,height,pricePerSq):
        self.id = id
        self.length = length
        self.breadth = breadth
        self.height = height
        self.pricePerSq = pricePerSq
    def volume(self):
        v = (self.length*self.breadth*self.height)
        
        return v
class PackagingCompany:
    def __init__(self,listOfContainer):
        self.listOfContainer = listOfContainer
    def findCCost(self,value):
        for i in listOfContainer:
            if i.id == value:
                call = i.volume()
                cost = (call * i.pricePerSq)
                return cost
            else:
                return None 
    def findLargestC(self):
        l1 = []
        for i in listOfContainer:
            call = i.volume()
            l1.append(call)
        # print(l1)
        m = max(l1)
        l2 = []
        for i in self.listOfContainer:
            call = i.volume()
            if call == m:
                l2.append(i.id)
                l2.append(call)
        return l2

n = int(input())
listOfContainer = []
for i in range(n):
    id = int(input())
    length = int(input())
    breadth = int(input())
    height = int(input())
    pricePerSq = int(input())
    objContainer = Container(id,length,breadth,height,pricePerSq)
    listOfContainer.append(objContainer)


value = int(input())
packagingCompanyObj = PackagingCompany(listOfContainer)
ans1 = packagingCompanyObj.findCCost(value)
if ans1:
    print(f"Price Of Container with id {value} is : ",ans1)
else:
    print("No Container")
ans2 = packagingCompanyObj.findLargestC()
for i in range(len(ans2)):
    print(ans2[i],end=' ')



'''

Input:
2
1
2
3
4
10
2
5
6
7
20
1

Output:
Price Of Container with id 1 is :  240
2 210
'''
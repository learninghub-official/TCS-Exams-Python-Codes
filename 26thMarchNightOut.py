'''

class Doctor:
    def __init__(self,docId,name,spec,consultfee):
        self.docId = docId
        self.name = name
        self.spec = spec
        self.consultfee = consultfee
class Hospital:
    def __init__(self,Docdb):
        self.Docdb = Docdb
        # self.listDoc = listDoc
    def searchbyDocName(self,userName):
        for i in Docdb.values():
            for j in i:
                if j.name.lower() == userName.lower():
                    print(j.docId , j.name , j.spec , j.consultfee)
    def calc(self,userSpec):
        for i in Docdb.values():
            c = 0
            for j in i:
                if j.spec.lower() == userSpec.lower():
                    c += j.consultfee
            return c 


listDoc = []
for i in range(int(input())):
    docId = int(input())
    name = input()
    spec = input()
    consultfee = int(input())
    Docdb = {}
    hospitalSerialNumber = '02213'
    objDoc = Doctor(docId,name,spec,consultfee)
    listDoc.append(objDoc)
    Docdb[hospitalSerialNumber] = listDoc
userName = input()
userSpec = input()
objHospital = Hospital(Docdb)
ans1 = objHospital.searchbyDocName(userName)
ans2 = objHospital.calc(userSpec)
if ans2:
    print(ans2)
else:
    print("No Doctor Found!")



'''
'''
Input:
5
90901
Govind
ENT
500
90902
Madhuri
dermitologist
700
90903
Divya
Gynaecologist       
600
90904
Suryam
Cardiologist
900
90905
Madhuri
Cardiologist
1000
Madhuri
cardiologist

Output:

90902 Madhuri dermitologist 700
90905 Madhuri Cardiologist 1000
1900

'''

class laptop:
    def __init__(self,id,brand,osType,price,rating):
        self.id = id
        self.brand = brand 
        self.osType = osType
        self.price = price
        self.rating = rating
class Solution:
    def __init__(self,list):
        self.list = list
    def CountLaptop(slef,userBrand):
        c = 0
        for i in list:
            if i.brand.lower()== userBrand.lower():
                c+=1
        return c
    def SearchLaptopbyosType(self,userOs):
        l1 = []
        for i in list:
            if i.osType.lower() == userOs.lower():
                l1.append(i)
            # l2 = l1.sort()
        for j in l1:
            print(f"{j.id} {j.rating}")
            # print(j.id,j.rating)

                
list = []
for i in range(int(input())):
    id = int(input())
    brand =  input()
    osType = input()
    price = float(input())
    rating = int(input())
    objLaptop = laptop(id,brand,osType,price,rating)
    list.append(objLaptop)
userBrand = input()
userOs = input()
objSol = Solution(list)
ans1 = objSol.CountLaptop(userBrand)
if ans1:
    print(ans1)
else:
    print("No Laptop found")

ans2 = objSol.SearchLaptopbyosType(userOs)



'''
Input:
4
123
HP
windows
35000
5
124
Apple
Mac Os
70000
5
125
Dell
Ubuntu
30000
4
126 
HP
windows
40000
4
HP

Output:

2
123 5
126 4
'''

'''
n = input()
j = ''
for i in range(len(n)):
    if i%2 == 0:
        pass
    else:
        j += n[i]
print(j)
        # print(n[i],end="") 

'''

'''

Input:
Hey There!

Output:
e hr!

'''

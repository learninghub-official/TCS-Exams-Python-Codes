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
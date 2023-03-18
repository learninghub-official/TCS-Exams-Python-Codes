class iqtest:
    def __init__(self,id,name,mage,page):
        self.id = id
        self.name = name
        self.mage = mage
        self.page = page

class hex:
    def __init__(self,l):
        self.l=l

    def iqcalc(self):
        for i in l:
            iq = (i.mage/i.page)*100
            print(f"{i.name} : {iq}")

l = []
for i in range(int(input())):
    id = int(input())
    name = input()
    mage = int(input())
    page = int(input())
    obj = iqtest(id,name,mage,page)
    l.append(obj)
hexobj = hex(l)
ans1 = hexobj.iqcalc()
'''

Input:
3
27    
lavish
20
13
08
darlish
17
13
16
shona
22
11

Output:
lavish : 153.84615384615387
darlish : 130.76923076923077
shona : 200.0

'''
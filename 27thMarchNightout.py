class vegitable:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
class Store:
    def __init__(self,list):
        self.list = list
    def catrgorizevegialphabates(self,n):
        for i in list:
            if(i.price)>=n:
                print("Expensive")

list = []
for i in range(int(input())):
    name = input()
    price = float(input())
    quantity = int(input())
    objV = vegitable(name,price,quantity)
    list.append(objV)
n = int(input())
objS = Store(list)
ans1 = objS.catrgorizevegialphabates(n)

'''

5
corn
20.0
30
onion
10.0
15
potato
30.0
10
cucumber
5.0
10
brocolli
24.5
8
5
Expensive
Expensive
Expensive
Expensive
Expensive
'''
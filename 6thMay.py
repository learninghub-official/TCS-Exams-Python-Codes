'''
def m (n1,n2):
    l3 = []
    
    for i in n1:
        if i in n2:
            l3.append(i)
    l4 = set(l3)
    # return l4
    s = ''
    if len(l4) == 0:
        print("No number Found !")
    else:
        for i in l4:
            s = s+(i) +' '
        print("Answers:",s)
                

n1 = input().split(",")
n2 = input().split(",")
l1 = []
# for i in n1:
#     l1.append(int(input()))

l2 = []
# for i in range(n2):
#     l2.append(int(input()))

ans = m(n1,n2)
# s = ''
# if len(ans) == 0:
#     print("No number Found !")
# else:
#     for i in ans:
#         s = s+str(i) +' '
#         print("Answers: ",s)

# another approach


# x=input()
# y=input()
# x1 =x.split(",")
# y1 =y.split(",")
# l1=[]
# l2=[]
# for i in x1:        
#     if i in l1:
#         pass
#     else:
#         l1.append(i)
# for i in y1:
#     if i in l2:
#         pass
#     else:
#         l2.append(i)
# l3=[]
# for i in l1:
#     if i in l2:
#         l3.append(i)
# s=''
# if len(l3)==0:
#     print('No Number Found')
# else:
#     for i in l3:
#         s= s+i+" "
#     print(s)

'''


class C1:
    def __init__(self,runnername,nameofclub,distance,time):
        self.runnername = runnername
        self.nameofclub = nameofclub
        self.distance = distance
        self.time = time
class C2:
    def __init__(self,list):
        self.list = list
    def m1(self,userpace):
        l2 = []
        for i in list:
            pace = (i.distance / i.time )
            if pace > userpace:
                l2.append(i.runnername)
        if len(l2) == 0:
            print("Not Found")
        else:
            for i in l2:
                print(i)



n = int(input())
list= []
for i in range(n):
    runnername = input()
    nameofclub = input()
    distance = int(input())
    time = int(input())
     
    obj1 = C1(runnername,nameofclub,distance,time)
    list.append(obj1)
userpace = int(input())
obj2 = C2(list)
ans = obj2.m1(userpace)

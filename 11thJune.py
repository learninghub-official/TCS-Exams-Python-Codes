class wweplayer:
    def __init__(self,rank,fights,weight,name):
        self.rank = rank
        self.fights = fights
        self.weight = weight
        self.name = name
class wweLeague:
    def __init__(self,leaguename , list1):
        self.leaguename = leaguename
        self.list1 = list1
    def findmaxplayerbyfights(self):
        l1 = []
        for i in list1:
            l1.append(i.fights)
        m = max(l1)
        for i in list1:
            if i.fights == m:
                print(i.name)
        # # l1 = []
        # for i in list1:
        #     s = sorted(list1, key=lambda x:x.fights ,reverse=True)
        # if s == []:
        #     return None
        # else:
        #     for i in s:
        #         print(i.rank)
        #         print(i.fights)
        #         print(i.weight)
        #         print(i.name)

        # s = sorted(self.list1, key=lambda x: x.fights, reverse=True)
        # if not s:
        #     return None
        # else:
        #     for i in s:
        #         print(i.rank)
        #         print(i.fights)
        #         print(i.weight)
        #         print(i.name)

        # max_fights = 0
        # max_player = None
        # for i in self.list1:
        #     if i.fights > max_fights:
        #         max_fights = i.fights
        #         max_player = i

        # if max_player is None:
        #     return None
        # else:
        #     print("Player with the maximum number of fights:")
        #     print(f"Rank: {max_player.rank}")
        #     print(f"Fights: {max_player.fights}")
        #     print(f"Weight: {max_player.weight}")
        #     print(f"Name: {max_player.name}")
            
    def sortPlayerbyRank(self):
        l3 = []
        for i in self.list1:
            l3.append(i.rank)
        # x = l3.sort()
        l3.sort()
        for i in l3:
            print(i)
        
n = int(input())
list1 = []
for i in range(n):
    rank = int(input())
    fights = int(input())
    weight = int(input())
    name = input()
    obj1 = wweplayer(rank,fights,weight,name)
    list1.append(obj1)
obj2 = wweLeague("Mayank's League",list1)
print("Max players by fights")
ans1 = obj2.findmaxplayerbyfights()
print("sort players by rank")
ans2 = obj2.sortPlayerbyRank()


'''    
3
32
12
43 
mayank
54
2
33
nupur
56
1
21
xyz

'''

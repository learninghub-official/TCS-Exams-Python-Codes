class Pepper :
    def __init__(self,name,color,SHI,price):
        self.name = name
        self.color = color
        self.SHI = SHI
        self.price = price
class Store:
    def __init__(self,username,list1):
        self.username = username
        self.list1 = list1
    def findSpiciestPepper(self):
        l1 = []
        for i in list1:
            l1.append(i.SHI)
        m = max(l1)
        for j in list1:
            if j.SHI >= 14000 and j.SHI == m:
                print(f"{j.name} with {j.color} of SHI : {j.SHI}")
                # print(j.name)
                # print(j.color)
                # print(j.SHI)
                # print(j.price)
        else:
            return None


    def SortPepperByprice(self):
        l2 = sorted(list1 , key = lambda  x : x.price , reverse = False)
        for i in l2:
            print(i.name)
            print(i.price)
        else:
            return None

n = int(input())
list1 = []
for i in range(n):
    name = input()
    color = input()
    SHI = int(input())
    price = float(input())
    objpepper = Pepper(name,color,SHI,price)
    list1.append(objpepper)
# username = input()
objStore = Store('Mayank',list1)
print("\n")
print("Spiciest Pepper :")
ans1 = objStore.findSpiciestPepper()
print("\n")
print("Sorted Pepper by price :")
ans2 = objStore.SortPepperByprice()
    



'''
Input:
3
corona
red
15000 
32
nupur
green
42350
90
greenchilli
yellow
12343
43

Output:

Spiciest Pepper :
nupur with green of SHI : 42350

Sorted Pepper by price :
corona
32.0
greenchilli
43.0
nupur
90.0

'''


# class wweplayer:
#     def __init__(self,rank,fights,weight,name):
#         self.rank = rank
#         self.fights = fights
#         self.weight = weight
#         self.name = name
# class wweLeague:
#     def __init__(self,leaguename , list1):
#         self.leaguename = leaguename
#         self.list1 = list1
#     def findmaxplayerbyfights(self):
#         l1 = []
#         for i in list1:
#             l1.append(i.fights)
#         m = max(l1)
#         for i in list1:
#             if i.fights == m:
#                 print(i.name)
#         # # l1 = []
#         # for i in list1:
#         #     s = sorted(list1, key=lambda x:x.fights ,reverse=True)
#         # if s == []:
#         #     return None
#         # else:
#         #     for i in s:
#         #         print(i.rank)
#         #         print(i.fights)
#         #         print(i.weight)
#         #         print(i.name)

#         # s = sorted(self.list1, key=lambda x: x.fights, reverse=True)
#         # if not s:
#         #     return None
#         # else:
#         #     for i in s:
#         #         print(i.rank)
#         #         print(i.fights)
#         #         print(i.weight)
#         #         print(i.name)

#         # max_fights = 0
#         # max_player = None
#         # for i in self.list1:
#         #     if i.fights > max_fights:
#         #         max_fights = i.fights
#         #         max_player = i

#         # if max_player is None:
#         #     return None
#         # else:
#         #     print("Player with the maximum number of fights:")
#         #     print(f"Rank: {max_player.rank}")
#         #     print(f"Fights: {max_player.fights}")
#         #     print(f"Weight: {max_player.weight}")
#         #     print(f"Name: {max_player.name}")
            
#     def sortPlayerbyRank(self):
#         # sorted in assending order 
#         l3 = []
#         for i in self.list1:
#             l3.append(i.rank)
#         # x = l3.sort()
#         l3.sort()
#         for i in l3:
#             print(i)

#         # sorted in decending order
# #         sorted_players = sorted(self.list1, key=lambda x: x.rank, reverse=True)
# #         for player in sorted_players:
# #             print(f"Rank: {player.rank}")
# #             print(f"Fights: {player.fights}")
# #             print(f"Weight: {player.weight}")
# #             print(f"Name: {player.name}")
            
# n = int(input())
# list1 = []
# for i in range(n):
#     rank = int(input())
#     fights = int(input())
#     weight = int(input())
#     name = input()
#     obj1 = wweplayer(rank,fights,weight,name)
#     list1.append(obj1)
# obj2 = wweLeague("Mayank's League",list1)
# print("Max players by fights")
# ans1 = obj2.findmaxplayerbyfights()
# print("sort players by rank")
# ans2 = obj2.sortPlayerbyRank()


'''   
Input:
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

Output:
Max players by fights
mayank
sort players by rank
32
54
56

'''

class pan:
    def __init__(self,id , material,brand,price,capacity):
        self.id = id 
        self.material = material
        self.brand = brand
        self.price = price
        self.capacity = capacity
class Solution:
    def __init__(self,list):
        self.list = list
    def CostliestPan(self,userMaterial):
        l = []
        for i in list:
            if i.material.lower() == userMaterial.lower():
                l.append(i.price)
        for j in l:
            if j == max(l):
                return i.id
            
    def discounted(self,userBrand):
        for i in list:
            if i.brand.lower() == userBrand.lower() and 1000 > i.capacity > 500:
                i.price -= ((i.price*20)/100)
                return i.price
            elif i.brand.lower() == userBrand.lower() and i.capacity >1000:
                i.price -= ((i.price*26)/100)
                return i.price
list = []
for i in range(int(input())):
    id = input()
    material = input()
    brand = input()
    price = int(input())
    capacity = int(input())
    objPan = pan(id,material,brand,price,capacity)
    list.append(objPan)
userMaterial = input()
userBrand = input()
objSol = Solution(list)
ans1 = objSol.CostliestPan(userMaterial)
ans2 = objSol.discounted(userBrand)
if ans1:
    print(ans1)
else:
    print("No pan of this Material Found !")
if ans2:
    print(ans2)
else:
    print("No pan found of thid brand !")


'''  
Input 1:
5
id23
brass
a
200
120
id24
copper
b
300
1130
id25
chromium
c
400
640
id26
steel
d
500
950
id27
steel
e
800
950
steel
d

Output 1:
id27
400.0

################

Input 2:
5
id23
brass
a
200
120
id24
copper
b
300
1130
id25
chromium
c
400
640
id26
steel
d
500
950
id27
steel
e
800
950
gold 
d

Output 2:
No pan of this Material Found !
400.0
'''

# def find_second_index(nums, num_to_find):
#     first_index = nums.index(num_to_find)  # find the first occurrence of the number
#     second_index = nums.index(num_to_find, first_index+1) # find the second occurrence of the number
#     return second_index

# # Example usage
# my_list = [3, 7, 2, 5, 2, 8, 2, 9]
# num = 2
# second_index = find_second_index(my_list, num)
# print("The second occurrence of", num, "is at index", second_index)

'''

l = []
for i in range(int(input())):
    l.append(int(input()))
n = int(input())
first= l.index(n)
second = l.index(n,first+1)
print(second)

'''

'''
Input 1:
5
3
4
3
7
4
3

Output:
2

'''

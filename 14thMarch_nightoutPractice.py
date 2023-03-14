# Find the index of the given string in the list

'''n = int(input())
# print(n)
l = []
for i in range(n):
    l.append(input())
m = input()
print("The position of the searched string is: ",l.index(m))
'''

'''
Input:
4
Hello GoodMorning
abcd123Fghy
India
Progoti.c
India

Output:
The position of the searched string is:  2

'''

# Another Method for the same Problem
'''
n = int(input())
# print(n)
l = []
for i in range(n):
    l.append(input())
m = input()
for i in range(0,len(l)):
    if l[i].lower() == m.lower():
        print("The position of the searched string is: ",i)
'''


'''

n = int(input())
l =[]
for i in range(n):
    l.append(input())
for i in l:
    if i == i[::-1]:
        print(i)
        
'''



'''
Input:
3
malayalam
radar
nitish

Output:

'''



def check(l):
    l1 = []
    for i in l:
        if i == i[::-1]:
            l1.append(i)
    return l1

n = int(input())
l =[]
for i in range(n):
    l.append(input())

if check(l):
    for i in check(l):
        print(i)
else:
    print("Not Found !")

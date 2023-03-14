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

n = int(input())
# print(n)
l = []
for i in range(n):
    l.append(input())
m = input()
for i in range(0,len(l)):
    if l[i].lower() == m.lower():
        print("The position of the searched string is: ",i)

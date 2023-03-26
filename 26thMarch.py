'''

n = input().split(",")
l = []
for i in n:
    l.append(i)
for i in range(len(l)):
    print(l[0],l[i+2])
    break

'''
"""

Input:
1,2,3,4,5,6 ,23, 09

Output:
1 3

"""
'''
l1 = []
l2 = []
for i in range(int(input())):
    serial = int(input())
    km = int(input())
    type = input().upper()
    availability = input().upper()
    l1.append(type)
    l2.append(availability)
print(l1)
# l3 = set(l1) set does not work while indexing so it should not be used here
l3 = []
for i in l1:
    if i in l3:
        pass
    else:
        l3.append(i)
print(l3)
l4 = []
for i in l3:
    c = 0
    for j in range(len(l2)):
        print(l2[j])
        if l1[j].lower() == i.lower() and l2[j].lower() == 'Available'.lower():
                c +=1
    l4.append(c)
for i in range(len(l3)):
    print(l3[i].capitalize(),":",l4[i])
'''


"""

Input:
5
1
10000
Electric
available
2
20000
Diesel
NotAvailable 
3
30000
Electric
Available
4
20000
petrol
available
5
30000
Electric
Available

Output:
['ELECTRIC', 'DIESEL', 'ELECTRIC', 'PETROL', 'ELECTRIC']
Electric : 3
Diesel : 0
Petrol : 1

"""

'''l = []
for i in range(int(input())):
    l.append(input())
n = input()
for i in range(len(l)):
    if l[i].lower() == n.lower():
        print("INDEX : ",i)
'''

'''

4
Good morning
abcdefg
India
mayank@tcs.com
india

'''
'''
n = input()
counta = 0
counts = 0
for i in n:
    if i.isalpha() == True :
        counta +=1
    elif i.isspace() == True:
        counts +=1
print(f"Numbre of spaces are : {counts}")
print(f"Numbre of letters are : {counta}")

'''

'''
Good morning
Numbre of spaces are : 1
Numbre of letters are : 11
'''

'''n = input()
v = ['a','e','i','o','u']
# v = 'aeiouAEIOU'
count = 0
l1 = []
for i in n:
    if i.isalpha():
        if i.lower() in v:
            count+=1
print("Number of vovels are :",count)
'''

'''
Good morning
Number of vovels are : 4
'''

'''
n = input()
s = 0
for i in n:
    s = s+(int(i))
print(s)
if s%3==0:
    print("True")
else:
    print("False")
'''

'''
333
9
True

'''


'''
l = []
for i in range(int(input())):
    n = input().split()
    l +=n
# print(l)
s = input()
c = 0
for i in l:
    if i.lower() == s.lower():
        c +=1
if c:
    print(c)
else:
    print("Target Not Found")

'''
'''
4
Hello World!
hi I am Hello
hello this is Hello
Tcs Explore
hello

4
'''



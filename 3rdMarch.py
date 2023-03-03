# Count the number of prime in the given list using sympy module

"""
from sympy import *

n = int(input())
l=[]
for i in range(n):
    l.append(int(input()))

print(l)
count = 0
for i in l:
    if(isprime(i) == True):
        count +=1

    else:
        # print("notFound !")
        pass

print("Total Prime numbers in the list are = ",count)

"""


# Count the number of prime in the given list without using sympy module


'''

n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

prime = []
for i in range(0,len(l)):
    for j in range(2,l[i]):
        if l[i]%j==0:
            # print("Not Prime")
            pass
            break
    else:
        prime.append(l[i])
    count = len(prime)
print(prime)
print(count)

'''

# count the number of time a given word repeated in users input string 

n = int(input())
l=[]
for i in range(n):
    j = (input().split(" "))
    l= l+j
print(l)
word = input()
count = 0
for i in l:
    if i.lower() == word.lower():
        count+=1
if count!=0:
    print("Count Of Given Word : ",count)
else:
    print("Not Found")


"""

sample input 1:
3                 
hello Mayank
Hello monu
Good Morning
['hello', 'Mayank', 'Hello', 'monu', 'Good', 'Morning']
hello

Output:
Count Of Given Word :  2


sample input 2:
3                 
hello Mayank
Hello monu
Good Morning      
['hello', 'Mayank', 'Hello', 'monu', 'Good', 'Morning']
gavish

Output:
Not Found

"""

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


# Print All Palindrom Strings present in the list 

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
'''

"""

Create a function count_words() which takes a string as input and creates a dictionary with a word in the string as a key and its value as the number of times the word is repeated in the string. It should return the dictionary.
eg: “hello hi hello world hello” 
dict={hello:3,hi:1,word:1}

Create another function max_accurance_word() which takes a string as input and returns the word which is occurring a maximum number of times in the string. Use the count_words function inside this function.

"""




def count_words(string):
    l=string.split()
    s=set(l)
    d={}
    for i in s:
        x=l.count(i)
        d[i]=x
    return d
def max_occurance(string):
    d=count_words(string)
    l1=[]
    for i in d.values():
        l1.append(i)
    max1=max(l1)
    for i in d.keys():
        if d[i]==max1:
            return i
string=input() 
print(max_occurance(string))

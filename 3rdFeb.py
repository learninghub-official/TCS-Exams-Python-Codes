#1 use of split() and replace() function 


'''

strng = input()
l = strng.split()
j=[]
# print(l)
for i in l:
    if 'il' in i:
        k = i.replace('il','')
        # print(k)
        j.append(k)
    else:
        j.append(i)

s = ''
for i in j:
    s = s+i+' '
print(s)

    
'''

'''
input:
Mayank is happyil

output:
Mayank is happy

'''

#2 finding the second largest number in the list

'''

n = int(input())
l=[]
for i in range(n):
    l.append(int(input()))
# print(l)
for i in l:
    l.sort()
    
print(l)
print("Second Largest Number : ",l[-2])

'''

'''
Input:
5
23
87
45
12
75        
[12, 23, 45, 75, 87]

Output:
Second Largest Number :  75
'''

#3 Calculate the sum of digits of an integer input

"""

n = (input())
s=0
for i in n:
    s += int(i)
# print(s)
if s%3==0:
    print('True')
else:
    print("False")


"""


"""
Input:
33

Output:
True
"""


#4 Print the position or index of the given string

"""
n = int(input())
l=[]
for i in range(n):
    l.append(input())
print(l)
m = input()
for i in range(len(l)):
    if l[i] == m:
        print(i)
        break

"""

#5 check palindrome in list of strings and return it 

'''

n = int(input())
l=[]
for i in range(n):
    l.append(input())

for i in l:
    if i == i[::-1]:
        print("Palindrome Word = ",i)

'''
        

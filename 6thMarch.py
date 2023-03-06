# Accenture Python Coding question 11 august 2021

r = int(input())
unit = int(input())
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

print("Numbers of Rats",r)
print(f"Each Rat consume {unit} units :" )
print(f"{n} Houses with units available : ",arr)

totalunitrequired = unit*r

s =0 
j = 0
for i in arr:
    if s>totalunitrequired:
        # print(j)
        break
    else:
        s+=i
        j+=1


print("Here is the count of houses : ",j)



"""

Input:
7
2
8
2
8
3
5
7
4
1
2

Output:
Numbers of Rats 7
Each Rat consume 2 units :
8 Houses with units available :  [2, 8, 3, 5, 7, 4, 1, 2]
Here is the count of houses :  4

"""

"""
# pair socks with colors 

l1 = []
n = int(input())
for i in range(n):
    l1.append(int(input()))
print(n)
print(l1)
l2 = set(l1)
s = 0
for i in l2:
    s = s +int((l1.count(i)/2))
print(s)

"""
    
    
    
    
"""
input:
9
10
20
20
10
10
30
50
10
20
output:
9
[10, 20, 20, 10, 10, 30, 50, 10, 20]
3
"""

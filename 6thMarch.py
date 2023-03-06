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
# print(totalunitrequired)
# print(arr)
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

    

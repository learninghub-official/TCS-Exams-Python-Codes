
def indexcheck(m):
    for j in range(len(l)):
        if l[j].lower() ==m.lower():
            return j

n = int(input())
l = []
for i in range(n):
    l.append(input())

m = input()
ans = indexcheck(m)
if ans:
    print(f"Position of the searched string is:{ans}")    
else:
    print("Not found")



'''
Input:
4          
Hello Good Morning
abcd123Fghy
India
progoti.c
India

Output:
Position of the searched string is:2

'''
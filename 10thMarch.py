n = int(input())
l = []
for i in range(n):
    l.append(input())
for i in range(len(l)):
    count1 = 0
    count2 = 0
    for j in l:
       
        if j.isidentifier() or (j.isspace()):
                count1 +=1
        else:
            count2 +=1
            # print("Invalid: ",j)

print("Valid: ",count1)
print("Invalid: ",count2)

'''

Input:
4
Hello Good Morning
abcd123Fghy
India
progoti.c

Output:
Valid:  2
Invalid:  2
'''




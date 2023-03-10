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

Explaination:
Example :
If the string given as argument is "Hello Good Morning", the function will return True.
If the string given as argument is "Purabi@gmail.com", the function will return False.

'''



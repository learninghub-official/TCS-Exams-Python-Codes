
# Wrong approach for this problem

'''
s = "Let's take LeetCode Contest"
print(s)

for i in s:
    l = s.split()
print(l)
x = len(l)
print(x)
m = []
for i in range(x):
    for j in l:
        lx =[]
        for k in j:
            lx.append(k)

        lx.reverse()

        m += lx
    print(m)
    final = ""
    final = " ".join(m)

    print(final)

    break
 '''   

# right approach for this problem 


s = "Let's take LeetCode Contest"
print(s)
l = s.split()
l1 = []
for i in l:
    l1.append(i[::-1])
# print(l1)
ss = ""
for i in l1:
    ss+=' '+i
print(ss)

'''

Output:
Let's take LeetCode Contest
 s'teL ekat edoCteeL tsetnoC

'''

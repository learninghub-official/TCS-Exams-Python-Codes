


n = int(input())
l = []
if n >9:
    for i in range(9,1,-1):
        while n%i == 0:
            l.append(i)
            n = n/i
        # break
    j = l[::-1]
    s = ''
    for i in j:
        s = s+str(i)
    print(int(s))
else:
    print(n+10)



'''

Input:
500 

Output:
4555

Explaination:

4*5*5*5 = 500


'''
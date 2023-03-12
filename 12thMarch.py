# Question 1

'''

Input:
Hyper12345Lower100

Output:
['HyperLower',12345100]

'''
'''
strng = input()

final = []
alpha = ''.join(i for i in strng if i.isalpha())
num = ''.join(i for i in strng if i.isdigit())
if len(alpha)!=0:
    final.append(alpha)
if len(num)!=0:
    final.append(int(num))
print(final)

'''

# Question 2

'''
Input:
arr = [1,2,2,1,1,3]

Output:
True

'''

'''arr = [1,2,2,1,1,3]
dic = {}
l1 = []
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] =1
for k ,v in dic.items():
    l1.append(v)
print(len(set(l1))==len(l1))
        '''

# Question 3 

nums = [6,4,5,1]
l1 = []
for i in range(len(nums)):
    # print(i)
    for j in range(i+1,len(nums)):
        # print("j = ",j)
        l1.append((nums[i]-1)*(nums[j]-1))
print(max(l1))



'''

Output:
20

'''

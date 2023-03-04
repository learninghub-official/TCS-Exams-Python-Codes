
# print the word which occured the maximum time in the string



strng = input()
l = strng.split()
setj = set(l)
# print(setj)
dict = {}
for i in setj:
    count = 0
    for j in l:
        if j.lower() == i.lower():
            count = count+1
    dict[i] = count
# print(dict)
l1 = []
for i in dict:
    l1.append(dict[i])
# print(l1)
m = max(l1)
for i in dict:
    if dict[i] == m:
        print(i)




"""
Input:
hello hi word hello

Output:
hello

"""

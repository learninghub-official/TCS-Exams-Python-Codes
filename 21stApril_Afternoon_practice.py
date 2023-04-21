# TCS IPA 9 APRIL 15 MARKS QUESTION

s1 = input()
s = s1.split(" ")
l1 = []
length = len(s)
vowels = ['a','e','i','o','u']
for i in s1:
    if i in vowels:
        pass
    else:
        l1.append(i)
x = ''
for i in l1:
    x += i
print(x)
print(length)


"""
Input:
hello worldaeiu 123

Output:
hll wrld 123
3
"""

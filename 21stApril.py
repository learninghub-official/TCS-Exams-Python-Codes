'''

# 35 marks ninja to digital asked in 22 march 2023 question

n1 = int(input())
s = input().split(" ")


n2 = int(input())
s1 = input().split(" ")

l1 = []
for i in s:
    if i in s1:
        pass
    else:
        l1.append(i)
ans = ''
for i in l1:
    ans = ans + i + ' '
print("Missing songs :",ans)
            
# print("Songs Of Old Playlist : ",s)
# print("Songs Of Old Playlist : ",s1)

'''

'''

input 
8 
1 2 3 4 5 6 7 8 
5
2 5 7 8 6

output
1 3 4


'''

# Ipa 15 marks question asked on 30th march 2023

s = input()
counta = 0
countn = 0 
for i in s:
    if i.isalpha():
        counta +=1
    elif i.isdigit():
        countn +=1
if counta > countn and countn!=0:
    print("Alphabets :",counta)
    print("Numbers :",countn)
elif countn > counta and counta!=0:
    print("Numbers :",countn)
    print("Alphabets :",counta)
elif counta > countn and countn ==0:
    print("Alphabets :",counta)
elif countn > counta and counta==0:
    print("Numbers :",countn)

    

'''
input 1 :
23455fdf

Output 1:
Numbers : 5
Alphabets : 3

input 2 :
dsfg23

Output2:
Alphabets : 4
Numbers : 2

input 3 :
342345

Output 3:
Numbers : 6

input 4 :
dfdg

Output 4:
Alphabets : 4
'''

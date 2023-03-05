# 35 Marks Question Of TCS IPA held on 25 Feb 2023

'''

class Film :
    def __init__(self,filmStudio , filmName,Price,Language):
        self.filmStudio = filmStudio
        self.filmName = filmName
        self.price = price
        self.Language = Language
    def search_print(self,list):
        flag = 0
        for i in list:
            if i.Language.lower() == 'English'.lower() and i.price >= 500:
                flag = 1
                print(i.filmName , i.filmStudio)
                
                
        if flag==0:
            print("Movie Not Found")
        # else:


n = int(input())
list = []
for i in range(n):
    filmStudio = input()
    filmName = input()
    price = int(input())
    Language = input()

    FilmObj = Film(filmStudio , filmName,price,Language)
    list.append(FilmObj)
FilmObj.search_print(list)


'''

"""

input 1:
2
MayankStudio
Ironman
200
Hindi
GavishStudio
Thor
300
Hindi

Output:
Movie Not Found

##########################
 
intput 2:
2
MayankStudio
Ironman
6000
english
GavishStudio
Thor
300
Hindi

output:
Ironman MayankStudio
"""

# Ninja To digital Level Question 

# Finding Sum Of Diagonal of Matrix of 3*3 and Substract their values 

'''

n = int(input())
matirx = []
for i in range(n*n):
    matirx.append(int(input()))
diagonal1 = []
diagonal2 = []

diagonal1.append(matirx[0])
diagonal1.append(matirx[4])
diagonal1.append(matirx[8])

diagonal2.append(matirx[2])
diagonal2.append(matirx[4])
diagonal2.append(matirx[6])

print(diagonal1)
print(diagonal2)
s1 = sum(diagonal1)
s2 = sum(diagonal2)

ans = abs(abs(s1)-abs(s2))
print(ans)


'''

'''

input:
3
11
2
-3
20
7
5
-9
7
6

Output:
[11, 7, 6]
[-3, 7, -9]
19

'''
#Another Method to Solve this
# Finding Sum Of Diagonal of Matrix of 3*3 and Substract their values

l = []
for i in range (int (input ( ) )):
    j =input().split(" ")
    l=l+j
s =0
for i in range (len (l)) :
    if i == 0 or i==4 or i==8:
        s=s+int (l[i])
s1=0
for i in range (len (l)) :
    if i==2 or i==4 or i==6:
        s1=s1+int(l[i])
print (abs (abs (s)-abs (s1)))



'''
input:
3
11 2 -3
20 7 5
-9 7 6

output:
19

'''

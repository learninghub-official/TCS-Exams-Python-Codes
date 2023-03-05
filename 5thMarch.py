# 35 Marks Question Of TCS IPA held on 25 Feb 2023

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

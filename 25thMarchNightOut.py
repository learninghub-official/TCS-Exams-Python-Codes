n = int(input())
l1 = []
if n>3:
    for i in range(n):
        l1.append(int(input()))
    l1.sort()
#     print(l1)
    n=len(l1)
    for j in l1:
        print("Second largest: ",l1[n-2])
        print("Second Smallest: ",l1[j])
        break

else:
    print("N should be greater than 3")

    
"""
Input 1:
5
1
2
3
4
6

Output:
Second largest:  4
Second Smallest:  2


Input 2:
3

Output:
N should be greater than 3

""" 

'''
class Movie:
    def __init__(self,id,director,rating,budget):
        self.id = id
        self.director = director
        self.rating = rating
        self.budget = budget
class Solution:
    def __init__(self,list_movie):
        self.list_movie = list_movie
    def findAvgBudgetByDirector(self,user_director):
        avg = 0
        count = 0
        for i in list_movie:
            if i.director.lower() == user_director.lower():
                count +=1
                avg += i.budget
        avg = avg/count
        return avg
    def getMoviebyratingandbudget(self,user_rating,user_budget):
        for i in list_movie:
            if i.rating == user_rating and i.budget == user_budget and i.budget%i.rating ==0:
                # print(i)
                print(i.id , i.director , i.rating , i.budget)
        
n = int(input())
list_movie = []
for i in range(n):
    id = int(input())
    director = input()
    rating = int(input())
    budget = int(input())
    objMovie = Movie(id,director,rating,budget)
    list_movie.append(objMovie)
user_director = input()
user_rating = int(input())
user_budget = int(input())
objSolution = Solution(list_movie)
ans1 = objSolution.findAvgBudgetByDirector(user_director)
if ans1:
    print(ans1)
else:
    print("No movie of this director")
ans2 = objSolution.getMoviebyratingandbudget(user_rating,user_budget)
if ans2:
    print(ans2)
'''

'''

Input:
4
101
gvm
4
100
102
shankar
5
500
103
shankar
3
50
104
gvm
5
300
gvm
5
300

Output:
200.0
104 gvm 5 300

'''


# print the word which occured the maximum time in the string

# 15 Marks Question
'''


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

'''




"""
Input:
hello hi word hello

Output:
hello

"""



#  35 Marks Question 
#scholar

class Scholar:
    def __init__(self,scholarId,scholarName,State,marks_list):
        self.scholarId = scholarId
        self.scholarName = scholarName
        self.State = State
        self.marks_list = marks_list
    
class ScholarResult:
    def F1(self,list_Scholar,g):
        ScholarGrade = []
        percentList = []
        TM = []
        for i in list_Scholar:
            s = 0
            for j in i.marks_list:
                s = s+int(j)
            TM.append(s)
            percentList.append(int(s/3))
        # print(percentList)
        k = 0
        
        for i in list_Scholar:
            dict = {}
            dict["scholarId"] = i.scholarId
            dict["scholarName"] = i.scholarName
            dict["TM"] = TM[k]
            if percentList[k] >=80:
                dict["G"] = "A"
            elif percentList[k] >=60 and percentList[k]<=80:
                dict["G"] = "B"
            elif percentList[k] >=50 and percentList[k] <=60:
                dict["G"] = "C"
            elif percentList[k] <50:
                dict["G"] = "D"
            dict["State"] = i.State
            ScholarGrade.append(dict)
            k+=1
        TM1= []
        for i in ScholarGrade:
            if i['G'].upper ()==g.upper ():
                TM1.append(i['TM'])
        if len (TM1)==0:
            print ("None")
        for i in TM1 [::-1]:
            for j in ScholarGrade:
                if i == j["TM"]:
                    print(j["scholarId"],j["scholarName"],j["TM"],j["G"],j["State"])
        ST=[]
        for j in ScholarGrade:
            ST.append(j["State"])
        ST = list (set (ST))
        ST = sorted (ST)
        # print (ST)
        kl =0
        for kl in ST:
            l5=[]
        for j in ScholarGrade:
            if j["State"] == kl:
                l5.append(j)
        P=0
        f=0
        for i in l5:
            if i["G"] in "ABC":
                P = P+1
            else:
                f =f+1
        k3=int ((P/len (l5) *100))
        k4 =int ((f/len (l5) *100))
        k5=str (k3) +": "+str (k4)
        print (kl, k5)
                    

            
        # print(ScholarGrade)
            
        

n = int(input())

list_Scholar = []
for i in range(n):
    scholarId = int(input())
    scholarName = input()
    State = input()
    marks_list = []
    for i in range(3):
        marks_list.append(int(input()))
    ScholarObj = Scholar(scholarId,scholarName,State,marks_list)
    list_Scholar.append(ScholarObj)

g = input()
SRobj = ScholarResult()
SRobj.F1(list_Scholar,g)

# for i in list_Scholar:
#     print(i.scholarId , i.scholarName ,i.State,i.marks_list)

# print(marks_list)


'''

Sample Input 1 :
3
01
Mayank
Haryana 
99
98
89
02
Nupur
Delhi
87
98
99
03
rohan  
goa
57
84
34
c

Output:
3 rohan   175 C goa
goa 100: 0

#####################

Sample Input 2 :
3
01
Mayank
Haryana 
99
98
89
02
Nupur
Delhi
87
98
99
03
rohan  
goa
57
84
34
A
 
Output:
2 Nupur 284 A Delhi
1 Mayank 286 A Haryana 
goa 100: 0
'''




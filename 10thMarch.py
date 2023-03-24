'''n = int(input())
l = []
for i in range(n):
    l.append(input())
for i in range(len(l)):
    count1 = 0
    count2 = 0
    for j in l:
       
        if j.isidentifier() or (j.isspace()):
                count1 +=1
        else:
            count2 +=1
            # print("Invalid: ",j)

print("Valid: ",count1)
print("Invalid: ",count2)
'''
'''

Input:
4
Hello Good Morning
abcd123Fghy
India
progoti.c

Output:
Valid:  2
Invalid:  2

'''


# 35 Marks question [Python Assessment Test given in TCS Explore]

class Employee:
    def __init__(self,employee_name,designation,salary,overTimeContribution,overTimeStatus):
        self.employee_name = employee_name
        self.designation = designation
        self.salary = salary
        self.overTimeContribution = overTimeContribution
        self.overTimeStatus = overTimeStatus
        
class Organization:
    def __init__(self,employee_list):
        self.employee_list = employee_list
    def checkElegibility(self,m):
       for i in employee_list:
            s = sum(i.overTimeContribution.values())
            if s >m:
                i.overTimeStatus = True
            print(f"{i.employee_name} {i.overTimeStatus} {s}")
    def bonus(self,k):
        l4 = []
        for i in employee_list:
            if i.overTimeStatus == True:
                l4.append(sum(i.overTimeContribution.values()))
        total = sum(l4)
        tm = total*k
        if tm:
            return tm
        else:
            # print("0")
            return 0
n = int(input())
employee_list = []
for i in range(n):
    employee_name = input()
    designation = input()
    salary = int(input())
    overTimeStatus = False
    overTimeContribution = {}
    for i in range(int(input())):
        monthname = input()
        hours = int(input())
        overTimeContribution[monthname] = hours
    EmployeeObj = Employee(employee_name,designation,salary,overTimeContribution,overTimeStatus)
    employee_list.append(EmployeeObj)
m = int(input())
k = int(input())
Organizationobj = Organization(employee_list)
ans = Organizationobj.checkElegibility(m)
# print(ans)
ans2 = Organizationobj.bonus(k)
if ans2:
    print(ans2)
else:
    print(ans2)




        
"""

Input:
5
Sunita
Faculty
23000
2
jan
4
March
6
Arun
Admin
30000
3
Feb
4
March
12
June
10
Dipak
Admin
25000
3
Jan
12
July
5
Aug
3
Balen
HR
12000
3
Jan
12
July
5
Aug
3
Tarun
HR
78000
3
Jan
12
July
5
Aug
3
18
100

"""

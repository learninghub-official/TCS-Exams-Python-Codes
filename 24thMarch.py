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
           for j in overTimeContribution:
               print(employee_list[i][])
    def bonus(self,k):
        pass
n = int(input())
overTimeContribution = {}
employee_list = []
for i in range(n):
    employee_name = input()
    designation = input()
    salary = int(input())
    overTimeStatus = False
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


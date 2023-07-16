class Album:
   def __init__(self,aname,sname,atrack,atype):
      self.sname = sname
      self.aname = aname
      self.atrack = atrack
      self.atype = atype
class song:
   def __init__(self,list1):
      self.list1 = list1
   def m1(self):
      L2 = []
      for i in list1:
         if i.aname[0].lower() == 'L'.lower() and i.atrack >= 5 and i.atype.lower() != 'Digital'.lower() :
            L2.append(i.sname)
      if L2 == []:
         print('No Albums found')
      else: 
         for j in L2:
            print(j)

list1 = []
for i in range(int(input())):
   sname = input()
   aname = input() 
   atrack = int(input())
   atype = input()
   obj1 = Album(aname,sname,atrack,atype)
   list1.append(obj1)
obj2 = song(list1)
ans = obj2.m1()


'''
Input:
3
Mayank
lforgetable    
13
pop
bohemia
ldanali
5
rock
nupur
bohiman rampasi
2
digital

Output:
Mayank
bohemia

'''

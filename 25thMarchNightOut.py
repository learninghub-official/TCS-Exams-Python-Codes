n = int(input())
l1 = []
if n>3:
    for i in range(n):
        l1.append(int(input()))
    l1.sort()
    # print(l1)
    n=len(l1)
    for j in l1:
        print("Second largest: ",l1[n-2])
        print("Second Smallest: ",l1[j])
        break

else:
    print("N should be greater than 3")

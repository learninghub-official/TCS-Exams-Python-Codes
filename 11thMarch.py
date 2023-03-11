
def indexcheck(m):
    for j in range(len(l)):
        if l[j].lower() ==m.lower():
            return j

n = int(input())
l = []
for i in range(n):
    l.append(input())

m = input()
ans = indexcheck(m)
if ans:
    print(f"Position of the searched string is:{ans}")    
else:
    print("Not found")



'''
Input:
4          
Hello Good Morning
abcd123Fghy
India
progoti.c
India

Output:
Position of the searched string is:2

'''





# string = input()
# n = int(input())

# if n <= 0:
#     print("Error: N should be greater than 0.")
# else:
#     middle = len(string) // 2
#     start = middle - n // 2
#     end = start + n
#     print(string[start:end] if end <= len(string) else string[start:])





'''

The code first prompts the user to enter a string and an integer 'n'.

It then checks whether 'n' is greater than 0. If 'n' is less than or equal to 0, it prints an error message and exits the program.

If 'n' is greater than 0, the code calculates the middle index of the string using the formula: middle = len(string) // 2. This formula calculates the floor division of the length of the string by 2, which gives the index of the middle character in the string.

The code then calculates the starting index for the 'n' characters using the formula: start = middle - n // 2. This formula calculates the floor division of 'n' by 2 and subtracts it from the middle index, which gives the index of the first character to be included in the substring.

The code then calculates the ending index for the 'n' characters using the formula: end = start + n. This formula adds 'n' to the starting index, which gives the index of the last character to be included in the substring.

Finally, the code prints the substring starting from the calculated starting index and up to the calculated ending index, or up to the end of the string if the requested characters are not available.

'''

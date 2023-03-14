
# Python3 program to
# Check if the string is pangram

def ispangram(str):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for i in alphabet:
		if i not in str.lower():
			return False
	return True
# string = "A quick brown fox jumps over the lazy dog"
string = "abcdefghijklg"
if (ispangram(string))==True:
	print("Yes")
else:
	print("No")

'''s = "A quick brown fox jumps over the lazy dog"
s = "abcdefghijkl"
l1 = []
alphabat = "abcdefghijklmnopqrstuvwxyz"
for i in s:
    if i.isalpha()==True:
        l1.append(i)
print(l1)
f = ''.join(l1)
print(f)
for i in alphabat:
    if i not in f.lower():
        print("No")
    else:
        print("Yes")
    break
'''


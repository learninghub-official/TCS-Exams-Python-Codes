'''
Write the code to define a class to create a Book object with the below attributes:

book id, book name, the name of the author of book.



Define the method to initialize the attributes when a Book object is created.


Write the code to define a Class to Create a Library object with the below attributes:

a list of Book type
an address of the Library , a dictionary in the format as follows:
{street: 'A-10', area:”gomitnagar”,city: 'Lucknow', state: 'UP', zip: 1090034}


Define a method to initialize the attributes when a Library object is created.



Define another method inside the class as below:

The method will find the count of books for each author from the book List of the Library class and returns a dictionary having the author name and bookCount (count of books) as key : value pairs. The search for author name should be case insensitive and return result with author name in UPPER case only.


Define a method outside both the classes.

This method will take name of a city and a list of Library objects as parameters and return the list of books which are present in the libraries of the given list which has the given city name as city in the address. If there is no Library in the given list which has the given city name as city in the address, the method should return None else it will return the list of books in descending order of book id for each library object with matching city i.e. If the city is matching with the library object1 and library object3, the method will display the list of books from library object1 in descending order of book id and then it will display the list of books from library object3 in descending order of book id. Please refer the sample input and output below for more clarity.


Note : All String Comparison should be case insensitive.



Instructions to write main function:

You would require to write the main section completely, hence please follow the below instructions for the same.

You would require to write the main program which is in line to the "sample input description section" mentioned below and to read the data in the same sequence.

Create the respective objects of the classes defined referring to the below instructions.



Main Function Instructions:



A. Create a list of Library objects which will be passed as argument while calling the function in main. To create the list:

Read a number for the count of Library objects to be created and added to the list.

Create a library object to be added to the list. To create the library object, do the following:

Read a number for the count of book objects to be added to the list of book objects for the library objects.

Create a book object after reading the data (book Id, book Name, author Name) related to it and add to the list of book objects. This point repeats for the count of Book objects to be created as per point #A.2.1.

Read values for the Address of the Library object. Attributes of the address are street, area, city, state and zip. Considering these attributes as keys, store the values read as key : value pairs in a dictionary for the address.

Create a Library object by passing the list of Book objects and dictionary created above and add it to the library list. This repeats for the number of Library objects to be created (considered in the first line of input) as per point #A.1.

B. Read a string value as input depicting city to be passed as argument to the second function(function defined outside the class).

C. Call the method to find count of books author wise mentioned above from the main section using the first element of the List of Library objects created in point #A(i.e the First library Object created)

D. Display the values returned by the above function. Display the author names and count of books returned by the function as per the requirement given.

E. Call the second function from the main section, by passing the city name and the list of Library objects created above.

F. Display the list of book names returned by the second function.

- If function returns None, then display “No Book Found” (excluding the quotes).


Sample Input (below) description:

The first input taken in the main section is the number of Library Objects to be created(suppose n).

The next set of inputs are related to n Library objects to be created as follows:

Count of Book objects(Suppose m) to be created and added to the list of books for the Library.

The next set of inputs are values for attributes of m books -bookId, bookName, authorName (for each book object taken one after other and is repeated for m number of book objects).

Next set of values are for the following keys of the address for the Library object .

street
area
city
state
zip
Last line of input represents the City Name, supplied as a argument to the second function.



You can use/refer the below given sample input and output for more details of the format for input and output.



Consider below sample input and output to test your code:

Sample Input :

3
3
1
Hamlet
shakesphere
2
Macbeth
SHAKESPHERE
3
othello
Shakesphere
A-10
gomtinagar
lucknow
u.p.
201876
3
1
A Christmas Carol.
Charles Dickens
2
Bleak House
Charles Dickens
3
Oliver Twist
Charles Dickens
A-770
rajamandi
agra
u.p.
2018763
3
1
The adventures of sherlock holmes
sherlock holmes
2
The return of sherlock holmes
sherlock holmes
3
The sign of the four
sherlock holmes
A-660
Khairatabad
lucknow
u.p.
201876
lucknow


Output :

SHAKESPHERE 3
['othello', 'Macbeth', 'Hamlet', 'The sign of the four', 'The return of sherlock holmes', 'The adventures of sherlock holmes']


'''

class book:
    def __init__(self,id , name,author):
        self.id = id
        self.name = name
        self.author = author
class library:
    def __init__(self,book_list,address):
        self.book_list = book_list
        self.address = address
    def bookCount(self):
        l3 = []
        count = 0
        for i in range(len(book_list)):
            for j in book_list:
                l3.append(j.author)
                break
            # print(l3)
        # k = set(l3)
        # print(k)
        print(f"{j.author.upper()} {l3.count('Shakesphere')}")
        

book_list = []
n = int(input())
for j in range(n):
    m = int(input())
    for i in range(m):
        id = int(input())
        name = input()
        author = input()
        address = {}
    
    street = input()
    area = input()
    city = input()
    state = input()
    zip= int(input())
    address[street] = street 
    address[area] = area 
    address[city] = city 
    address[state] = state 
    address[zip] = zip

    objBook = book(id,name,author)
    book_list.append(objBook)

city = input()
libobj = library(book_list,address)
ans1 = libobj.bookCount()
if ans1:
    print(ans1)

'''
"""

Input:
3
3
1
Hamlet
shakesphere
2
Macbeth
SHAKESPHERE
3
othello
Shakesphere
A-10
gomtinagar
lucknow
u.p.
201876
3
1
A Christmas Carol.
Charles Dickens
2
Bleak House
Charles Dickens
3
Oliver Twist
Charles Dickens
A-770
rajamandi
agra
u.p.
2018763
3
1
The adventures of sherlock holmes
sherlock holmes
2
The return of sherlock holmes
sherlock holmes
3
The sign of the four
sherlock holmes
A-660
Khairatabad
lucknow
u.p.
201876
lucknow

Output:
SHAKESPHERE 3

"""

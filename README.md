
<h1>Python</h1>
Here you can find some python exercises. <br/>
In case of everything work out as planned(i have free time), I will provide more than one answer to each question (Usually useless, just for fun) <br/>
<a href= "https://www.w3resource.com/python-exercises/">w3resource</a> is the resource(ha!) of the questions.

<details><summary>W3RESOURCE</summary>
<details>
<summary> Python Programming Puzzles </summary>


<summary>1</summary>
Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five.
<pre>
def teste(lista):
    print("The list:", lista)
    if lista.count(19) == 2 and lista.count(5) >= 3:
        print(True)
    else:
        print(False)


list1 = [1,2,3,4,5,5,5,5,19,19]
teste(list1)
list2 = [5,5,5,5,55,5,5,19,19,19,19]
teste(list2)
</pre>
<summary>2</summary>
Write a Python program that accept a list of integers and check the length and the fifth element.
Return true if the length of the list is 8 and fifth element occurs thrice in the said list.
def check(lista):
    if lista.count(lista[4]) == 3:
        print(lista, "True")
    else:
        print(lista, "False")


list1 = ([1,2,3,4,5,5,5,6])
check(list1)

list2 =([0,1,2,3,4,5,6,7,8,9])
check(list2)
</pre>

</details>
	
<details>
<summary>Python Basic (Part -I)</summary>
	<summary>1</summary>
Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How           I wonder what you are" Output :
			
<pre>
     Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
</pre>
          
First method:
<pre>
# Just use """ to print multiple line  
print("""Twinkle, Twinkle, little star,
        How I wonder what you are!
                Up above the world so high,
                Like a diamond in the sky.
Twinkle, twinkle, little star,
    How I wonder what you are""")

# 0.0009927749633789062 seconds. The most beautiful, but took a longer time.
</pre> 


Second Method:      
<pre>
# Print all in a single line (ouch!)      
print("winkle, Twinkle, little star,\n        How I wonder what you are!\n                Up above the world so high,\n                Like a diamond in the                   sky.\nTwinkle, twinkle, little star,\n    How I wonder what you are")
# 0.00049591064453125 seconds.
</pre>

      
 Third Method:
 <pre>
#  Create a variable and print it (double ouch!).

Text = "winkle, Twinkle, little star,\n        How I wonder what you are!\n                Up above the world so high,\n                Like a diamond in the sky.\nTwinkle, twinkle, little star,\n    How I wonder what you are"
print(Text)
</pre>
<summary>2</summary>
Write a Python program to get the Python version you are using.

First Method:
<pre>
# Honestly? Had no idea
import sys # ok, I knew this one
print("You are using Python {}.{}.".format(sys.version_info.major, sys.version_info.minor)) # I didn't had idea
</pre>
0.00049591064453125 seconds

Second Method:
<pre>
# Took more time, but shows an completier message.
#import sys

print("Python version")
print (sys.version)
# 0.0009987354278564453 seconds
</pre>

   	    	<summary>3</summary>
 Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14

First Method:
<pre>
import datetime
print("Current date and time:")
print(datetime.datetime.now()) # Other print, to avoid the " "
</pre>

Second Method:
I could use (sys.version - irrelevant info), but nah

<summary>4</summary>
Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output :
r = 1.1
Area = 3.8013271108436504
	
First Method:
<pre>
# Easy
from numpy import pi

r = float(input("Enter with the radius: "))
print("r = ", r, "\nArea = ", pi*(r**2))
# 1.977311372756958 Seconds
</pre>
	
Second Method:
<pre>
mypi = 3.13159265358779323626433
print("Enter with radius: ")
r = float(input("r = "))

def area():
    print("Area: =",mypi*(r**2))


area()
# 1.540489912033081 Seconds.
</pre>

<summary>5</summary>
Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

First Method:
<pre>
Lname = (input("Enter your first name: "))
Lname = (input("Enter your last name: "))
print(Lname, Fname)

# 3.1332342624664307 Seconds
</pre>

Second Method:
<pre>
FLname = input(str("Enter your first and last name: "))
sepname = FLname.split(" ")
print(sepname[1],sepname[0])

# 4.2260999679565435 Seconds, of course
</pre>

Thirt Method:
<pre>
# Basically the first one, but using one line to input Names.
Fname, Lname = (input("Enter your first name: "), input("Enter your last name: "))
print(Lname, Fname)
	
# 3.762261152267456 Seconds.
</pre>
	
Fourth Method:
<pre>
# Just one more
def name():
        Fname = str(input("Enter your first name: "))
        Lname = str(input("Enter your last name: "))
        print(Lname, Fname)

name()

# 4.156754732131958 Seconds.
</pre>

<summary>6</summary>
Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')

First method:
<pre>

UserNumbers = (input("Insert your sequence of comma-separated numbers: "))
UserNumbersList = UserNumbers.split((","))
print((type(UserNumbersList), UserNumbersList))
UserNumbersTuple = tuple(UserNumbersList)

# Time:  3.716700315475464
</pre>

<summary>7</summary>
Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java
Output : java
	

<pre>
FileName = input("""Enter your file name with extension , example: mybook.txt 
your turn: """)
FileName = FileName.split(".")
print(FileName[-1])

# Time 7.073101282119751
</pre>
<summary>8</summary>
Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]

<pre>
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], color_list[-1])

# Time 0.012399673461914062
</pre>

<summary>9</summary>
 Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014

<pre>
exam_st_date = (11, 12, 2014)
exam_st_date = list(exam_st_date)
print ("The examination will start from: ", exam_st_date[0],"/", exam_st_date[1], "/", exam_st_date[2])

# Time 0.0004971027374267578
</pre>

<summary>10</summary>
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
	<br>Sample value of n is 5
		<br>Expected Result : 615
<pre>
BaseNumber = int(input("Enter the number n: "))
print(BaseNumber + BaseNumber**2 + BaseNumber**3)
# Time 2.142456293106079

</pre>
<summary>11</summary>
Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
	<br>Sample function: abs()

<pre>
print(abs.__doc__)

# Time 0.0 , could be faster
</pre>
<summary>12</summary>
Write a Python program to print the calendar of a given month and year.
	<br>Note : Use 'calendar' module.

<pre>
year = int(input("Year: "))
month = int(input("Month: "))

print(calendar.month(year, month))

# Time 0.0 , could be faster
</pre>

<summary>14</summary>
Write a Python program to calculate number of days between two dates.
	<br>Sample dates : (2014, 7, 2), (2014, 7, 11)
	<br>Expected output : 9 days
<pre>
from datetime import date

fdate = date(2020, 5, 5)
ldate = date(2021, 5, 5)
print((ldate - fdate).days)

# Time 0.003968238830566406
</pre>

<summary>15</summary>
 Write a Python program to compute the product of a list of integers (without using for loop)
<pre>
actualposition ,total  = 0, 1
numbers = [3, 3, 2]
total = 1

while actualposition  < (len(numbers)):
    total = (numbers[actualposition]*total)
    actualposition += 1
</pre>

<summary>116 (mb) </summary>
Write a Python program to print Unicode characters.
	<pre>
	Unicode = u'\03 \u004E \u0049 \u0043 \u0045 \03'
	print(Unicode)
	</pre>
# Time 0.0004966259002685547

	<summary>16</summary>
Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
<pre>
try:
    n1 = float(input("Enter your given number: "))
except ValueError:
    print("Number my brother")
if n1 > 17:
    print((n1 - 17)*2)
elif n1 == 17:
    print("Even number")
else:
    print ("Given number is lower then 17")
</pre>

<summary>17</summary>
Write a Python program to test whether a number is within 100 of 1000 or 2000.
<pre>
YourNumber = float(input("Enter your number: "))
if abs(YourNumber - 1000) <= 100:
    print("Close to 1000")
elif abs(YourNumber - 2000) <= 100:
    print("Close to 2000")
    print(YourNumber - 2000)
else: print("None of them")
</pre>

<summary>18</summary>
Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
<pre>
def nsums(n1, n2, n3):
    if n1 == n2 == n3:
        sum = (n1+n2+n3)*3
    else:
        sum = (n1+n2+n3)
    return sum

print(nsums(-3, 0, 9))
print(nsums(2, 2, 2))
</pre>

<summary>19</summary>
Write a Python program to get a new string from a given string where "Is" has been added to the front.
If the given string already begins with "Is" then return the string unchanged.
<pre>
def input_Is (x):
	if phrase[0:2] == "Is":
        print(phrase)
    else:
        print("Is"+phrase)

phrase = ("ThisOk?")
input_Is(phrase)
phrase = ("IsThisOk?")
input_Is(phrase)
</pre>

<summary>20</summary>
Write a Python program to get a string which is n (non-negative integer) copies of a given string.
<pre>
	def repeat_this (x, y):
    print(x*y)

repeat_this("Hi", 3)
</pre>

<summary>21</summary>
Write a Python program to find whether a given number (accept from the user) is even or 
odd, print out an appropriate message to the user.
<pre>
def even_or_odd(x):
    if x%2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

num = int(input("Insert Number: "))

even_or_odd(num)
</pre>

<summary>22</summary>
Write a Python program to count the number 4 in a given list.
<pre>
def search_num4(x):
    nums_4 = 0
    for i in x:
        if i == 4:
            nums_4 += 1

    print(nums_4)

list_one = [0, 1, 2, 3, 4, 5, 6]
list_two = [4, 4 , 4, 4, 4, 4, 4]
search_num4(list_one)
search_num4(list_two)
</pre>

<summary>23</summary>
Write a Python program to get the n (non-negative integer) copies of the first 2 characters
of a given string. Return the n copies of the whole string if the length is less than
<pre>
def copies(word, rep):
    firstwo = word[0:2]
    print(firstwo*rep)

word = str(input("Enter with the word or phrase: "))
rep = int(input("How many times you want to repeat the first two letters?"))
copies(word, rep)
</pre>

<summary>24</summary>
Write a Python program to test whether a passed letter is a vowel or not.
<pre>
	def vogal(letter):
    vogais = "aeiou"
    return letter in vogais

letter = str(input("Enter your letter: "))
if (vogal(letter) == True):
    print("Vowel")
else:
    print("Not Vowel")

</pre>

<summary>25</summary>
Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
<pre>
def check_if_contained(i, data):
	for x in data:
        if i == x:
            return (True)
    return (False)

data_group = [1, 5, 8, 3]
print(check_if_contained(3, data_group))
print(check_if_contained(-1, data_group))
</pre>
</details>
</details>

<h1>C++</h1>
<details>
<summary><a href= "https://www.w3resource.com/cpp-exercises/">W3resource</a></summary>
<details><summary>C++ Basic</summary>
<summary>1</summary>
Write a program in C++ to print a welcome text in a separate line
<pre>
    #include <iostream>
        using namespace std;
        
        int main()
        {
          cout << "Wellcome :" <<endl;
          cout << "Thats some c++ Exercises";
          return 0;
        }        
</pre>

<summary>2</summary>
Write a program in C++ to print the sum of two numbers.
<pre>
    #include <iostream>
        using namespace std;
        
        int main()
        {
        cout << "5 + 9 = " <<5+9;
        }        
</pre>

<summary>3</summary>
Write a program in C++ to find Size of fundamental data types.
<pre>
#include <iostream>
    using namespace std;
    int main()
    {
    string name("Felipe");
    cout << "Size of my name (Felipe) is: " <<sizeof(name) << "bytes";
    
    return 0;
    }
</pre>

<summary>4</summary>
Write a program in C++ to print the sum of two numbers using variables.
<pre>
#include <iostream>
using namespace std;
        
int main()
{
float a = (2.3), b(9.8);
cout << "The sums of a b = " << (a+b);
}
</pre>

<summary>5</summary>
Write a program in C++ to check the upper and lower limits of integer
<pre>
#include <iostream>
#include <climits>
using namespace std;

int main()
{
cout << "The maximum limit in data type: " << INT_MAX << endl;
cout << "The maximum limit in data type is: " << INT_MIN << endl;

return 0;
}
</pre>

</details>

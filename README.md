# Python-Exercises
Here you can find some python exercises. <br/>
In case of everything work out as planned(i have free time), I will provide more than one answer to each question (Usually useless, just for fun) <br/>
https://www.w3resource.com/python-exercises/, w3resource is the resource(ha!) of the questions.

<details>
<summary>W3RESOURCE</summary>
	<details>
	<summary>Python Basic (Part -I)</summary>
       		<details>
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
</details>
<details> 
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
</details>
<details> 
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
</details>
<details>
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
</details>
<details>
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
</details>
<details>
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
</details>
		
<details>
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
</details>
		
<details>
        	<summary>8</summary>
Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]

<pre>
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], color_list[-1])

# Time 0.012399673461914062
</pre>
</details>
		
<details>
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
</details>
		
<details>
        	<summary>10</summary>
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
	<br>Sample value of n is 5
		<br>Expected Result : 615
<pre>
BaseNumber = int(input("Enter the number n: "))
print(BaseNumber + BaseNumber**2 + BaseNumber**3)

# Time 2.142456293106079
</pre>
</details>
		
<details>
        	<summary>11</summary>
Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
	<br>Sample function: abs()

<pre>
print(abs.__doc__)

# Time 0.0 , could be faster
</pre>
</details>
		
<details>
        	<summary>12</summary>
Write a Python program to print the calendar of a given month and year.
	<br>Note : Use 'calendar' module.


<pre>
year = int(input("Year: "))
month = int(input("Month: "))

print(calendar.month(year, month))

# Time 0.0 , could be faster
</pre>
</details>

<details>
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
</details>

<details>
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
</details>

	
<details>
        	<summary>116 (mb) </summary>
Write a Python program to print Unicode characters.
	<pre>
	Unicode = u'\03 \u004E \u0049 \u0043 \u0045 \03'
	print(Unicode)
	</pre>
# Time 0.0004966259002685547
</details>

<details>
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
</details>

	<summary>17</summary>
Write a Python program to test whether a number is within 100 of 1000 or 2000.
<pre>



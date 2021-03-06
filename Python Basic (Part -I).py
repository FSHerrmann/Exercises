# Python-Exercises
# Here you can find some python exercises. <br/>
# In case of everything work out as planned(i have free time), I will provide more than one answer to each question (Usually useless, just for fun) <br/>
# https://www.w3resource.com/python-exercises/, w3resource is the resource(ha!) of the questions.
# Python Basic (Part -I)

# 1 - Write a Python program to print the following string in a specific format (see the output). Go to the editor
# Sample String :
#      Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are

# First method:
# Just use """ to print multiple line  

print("""Twinkle, Twinkle, little star,
        How I wonder what you are!
                Up above the world so high,
                Like a diamond in the sky.
Twinkle, twinkle, little star,
    How I wonder what you are""")

# Second Method:      
# Print all in a single line (ouch!) 

print("winkle, Twinkle, little star,\n        How I wonder what you are!\n                Up above the world so high,\n                Like a diamond in the                   sky.\nTwinkle, twinkle, little star,\n    How I wonder what you are")
      
# Third Method:
# Create a variable and print it (double ouch!).

Text = "winkle, Twinkle, little star,\n        How I wonder what you are!\n                Up above the world so high,\n                Like a diamond in the sky.\nTwinkle, twinkle, little star,\n    How I wonder what you are"

# 2 - Write a Python program to get the Python version you are using.
# First Method:
# Honestly? Had no idea
import sys # ok, I knew this one
print("You are using Python {}.{}.".format(sys.version_info.major, sys.version_info.minor)) # I didn't had idea

# Second Method:
# Took more time, but shows an completier message.
import sys
print("Python version")
print (sys.version)

# 3 -  Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

# First Method:
import datetime
print("Current date and time:")
print(datetime.datetime.now())

# 4 - Write a Python program which accepts the radius of a circle from the user and compute the area.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

# First Method:
# Easy
from numpy import pi

r = float(input("Enter with the radius: "))
print("r = ", r, "\nArea = ", pi*(r**2))

# Second Method:
mypi = 3.13159265358779323626433
print("Enter with radius: ")
r = float(input("r = "))

def area():
    print("Area: =",mypi*(r**2))


area()
# 1.540489912033081 Seconds.

# 5  - Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
# First Method:
Lname = (input("Enter your first name: "))
Lname = (input("Enter your last name: "))
print(Lname, Fname)

# Second Method:
FLname = input(str("Enter your first and last name: "))
sepname = FLname.split(" ")
print(sepname[1],sepname[0])

# Thirt Method:
# Basically the first one, but using one line to input Names.
Fname, Lname = (input("Enter your first name: "), input("Enter your last name: "))
print(Lname, Fname)

# Fourth Method:
# Just one more
def name():
        Fname = str(input("Enter your first name: "))
        Lname = str(input("Enter your last name: "))
        print(Lname, Fname)

name()

# 6 - Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

# First method:
UserNumbers = (input("Insert your sequence of comma-separated numbers: "))
UserNumbersList = UserNumbers.split((","))
print((type(UserNumbersList), UserNumbersList))
UserNumbersTuple = tuple(UserNumbersList)

# 7 - Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
# Output : java

FileName = input("""Enter your file name with extension , example: mybook.txt 
your turn: """)
FileName = FileName.split(".")
print(FileName[-1])

# 8 - Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], color_list[-1])

# 9 -  Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014
		
exam_st_date = (11, 12, 2014)
exam_st_date = list(exam_st_date)
print ("The examination will start from: ", exam_st_date[0],"/", exam_st_date[1], "/", exam_st_date[2])

# 10 - Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
# Sample value of n is 5
# Expected Result : 615

BaseNumber = int(input("Enter the number n: "))
print(BaseNumber + BaseNumber**2 + BaseNumber**3)

# 11 - Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function: abs()
print(abs.__doc__)

# 12- Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

year = int(input("Year: "))
month = int(input("Month: "))
print(calendar.month(year, month))

# 14 - Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

from datetime import date

fdate = date(2020, 5, 5)
ldate = date(2021, 5, 5)
print((ldate - fdate).days)

# 15 -  Write a Python program to compute the product of a list of integers (without using for loop)
actualposition ,total  = 0, 1
numbers = [3, 3, 2]
total = 1

while actualposition  < (len(numbers)):
    total = (numbers[actualposition]*total)
    actualposition += 1
	
	
# 16 - Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
number = float(input("Enter your number: "))
numberdif = 17 - number
if numberdif > 0:
    print(numberdif)
else:
    print((numberdif**2))
	
# 17 - Write a Python program to test whether a number is within 100 of 1000 or 2000.
YourNumber = float(input("Enter your number: "))
if abs(YourNumber - 1000) <= 100:
    print("Close to 1000")
elif abs(YourNumber - 2000) <= 100:
    print("Close to 2000")
    print(YourNumber - 2000)
else: print("None of them")

# 18 - Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
def nsums(n1, n2, n3):

    if n1 == n2 == n3:
        sum = (n1+n2+n3)*3
    else:
        sum = (n1+n2+n3)
    return sum


print(nsums(-3, 0, 9))
print(nsums(2, 2, 2))

# 19 -  Write a Python program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.

def input_Is (x):
    if phrase[0:2] == "Is":
        print(phrase)
    else:
        print("Is"+phrase)

phrase = ("ThisOk?")
input_Is(phrase)
phrase = ("IsThisOk?")
input_Is(phrase)

#20 Write a Python program to get a string which is n (non-negative integer) copies of a given string.
def repeat_this (x, y):
    print(x*y)

repeat_this("Hi", 3)

#21 Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
def even_or_odd(x):
    if x%2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

num = int(input("Insert Number: "))

even_or_odd(num)

#22 -  Write a Python program to count the number 4 in a given list.
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

#23 -  Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. 
# Return the n copies of the whole string if the length is less than 2

	
# 116 (My bad) - Write a Python program to print Unicode characters.
Unicode = u'\03 \u004E \u0049 \u0043 \u0045 \03'
print(Unicode)

#17 - 

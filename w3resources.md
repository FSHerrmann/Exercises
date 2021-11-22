# Python-Exercises
Here you can find some python exercises, I will make them in my free time, so it will serve as a simple portfolio. <br/>
In case of everything work out as planned(i have free time), I will provide more than one answer to each question. <br/>
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
          
Firt method:
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

	
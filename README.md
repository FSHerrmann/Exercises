# Python-Exercises
Here you can find some python exercises, I will make them in my free time, so it will serve as a simple portfolio. <br/>
In case of everything work out as planned(i have free time), I will provide more than one answer to each question. <br/>

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
          
Firt method: Just use """ to print multiple line   
<pre>
print("""Twinkle, Twinkle, little star,
        How I wonder what you are!
                Up above the world so high,
                Like a diamond in the sky.
Twinkle, twinkle, little star,
    How I wonder what you are""")
</pre> 
0.0009927749633789062 seconds. <-- The most beautiful, but took the double of time

Second Method: Print all in a single line (ouch!)            
<pre>
print("winkle, Twinkle, little star,\n        How I wonder what you are!\n                Up above the world so high,\n                Like a diamond in the                   sky.\nTwinkle, twinkle, little star,\n    How I wonder what you are")
</pre>
0.00049591064453125 seconds.
      
 Third Method: Create a variable and print it (double ouch!).
 <pre>
 Text = "winkle, Twinkle, little star,\n        How I wonder what you are!\n                Up above the world so high,\n                Like a diamond in the sky.\nTwinkle, twinkle, little star,\n    How I wonder what you are"
print(Text)
</pre>
0.0004951953887939453 seconds.
      
    
</details>


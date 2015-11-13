Here is the some code that does the exact same thing the right way. Using a function.

{Run the code}(python3 content/1-intro/example-func.py)

## Why is it better?
Just look at the code on the left compared to the code on the previous page. Go back a page and look. You should immediately see how much nicer it looks. 

### Duplication
The reason this code is better is that we no longer have duplicated bits of code. In this example we are only calling the function a couple of times.

Imagine you needed to use this code from 100 different places and coded it in the way it was done on the previous page. Now, you would have the same bit of code in 100 different places.

Now imagine that you later find out that that bit of code has a bug in it. You now have to go and fix the code in 100 places.

### Legibility
Another really important reason is that it makes your code **much** easier to read.

Instead of having to decipher lots of lines of code (the code that you moved to a function could have been hundreds of lines long) you can now read a nice, meaningful name and know immediately what it does.

And if you are still not sure, then you can go read the function code and then you'll know for the future.

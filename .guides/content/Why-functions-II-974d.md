On the left you will see code that does exactly the same thing in the correct way, by using a function.

{Run the code}(python3 content/1-intro/example-func.py)

## Why is it better?
One of the Programming Principles for this unit is **information hiding**. This is accomplished here by hiding the calculations necessary to calculate the weight of a cylinder behind a single function call.

### Duplication
The reason this code is better is that there are no duplicated bits of code.
In the example the function is only called a couple of times, but imagine you needed to use this code in one-hundred different places and you coded it in the way it was done on the previous page. Now, you would have the same bit of code repeated over and over in one-hundred different places.
What would happen if later you found out that that bit of code has a bug in it? You would have to go and fix the code over and over in one-hundred places.

### Legibility
Another really important reason is that it makes your code **much** easier to read.

Instead of having to decipher lots of lines of code (the code that you moved to a function could have been hundreds of lines long) you can now read a nice, meaningful name and know immediately what it does.


Have a look at the function `volumeCylinder()`. Below is an explanation of how this function is constructed.

{Run the code}(python3 content/1-intro/example2-func.py)

```python
def volCylinder(radius, height):
  v = math.pi * radius * radius * height
  return v
```

An alternative way to write the code would be like this:

```python
def volCylinder(radius, height):
  return math.pi * radius * radius * height
```

## Function name
To name a function you use the same rules that apply to a variable. In this case, the function is called `volCylinder`.

## Code block
The function gets its own code block (just like an `if` statement or a `for` loop). The block starts with a `:` and is followed by as many lines of code as you want.

## Arguments
After the function name come any *arguments* that the function receives. Some functions do not take any arguments.

You can think of an argument as a variable. In our example, the arguments are `radius` and `height`. Within your function's code block, you can now treat this argument as if it were a variable.

The main thing to note here is that the calling function takes a *parameter* that maps to this argument. Look at the function call below as an example:

```python
vol = volumeCylinder(10, 30)
```

- `10` is the 1st parameter and is passed to the `radius` argument of the function
- `30` is the 2nd parameter and is passed to the `height` argument.

## Return
Below is a summary of the use of the `return` statement within a function:

- All functions return control back to the line of code that called them whether you include an return statement or not.
- If you don't include an explicit `return` statement in your function, then it will return when execution reaches the end of the code block.
- A `return` statement without an expression after it will simply return to the calling code.
- A `return` statement with an expression after it will return that value back to the line of code that called it. In the above example, that value is then assigned to `vol`.

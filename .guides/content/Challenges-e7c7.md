Now you are ready to try some challenges and test your knowledge of functions.

## Testing your functions
In these challenges, you will write functions that will be called for you. You can test these out easily directly in your code as shown in the earlier example:

```python
# caclulate the volume of a cylinder
import math

def volumeCylinder(radius, height):
  v = math.pi * radius * radius * height
  return v

output ('r=10, h=20 => V=' + str(volumeCylinder(10, 20)))
```

You can call your function anywhere outside the function as `value = convertField(string1)` does above.

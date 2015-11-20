## Tip: String.find(searchWord)
In this challenge, you'll be asked to find one string in the text of another string. Python provides a function to help with this called `find()` that can be called on any string.

To find a string `needle` in another string `haystack`, use `haystack.find(needle)`, which will return the position where `needle` was found, or `-1` if it was not found at all.

```python
haystack= 'abc def ghi'
needle= 'def'
needleLocation= haystack.find(needle)
print(needneedleLocation)
print(haystack.find('chicken'))
```
{Run find test}(python3 content/find.py)

{Check It!|assessment}(test-2339136925)

|||guidance
### Solutions
```python
# Get our input from the command line
import sys
text= sys.argv[1]

# Write your code here
def isRed(val):
  if val.find('red') == -1:
    return False
  else:
    return True

print(isRed(text))
```
|||

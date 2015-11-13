{Check It!|assessment}(test-1824401609)

|||guidance
### Solutions
```python
# Get our arguments from the command line
import sys
character= sys.argv[1]
count= int(sys.argv[2])

# Your code goes here
def generateString(char, val):
  result = ''
  
  for i in range(0, val):
    result = result + char

  return result
    
print(generateString(character, count))

```
|||

{Check It!|assessment}(test-2339136925)

|||guidance
### Solutions
```python
# Get our input from the command line
text= sys.argv[2]

# Write your code here
def isRed(val):
  if val.find('red') == -1:
    return False
  else:
    return True

print(isRed(text))
```
|||

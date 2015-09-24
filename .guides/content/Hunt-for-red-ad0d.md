{Run the code}(python3 run-user.py red.py)

{Check It!|assessment}(test-2339136925)

|||guidance
### Solutions
```python
input0 = input0('blue red green')

# Write your code here

def isRed(val):
  if val.find('red') == -1:
    return False
  else:
    return True

output(isRed(input0))
```
|||
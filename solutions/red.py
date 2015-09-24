
input0 = input0('blue red green')

def isRed(val):
  if val.find('red') == -1:
    return False
  else:
    return True

# Tests
output(isRed(input0))

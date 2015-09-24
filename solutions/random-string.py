
input0 = input0('a')
input1 = input1(7)

def generateString(char, val):
  result = ''
  
  for i in range(0, val):
    result = result + char

  return result
    
output(generateString(input0, input1))
  
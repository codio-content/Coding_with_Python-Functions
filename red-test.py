
import test

test.test('red.py', [''], [False])
test.test('red.py', ['blue red green'], [True])
test.test('red.py', ['aaa'], [False])
test.test('red.py', ['red'], [True])

print('Well done')

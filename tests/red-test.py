
import test

test.test('challenges/red.py', [''], [False])
test.test('challenges/red.py', ['blue red green'], [True])
test.test('challenges/red.py', ['aaa'], [False])
test.test('challenges/red.py', ['red'], [True])

print('Well done')

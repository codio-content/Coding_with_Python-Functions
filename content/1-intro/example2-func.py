
import math

def volCylinder(radius, height):
  return math.pi * radius * radius * height

print('r=10, h=20 => V=' + str(volCylinder(10, 20)))
print('r=1, h=10 => V=' + str(volCylinder(1, 10)))
print('r=125, h=2520 => V=' + str(volCylinder(125, 2520)))

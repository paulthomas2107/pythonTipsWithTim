import math

x = 10
y = 20

print("Before swap: ")
print('X =', x)
print('Y =', y)

x, y = y, x

print("After swap: ")
print('X =', x)
print('Y =', y)

x, y = 120, math.pi

print("After change: ")
print('X =', x)
print('Y =', y)

import math
radius = int(input('Enter radius: '))

def area(r):
  return math.pi * (r **2)

result = area(radius)
print(f'Area of circle is {result}')
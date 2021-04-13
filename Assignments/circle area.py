# input is radius
# area = pi * r(2)

import math
r = int(input('enter radius '))

def areaofcircle(r):
    a = math.pi * (r**2)

    return a


print(areaofcircle(r))
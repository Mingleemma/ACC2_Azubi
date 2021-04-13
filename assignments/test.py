# Area of a circle

# def area(r):
#     a = 3.14 * (r**2)
#     return a
# print(area(8))

# Area of a circle with math.pi
# import math
# def areaCircle(r):
#     a = math.pi * (r**2)
#     return a
# print(area(8))


# The third approach
import math

def area_of_circle(r):
    a = math.pi * (r**2)
    return a

radius = float(input("Enter radius of the circle: "))

print(area_of_circle(radius))


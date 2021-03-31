# input radius
# area = pi * radius**2
import math

r = float(input("enter radius: "))


def area_circle():
    a = math.pi * (r ** 2)
    return round(a, 2)


print(area_circle())

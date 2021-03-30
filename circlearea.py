#importing the math module to call math functions
import math
#input is the radius
# area = pi * (r**2)

#radius to be inputted by user
def area():
    r = float(input('Enter radius here: '))
    c_area = math.pi * (r**2)
    return c_area
print (area())




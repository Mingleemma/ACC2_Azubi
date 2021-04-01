
def celcius_to_fahrenheit(c):
    f = round((c * 9 / 5) + 32, 2)
    print("{} celcius is {} fahrenheit".format(c, f))
    return f


def fahrenheit_to_celcius(f):
    c = (f - 32) * 5 / 9
    print("{} fahrenheit is {} celcius".format(c, f))
    return c


fahrenheit_to_celcius(100)

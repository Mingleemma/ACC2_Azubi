def convert_temperature():
    print("We are going to convert temperature from degree celcius to degree farenheit.")
    while True:
        try:
            temp_celcius = input("Enter temperature in Celcius: \n")
            temp_farh = round(((float(temp_celcius) * 9 / 5) + 32), 2)
            print("The temperature in farenheit is {}.".format(temp_farh))
            break
        except ValueError:
            print("Please type a number")
            continue


convert_temperature()

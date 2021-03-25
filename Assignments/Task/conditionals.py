#name = input("What is your name?")
#if len(name) > 21:
#   print("You have a long name {}".format(name))
#   print("Your name is not very long {}".format(name))
response = "YES"
while response.upper() == "YES":
    dayborn = input("On what day were you born:")
    if dayborn.upper() == "SUNDAY":
        print("You are Kwasi or Akosua")
    elif dayborn.upper() == "MONDAY":
        print("You are Kwadwo or Adwoa")
    elif dayborn.upper() == "TUESDAY":
        print("You are Kwadwo or Adwoa")
    elif dayborn.upper() == "WEDNESDAY":
        print("You are Kwaku or Akua")
    elif dayborn.upper() == "THURSDAY":
        print("You are Yaw or Yaa")
    elif dayborn.upper() == "FRIDAY":
        print("You are Kofi or Afua")
    elif dayborn.upper() == "SATURDAY":
        print("You are Kwame or Ama")
    else:
        print("The day must be between Sunday and Saturday")

    response = input("Do you want to check for another day? ")
    if response.upper() != ("YES" or "NO"):
        response = input("Do you want to check for another day? ")

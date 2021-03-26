# python3.9
# list of Fincher films
fincherCatalog = ["Se7en", "Fight Club", "The Curious Case of Benjamin Button", "The Game"]

# questionnaire on fincher discography viewing
question = "Have you seen"
follow_up = "How about"
logged = "se7en"

# test for se7en
while logged == "se7en":
    answer1 = input(f"{question} {fincherCatalog[0]}\n ")
    answer1 = answer1.lower()
    if answer1 == "yes" or answer1 == "yeah":
        print("taste!")
    else:
        print("do better")

    # test for fight club
    logged = "fight_club"
    answer2 = input(f"{follow_up} {fincherCatalog[1]}\n ")
    answer2 = answer2.lower()
    while logged == "fight_club" and logged != "no":
        if answer2 == "yes" or logged == "yeah":
            print("you live in a society")


        else:
            print("pattern up!")

        # breaking loop
        logged = "end"

        print("bye")

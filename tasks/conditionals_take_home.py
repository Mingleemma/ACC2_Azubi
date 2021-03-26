# list of Fincher films
fincher_discog = ["Se7en", "Fight Club", "The Curious Case of Benjamin Button", "The Game"]

# questionaire on fincher discography viewing
question = "Have you seen"
follow_up = "How about"
logged = "se7en"

# test for se7en
while logged == "se7en":
    answer1 = input(f"{question} {fincher_discog[0]}\n ")
    answer1 = answer1.lower()
    if answer1 == "yes" or answer1 == "yeah":
        print("taste!")
    else:
        print("do better")


    logged = "fight_club"
    answer2 = input(f"{follow_up} {fincher_discog[1]} ")
    answer2 = answer2.lower()
    while logged == "fight_club" and logged != "no":
        if logged == "yes" or logged == "yeah":
            print("you live in a society")

        elif logged == "no":
            print("pattern up")

        else:
            print("you should join a fight club")

        logged = "end"

        print("bye")

# list of Fincher films
fincher_discog = ["Se7en", "Fight Club", "The Curious Case of Benjamin Button", "The Game"]

# questionaire on fincher discography viewing
question = "Have you seen"
follow_up = "How about"
logged = "se7en"

# test for se7en
while logged == "se7en":
    answer = input(f"{question} {fincher_discog[0]}\n ")
    answer = answer.lower()
    if answer == "yes" or answer == "yeah":
        print("taste!")
    else:
        print("do better")

    fight_club = input(f"{follow_up} {fincher_discog[1]} ")
    logged = fight_club
    logged = logged.lower()
    while logged == fight_club:
        if logged == "yes" or logged == "yeah":
            print("you live in a society")

        elif logged == "no":
            print("do the needful")

        else:
            print("you should join a fight club")

        logged = "end"

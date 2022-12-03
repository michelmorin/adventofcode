rock = 1
paper = 2
scissors = 3

with open("input.txt", "r") as file:
    games = file.read().splitlines()

    totalPoints = 0
    totalPoints2 = 0

    for game in games:
        selection = game.split()
        selection1 = 0
        selection2 = 0
        if selection[0].lower() == "a":
            selection1 = 1
        if selection[0].lower() == "b":
            selection1 = 2
        if selection[0].lower() == "c":
            selection1 = 3
        if selection[1].lower() == "x":
            selection2 = 1
        if selection[1].lower() == "y":
            selection2 = 2
        if selection[1].lower() == "z":
            selection2 = 3

        if selection1 == rock:
            if selection2 == 2:
                totalPoints += (6+selection2)
                totalPoints2 += (3 + rock)
            elif selection2 == 3:
                totalPoints += selection2
                totalPoints2 += (6 + paper)
            else:
                totalPoints += (3+selection2)
                totalPoints2 += scissors
        if selection1 == paper:
            if selection2 == 3:
                totalPoints += (6+selection2)
                totalPoints2 += (6 + scissors)
            elif selection2 == 1:
                totalPoints += selection2
                totalPoints2 += rock
            else:
                totalPoints += (3+selection2)
                totalPoints2 += (3+paper)
        if selection1 == scissors:
            if selection2 == 1:
                totalPoints += (6+selection2)
                totalPoints2 += paper
            elif selection2 == 2:
                totalPoints += selection2
                totalPoints2 += (3 + scissors)
            else:
                totalPoints += (3+selection2)
                totalPoints2 += (6 + rock)

    print(f"Part 1: Your Total points at Rock, Papers, Scissors game is : {totalPoints} points")
    print(f"Part 2: Your Total points at Rock, Papers, Scissors game is : {totalPoints2} points")

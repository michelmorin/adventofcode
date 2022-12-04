with open("input.txt", "r") as file:
    data = file.read().splitlines()

    priorityList = []
    priorityList2 = []
    groupList = []
    badgeList = []

    for index, rucksack in enumerate(data):
        compartmentA = rucksack[:int(len(rucksack)/2)]
        compartmentB = rucksack[int(len(rucksack) / 2):]
        for char in compartmentA:
            if char in compartmentB:
                if char.islower():
                    priorityList.append(ord(char)-96)
                else:
                    priorityList.append(ord(char)-38)
                break
        if index % 3 == 2:
            groupList.append(rucksack)
            for char in groupList[0]:
                if char in groupList[1]:
                    if char in groupList[2]:
                        if char.islower():
                            priorityList2.append(ord(char) - 96)
                        else:
                            priorityList2.append(ord(char) - 38)
                        break
            groupList.clear()
        else:
            # Add line to groupList
            groupList.append(rucksack)

    print(f"Part 1: The sum of the priorities is : {sum(priorityList)} points")
    print(f"Part 2: The sum of the priorities is : {sum(priorityList2)} points")
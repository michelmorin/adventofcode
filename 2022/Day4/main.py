part1count = 0
part2count = 0

with open("input.txt", "r") as file:
    data = file.read().splitlines()

    for assignement in data:
        replaceList = assignement.replace('-', ' ').replace(',', ' ').split()
        sectionID = [int(x) for x in replaceList]
        section1 = [sectionID[0], sectionID[1]]
        section2 = [sectionID[2], sectionID[3]]
        if section2[0] >= section1[0] and section2[1] <= section1[1]:
            part1count += 1
        elif section1[0] >= section2[0] and section1[1] <= section2[1]:
            part1count += 1

        if section2[0] >= section1[0] and section2[0] <= section1[1]:
            part2count += 1
        elif section2[1] >= section1[0] and section2[1] <= section1[1]:
            part2count += 1
        elif section1[0] >= section2[0] and section1[0] <= section2[1]:
            part2count += 1
        elif section1[1] >= section2[0] and section1[1] <= section2[1]:
            part2count += 1

    print(f"Part 1: The number of assignment pairs that fully contain the other are: {part1count}")
    print(f"Part 2: The number of assignment pairs that have overlapping: {part2count}")
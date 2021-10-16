file1 = open('input14test.txt', 'r')
Lines = file1.readlines()


def populateFromFile():
    data = []
    for line in Lines:
        data.append(line.strip())
    return data


print("Part 1 - answer:", currentPositionVertical+currentPositionHorizontal)
print("Part 2 - answer:", currentPositionVertical+currentPositionHorizontal)

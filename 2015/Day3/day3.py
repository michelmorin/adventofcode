def move_to_house(direction, x, y):
        if (direction == "^"):
            y += 1
        elif (direction == "v"):
            y -= 1
        elif (direction == ">"):
            x += 1
        elif (direction == "<"):
            x -= 1

        return x, y

with open("input.txt", 'r') as direction_file:
    directions = direction_file.readline()

    x_part1 = 0
    y_part1 = 0
    house_dict_part1 = {}

    house_dict_part1[str(x_part1) + str(y_part1)] = True
    for direction in [char for char in directions]:
        x_part1, y_part1 = move_to_house(direction, x_part1, y_part1)
        house_dict_part1[str(x_part1) + str(y_part1)] = True

    print(f"Part 1 Number of houses visited is {len(house_dict_part1)}")

    x_santa = 0
    y_santa = 0
    x_robot = 0
    y_robot = 0
    house_dict_part2 = {}

    house_dict_part2[str(x_santa) + str(y_santa)] = True
    house_dict_part2[str(x_robot) + str(y_robot)] = True
    turn = "santa"
    for direction in [char for char in directions]:
        if turn == "santa":
            x_santa, y_santa = move_to_house(direction, x_santa, y_santa)
            house_dict_part2[str(x_santa) + str(y_santa)] = True
            turn = "robot"
        elif turn == "robot":
            x_robot, y_robot = move_to_house(direction, x_robot, y_robot)
            house_dict_part2[str(x_robot) + str(y_robot)] = True
            turn = "santa"

    # there is something that fails here, but I don't what, getting 2625, but answer is 2639
    print(house_dict_part2)
    print(f"Part 2 Number of houses visited is {len(house_dict_part2)}")
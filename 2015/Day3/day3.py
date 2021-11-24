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
    house_dict_part1 = set()

    house_dict_part1.add((x_part1, y_part1))
    for direction in [char for char in directions]:
        x_part1, y_part1 = move_to_house(direction, x_part1, y_part1)
        house_dict_part1.add((x_part1, y_part1))

    print(f"Part 1 Number of houses visited is {len(house_dict_part1)}")

    x_santa = 0
    y_santa = 0
    x_robot = 0
    y_robot = 0
    house_dict_part2 = set()

    house_dict_part2.add((x_santa, y_santa))
    house_dict_part2.add((x_robot, y_robot))
    turn = "santa"
    for direction in [char for char in directions]:
        if turn == "santa":
            x_santa, y_santa = move_to_house(direction, x_santa, y_santa)
            house_dict_part2.add((x_santa, y_santa))
            turn = "robot"
        elif turn == "robot":
            x_robot, y_robot = move_to_house(direction, x_robot, y_robot)
            house_dict_part2.add((x_robot, y_robot))
            turn = "santa"

    print(f"Part 2 Number of houses visited is {len(house_dict_part2)}")
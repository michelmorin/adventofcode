def has_it_increased(previous, current):
    return current > previous


with open("input.txt", "r") as file:
    depths = file.readlines()
    count_increased = 0

    for index, depth in enumerate(depths):
        if index >= 1:
            if has_it_increased(int(depths[index-1].rstrip()), int(depths[index].rstrip())):
                count_increased += 1

    print(f"Part 1: The number depths increased is: {count_increased}")

with open("input.txt", "r") as file:
    depths = file.readlines()
    count_increased = 0

    for index, depth in enumerate(depths):
        if index >= 3:
            previous_sum = int(depths[index - 3].rstrip()) \
                + int(depths[index - 2].rstrip()) \
                + int(depths[index - 1].rstrip())
            current_sum = int(depths[index - 2].rstrip()) \
                + int(depths[index - 1].rstrip()) \
                + int(depths[index].rstrip())

            if has_it_increased(previous_sum, current_sum):
                count_increased += 1

    print(f"Part 2: The number sum depths increased is: {count_increased}")

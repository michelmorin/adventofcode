def has_it_increased(previous, current):
    return current > previous


with open("input.txt", "r") as file:
    depths = file.read().splitlines()
    count_increased = 0

    for index, depth in enumerate(depths):
        if index >= 1:
            if has_it_increased(int(depths[index-1]), int(depths[index])):
                count_increased += 1

    print(f"Part 1: The number depths increased is: {count_increased}")

with open("input.txt", "r") as file:
    depths = file.read().splitlines()
    count_increased = 0

    for index, depth in enumerate(depths):
        if index >= 3:
            previous_sum = sum([int(d) for d in depths[index - 3:index]])
            current_sum = sum([int(d) for d in depths[index - 2:index+1]])

            if has_it_increased(previous_sum, current_sum):
                count_increased += 1

    print(f"Part 2: The number sum depths increased is: {count_increased}")

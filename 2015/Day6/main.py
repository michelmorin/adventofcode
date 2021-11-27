light_grid = [[False for _ in range(1000)] for _ in range(1000)]
light_grid2 = [[0 for _ in range(1000)] for _ in range(1000)]


def check_lights_on(light_list):
    light_on_count = 0
    for row in light_list:
        for light in row:
            if light is True:
                light_on_count += 1
    return light_on_count


def check_lights_brightness(light_list):
    light_brightness_count = 0
    for row in light_list:
        for light in row:
            light_brightness_count += light
    return light_brightness_count


def execute_instruction_part1(new_instruction):
    if "turn on" in new_instruction:
        split_instruction = new_instruction.split()
        start_coord = split_instruction[2].split(",")
        end_coord = split_instruction[4].split(",")
        for index, row in enumerate(light_grid[int(start_coord[0]):int(end_coord[0])+1]):
            for index2, light in enumerate(row[int(start_coord[1]):int(end_coord[1])+1]):
                row_index = index + int(start_coord[0])
                col_index = index2 + int(start_coord[1])
                light_grid[row_index][col_index] = True
    elif "turn off" in instruction:
        split_instruction = instruction.split()
        start_coord = split_instruction[2].split(",")
        end_coord = split_instruction[4].split(",")
        for index, row in enumerate(light_grid[int(start_coord[0]):int(end_coord[0]) + 1]):
            for index2, light in enumerate(row[int(start_coord[1]):int(end_coord[1]) + 1]):
                row_index = index + int(start_coord[0])
                col_index = index2 + int(start_coord[1])
                light_grid[row_index][col_index] = False
    elif "toggle" in instruction:
        split_instruction = instruction.split()
        start_coord = split_instruction[1].split(",")
        end_coord = split_instruction[3].split(",")
        for index, row in enumerate(light_grid[int(start_coord[0]):int(end_coord[0]) + 1]):
            for index2, light in enumerate(row[int(start_coord[1]):int(end_coord[1]) + 1]):
                row_index = index+int(start_coord[0])
                col_index = index2+int(start_coord[1])
                light_grid[row_index][col_index] = not light_grid[row_index][col_index]


def execute_instruction_part2(new_instruction):
    if "turn on" in new_instruction:
        split_instruction = new_instruction.split()
        start_coord = split_instruction[2].split(",")
        end_coord = split_instruction[4].split(",")
        for index, row in enumerate(light_grid[int(start_coord[0]):int(end_coord[0])+1]):
            for index2, light in enumerate(row[int(start_coord[1]):int(end_coord[1])+1]):
                row_index = index + int(start_coord[0])
                col_index = index2 + int(start_coord[1])
                light_grid2[row_index][col_index] += 1
    elif "turn off" in new_instruction:
        split_instruction = new_instruction.split()
        start_coord = split_instruction[2].split(",")
        end_coord = split_instruction[4].split(",")
        for index, row in enumerate(light_grid2[int(start_coord[0]):int(end_coord[0]) + 1]):
            for index2, light in enumerate(row[int(start_coord[1]):int(end_coord[1]) + 1]):
                row_index = index + int(start_coord[0])
                col_index = index2 + int(start_coord[1])
                if light_grid2[row_index][col_index] >= 1:
                    light_grid2[row_index][col_index] -= 1
    elif "toggle" in new_instruction:
        split_instruction = new_instruction.split()
        start_coord = split_instruction[1].split(",")
        end_coord = split_instruction[3].split(",")
        for index, row in enumerate(light_grid2[int(start_coord[0]):int(end_coord[0]) + 1]):
            for index2, light in enumerate(row[int(start_coord[1]):int(end_coord[1]) + 1]):
                row_index = index+int(start_coord[0])
                col_index = index2+int(start_coord[1])
                light_grid2[row_index][col_index] += 2


with open("input.txt", "r") as file:
    instructions = file.readlines()

    for instruction in instructions:
        execute_instruction_part1(instruction.strip())
        execute_instruction_part2(instruction.strip())

    print(f"Part 1: Number of lights on are {check_lights_on(light_grid)}")
    print(f"Part 2: Number of light brightness are {check_lights_brightness(light_grid2)}")

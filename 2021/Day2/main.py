def handle_instruction(instr: str, part: int):
    global forward, vertical, aim

    split_instruction = instr.split(" ")
    if split_instruction[0] == "forward":
        forward += int(split_instruction[1])
        if part == 2:
            vertical += aim * int(split_instruction[1])
    if split_instruction[0] == "up":
        if part == 1:
            vertical -= int(split_instruction[1])
        else:
            aim -= int(split_instruction[1])
    if split_instruction[0] == "down":
        if part == 1:
            vertical += int(split_instruction[1])
        else:
            aim += int(split_instruction[1])


with open("input.txt", 'r') as file:
    forward = 0
    vertical = 0
    aim = 0
    input_list = file.read().splitlines()

    for instruction in input_list:
        handle_instruction(instruction, 1)

    answer = forward * vertical
    print(f"Part 1: Forward is {forward}, vertical is {vertical}, sum is {answer}")


with open("input.txt", 'r') as file:
    forward = 0
    vertical = 0
    aim = 0

    input_list = file.read().splitlines()

    for instruction in input_list:
        handle_instruction(instruction, 2)

    answer = forward * vertical
    print(f"Part 2: Forward is {forward}, vertical is {vertical}, sum is {answer}")

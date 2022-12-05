import copy

stacks = [[], [], [], [], [], [], [], [], []]
answer1 = ""
answer2 = ""

with open("input.txt", "r") as file:
    data = file.read().splitlines()

    instructions = [x for x in data if x.startswith("move")]
    stackList = [x for x in data if "[" in x]
    for i in range(0, 4*len(stackList)+1, 4):
        if len(stackList) == 0:
            break
        tmp = stackList.pop()
        for index, char in enumerate(tmp):
            if char == "[" and index == 0:
                stacks[0].append(tmp[index+1])
            elif char == "[" and index == 4:
                stacks[1].append(tmp[index+1])
            elif char == "[" and index == 8:
                stacks[2].append(tmp[index+1])
            elif char == "[" and index == 12:
                stacks[3].append(tmp[index+1])
            elif char == "[" and index == 16:
                stacks[4].append(tmp[index+1])
            elif char == "[" and index == 20:
                stacks[5].append(tmp[index+1])
            elif char == "[" and index == 24:
                stacks[6].append(tmp[index+1])
            elif char == "[" and index == 28:
                stacks[7].append(tmp[index+1])
            elif char == "[" and index == 32:
                stacks[8].append(tmp[index+1])

    stacks2 = copy.deepcopy(stacks)

    for instruction in instructions:
        splitInstruction = instruction.split()
        cratesToMove = int(splitInstruction[1])
        fromStack = int(splitInstruction[3])
        toStack = int(splitInstruction[5])

        tempList = []
        for _ in range(cratesToMove):
            stacks[toStack-1].append(stacks[fromStack - 1].pop())
            tempList.append(stacks2[fromStack - 1].pop())
        for _ in range(len(tempList)):
            stacks2[toStack - 1].append(tempList.pop())

    for stack in stacks:
        answer1 += stack.pop()
    for stack in stacks2:
        answer2 += stack.pop()

    print(f"Part 1: The crate on top of each crate are: {answer1}")
    print(f"Part 2: The crate on top of each crate are: {answer2}")





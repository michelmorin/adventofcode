with open("input.txt", "r") as file:
    calories = file.read().splitlines()
    elves = []
    totalElfCalories = 0

    for calorie in calories:
        if calorie.strip():
            totalElfCalories += int(calorie)
        else:
            elves.append(totalElfCalories)
            totalElfCalories = 0

    # Add last entry
    if totalElfCalories != 0:
        elves.append(totalElfCalories)

    print(f"Part 1: The elf carrying the most calories has: {max(elves)} calories")
    combinedCalories = sum(sorted(elves, reverse=True)[:3])
    print(f"Part 2: The total calories of the top 3 value combined is {combinedCalories} calories")

VOWELS = ["a", "e", "i", "o", "u"]
NOT_THESE = ["ab", "cd", "pq", "xy"]

def is_nice_part1(new_string):
    for combination in NOT_THESE:
        if combination in new_string:
            return False

    vowel_count = 0
    for char in new_string:
        if char in VOWELS:
            vowel_count += 1

    is_double_char = False
    for index, char in enumerate(new_string):
        if index < len(new_string)-1 and char == new_string[index+1]:
            is_double_char = True

    if vowel_count >= 3 and is_double_char:
        return True

    return False

def is_nice_part2(new_string):
    is_double_char = False
    for index, char in enumerate(new_string):
        if index < len(new_string)-2 \
                and char == new_string[index+2] \
                and is_double_char is False:
            is_double_char = True

    is_double_combination = False
    for index, char in enumerate(new_string):
        if index < len(new_string) - 3 \
                and char+new_string[index + 1] in new_string[index + 2:] \
                and is_double_combination is False:
            is_double_combination = True

    if is_double_char and is_double_combination:
        return True

    return False


with open("input.txt", 'r') as file:
    string_list = file.readlines()

    nice_count = 0
    for string in string_list:
        if is_nice_part1(string):
            nice_count += 1
    print(f"Part 1: The number of nice strings are {nice_count}")

    nice_count = 0
    for index, string in enumerate(string_list):
        if is_nice_part2(string.strip()):
            nice_count += 1
    print(f"Part 2: The number of nice strings are {nice_count}")



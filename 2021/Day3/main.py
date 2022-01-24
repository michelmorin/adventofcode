from statistics import mode, multimode

BIT_LENGTH = 12

def check_common_bit(bits_list: list, index: int, reversed: bool):
    new_bits_list = []

    for entry in bits_list:
        for bit in entry[index]:
            new_bits_list.append(bit)

    if reversed:
        if len(multimode(new_bits_list)) > 1:
            return '0'
        else:
            if mode(new_bits_list) == '0':
                return '1'
            else:
                return '0'
    else:
        if len(multimode(new_bits_list)) > 1:
            return '1'
        else:
            return mode(new_bits_list)

def filter_list(bits_list: list, index: int, common_number: int):
    return [entry for entry in bits_list if entry[index] == str(common_number)]

with open("input.txt", "r") as f:
    input_list = f.read().splitlines()

new_input_list = [[] for i in range(BIT_LENGTH)]

for entry in input_list:
    for index, bit in enumerate(entry):
        new_input_list[index].append(bit)

mode_list = [mode(i) for i in new_input_list]

gamma_rate = int(''.join(mode_list), 2)

epsilon_list = []
for i in mode_list:
    if i == '0':
        epsilon_list.append('1')
    else:
        epsilon_list.append('0')
epsilon_rate = int(''.join(epsilon_list), 2)

print(f"Part 1: Power Consumption is: {gamma_rate * epsilon_rate}")

new_input_list = input_list

# Oxygen generator rating
for i in range(BIT_LENGTH):
    common_number = check_common_bit(new_input_list, i, False)
    new_input_list = filter_list(new_input_list, i, common_number)
    if len(new_input_list) == 1:
        break

oxygen_generator_rating = int(new_input_list[0], 2)

# C02 Scrubber rating
new_input_list = input_list

for i in range(BIT_LENGTH):
    common_number = check_common_bit(new_input_list, i, True)
    new_input_list = filter_list(new_input_list, i, common_number)
    if len(new_input_list) == 1:
        break

co2_scrubber_rating = int(new_input_list[0], 2)

print(f"Part 2: Life Support Rating is: {oxygen_generator_rating * co2_scrubber_rating}")








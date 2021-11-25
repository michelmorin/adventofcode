import hashlib

secret = "yzbqklnj"
decimal_count = 0


def check_value(decimal):
    return hashlib.md5(f"{secret}{decimal}".encode('utf-8')).hexdigest()


# Part 1
isNotFound = True

while isNotFound:
    hex_value = check_value(str(decimal_count))
    if hex_value[0:5] == "00000":
        print(f"Part 1: Decimal Value of {str(decimal_count)} makes Hex Value of {hex_value} "
              f"that starts with 5 leading zeros")
        break
    else:
        decimal_count += 1

# Part 2
isNotFound = True

while isNotFound:
    hex_value = check_value(str(decimal_count))
    if hex_value[0:6] == "000000":
        print(f"Part 2: Decimal Value of {str(decimal_count)} makes Hex Value of {hex_value} "
              f"that starts with 6 leading zeros")
        break
    else:
        decimal_count += 1

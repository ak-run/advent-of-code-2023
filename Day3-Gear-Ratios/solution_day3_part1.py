import random


def find_symbols(strings):
    """Find symbols in the engine schematics matrix and save their locations in a list of tuples"""
    symbol_locations_list = []

    for i, string in enumerate(strings):
        for j, char in enumerate(string):
            if char.isalnum() or char == '.':
                continue
            else:
                symbol_locations_list.append((i, j))

    return symbol_locations_list


def extract_numbers_with_variations(strings):
    """
    Find each number and save it in a dictionary:
    key: code string for the number to account for duplicates
    value: list of tuples representing locations of each digit and locations around them
    """
    result_dict = {}

    for i, string in enumerate(strings):
        j = 0
        while j < len(string):
            if string[j].isdigit():
                num_str = ""
                num_start = j
                digit_locations = []

                while j < len(string) and string[j].isdigit():
                    num_str += string[j]
                    digit_locations.append(j)
                    j += 1

                key = f"index{i}-num-{num_str}-{random.randint(1, 1000)}"
                value = []

                for line_variation in [-1, 0, 1]:
                    for digit_location in digit_locations:
                        new_line = i + line_variation

                        for digit_column_variation in [-1, 0, 1]:
                            new_digit = digit_location + digit_column_variation

                            if 0 <= new_line < len(strings) and 0 <= new_digit < len(string):
                                value.append((new_line, new_digit))

                result_dict[key] = value
            else:
                j += 1

    return result_dict


with open("input_day3.txt", "r") as input_file:
    lines = input_file.readlines()
    lines = [line.strip() for line in lines]


symbol_locations = find_symbols(lines)
adjacent_number_locations = extract_numbers_with_variations(lines)
part_codes = []

# checking each number and adjacent location and if it is in symbol locations, adding it to a list of part codes
for number_code, locations in adjacent_number_locations.items():
    for location in locations:
        if location in symbol_locations:
            part_codes.append(number_code)

# turning part_codes into set to remove duplicates
part_codes_set = set(part_codes)
result = 0

# extracting part number from each part code and adding it to the result
for part_code in part_codes_set:
    code = int(part_code.split("-")[2])
    result += code

print(result)

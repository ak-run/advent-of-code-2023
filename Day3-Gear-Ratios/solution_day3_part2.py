import random


def find_asterix(strings):
    """Find symbols in the engine schematics matrix and save their locations in a list of tuples"""
    asterix_locations_list = []

    for i, string in enumerate(strings):
        for j, char in enumerate(string):
            if char == "*":
                asterix_locations_list.append((i, j))

    return asterix_locations_list


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


asterix_locations = find_asterix(lines)
adjacent_number_locations = extract_numbers_with_variations(lines)

# removing duplicate locations
for number_code, locations in adjacent_number_locations.items():
    adjacent_number_locations[number_code] = list(set(locations))

part_codes = {}

# creating dictionary with all part codes
for number_code, locations in adjacent_number_locations.items():
    part_codes[number_code] = []

# checking each number and adjacent location and if it is in symbol locations, adding it to a list of part codes
for number_code, locations in adjacent_number_locations.items():
    for location in locations:
        if location in asterix_locations:
            part_codes[number_code].append(location)


part_codes_dict = {}

# mapping all part codes that have locations saved
for part_code, value in part_codes.items():
    if value:
        part_codes_dict[part_code] = value

# Dictionary to store keys from part_codes_dict based on common value
value_to_keys = {}

# Populate the value_to_keys dictionary
for key, value in part_codes_dict.items():

    value_tuple = tuple(value)

    if value_tuple not in value_to_keys:
        value_to_keys[value_tuple] = [key]
    else:
        value_to_keys[value_tuple].append(key)

# Filter out items with only one key in the list (no duplicates)
duplicates = {k: v for k, v in value_to_keys.items() if len(v) > 1}

result = 0


#
for value_tuple, keys in duplicates.items():
    part_1 = int(keys[0].split("-")[2])
    part_2 = int(keys[1].split("-")[2])
    multiplication = part_1 * part_2
    result += multiplication


print(f"The sum of all of the gear ratios in engine schematic is {result}.")

"""
The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green
cubes, and 14 blue cubes?
"""
from itertools import chain


def replace_punctuation_with_commas(string):
    """
    Function to replace ; and : with commas in the input stings
    This way I'll be able to split them into lists using comma as separator
    """
    new_string = string.replace(";", ",")
    result_string = new_string.replace(":", ",")
    return result_string


def make_list_of_possibilities(red_num, green_num, blue_num):
    """Function to make a list of all possible cube numbers the elf can take out of the bag"""
    possibilities_red = []
    possibilities_green = []
    possibilities_blue = []
    for i in range(1, red_num+1):
        possibilities_red.append(f"{i} red")
    for i in range(1, green_num+1):
        possibilities_green.append(f"{i} green")
    for i in range(1, blue_num+1):
        possibilities_blue.append(f"{i} blue")
    # using itertools.chain to combine the three lists
    all_possibilities = list(chain(possibilities_red, possibilities_green, possibilities_blue))
    return all_possibilities


def remove_possible(list_of_possibilities, list_to_filter):
    """Removing all possible number of cubest from each list"""
    filtered_list = list(filter(lambda x: x not in list_of_possibilities, list_to_filter))
    return filtered_list


possibilities = make_list_of_possibilities(12, 13, 14)
result = 0

with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    for index, line in enumerate(lines):
        # split each line into a list and remove the first element (which is the Game number)
        game_list = replace_punctuation_with_commas(line).strip().split(", ")
        game_list.pop(0)
        filtered_line = remove_possible(possibilities, game_list)
        # Each list that's empty represents a game that's possible and its index + 1 is the game number added to result
        if not filtered_line:
            result += index + 1


print(result)

"""
As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.
"""


def replace_punctuation_with_commas(string):
    """
    Function to replace ; and : with commas in the input stings
    This way I'll be able to split them into lists using comma as separator
    """
    new_string = string.replace(";", ",")
    result_string = new_string.replace(":", ",")
    return result_string


def get_grouped_colours_dict(game):
    """Function to return a dictionary of number of cubes taken out by elf in a game
    returns dictionary with colours as keys and numbers representing the cubes sorted in ascending order"""
    color_groups = {'red': [], 'green': [], 'blue': []}
    for item in game:
        parts = item.split()
        if len(parts) == 2:
            color, value = parts[1], parts[0]
            color_groups.setdefault(color, []).append(int(f"{value}"))
        else:
            print(f"Invalid entry: {item}. Skipping.")

    # Sort each list in color_groups
    for color, games in color_groups.items():
        color_groups[color] = sorted(games)

    return color_groups


def power_of_highest_numbers(dict):
    """Function to calculate power of highest numbers in a dictionary for each cube colour"""
    power_result = 1
    for key, lst in dict.items():
        power_result *= lst[-1]
    return power_result


result = 0

with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        # split each line into a list and remove the first element (which is the Game number)
        game = replace_punctuation_with_commas(line).strip().split(", ")
        game.pop(0)
        game_dict = get_grouped_colours_dict(game)
        game_result = power_of_highest_numbers(game_dict)
        result += game_result


print(f"The sum of the power of the sets is {result}.")

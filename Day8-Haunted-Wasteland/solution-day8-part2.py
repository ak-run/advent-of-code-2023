# Using cycle to iterate over input directions in a cycle
import math
from itertools import cycle


with open("input_day8.txt", "r") as file:
    # Read lines from the file and remove leading/trailing whitespaces
    lines = [line.strip() for line in file.readlines()]

# Extract directions as a list of chars, turn it into cycle object
directions = list(lines[0])
directions_cycle = cycle(directions)

# Initialise a dictionary to store network
network = {}

# Process the lines to create a dictionary with tuples
for line in lines[1:]:
    parts = line.split("=")
    var_name = parts[0].strip()
    values = tuple(part.strip(" (),") for part in parts[1].strip().split(",")) if len(parts) > 1 else ("", "")
    network[var_name] = values


def steps_to_get_to_z(current_node, network):
    """Function to calculate number of steps to get to node ending with Z"""
    num_of_steps = 0
    # While loop to find node ending with Z
    while current_node[-1] != "Z":
        # accessing next direction from the cycle object
        direction = next(directions_cycle)
        # if direction is L access left node, if right, right node, update result
        if direction == "L":
            num_of_steps += 1
            current_node = network.get(current_node)[0]
        else:
            num_of_steps += 1
            current_node = network.get(current_node)[1]
    return num_of_steps


def lcm_of_list(numbers):
    """Function to calculate the lowest common multiplier of a list of numbers"""
    # Set result as the first number in the list
    lcm_result = numbers[0]

    # Calculate LCM for each number in the list
    for num in numbers[1:]:
        lcm_result = lcm_result * num // math.gcd(lcm_result, num)

    return lcm_result


# Save a list of nodes ending with A
nodes_ending_with_a = {key for key, value in network.items() if key.endswith('A')}


list_of_results = []
for node in nodes_ending_with_a:
    num_of_steps = steps_to_get_to_z(node, network)
    list_of_results.append(num_of_steps)


result = lcm_of_list(list_of_results)


print(f"{result} steps are required for all nodes ending with A to reach nodes ending with Z.")



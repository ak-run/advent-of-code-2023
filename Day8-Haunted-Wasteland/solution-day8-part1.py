# Using cycle to iterate over input directions in a cycle
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


def steps_to_get_to_z(node, network):
    """Function to calculate number of steps to get to node ending with Z"""
    num_of_steps = 0
    # While loop to find node ending with Z
    while node[-1] != "Z":
        # accessing next direction from the cycle object
        direction = next(directions_cycle)
        # if direction is L access left node, if right, right node, update result
        if direction == "L":
            num_of_steps += 1
            node = network.get(node)[0]
        else:
            num_of_steps += 1
            node = network.get(node)[1]
    return num_of_steps


result = steps_to_get_to_z("AAA", network)
print(f"{result} steps are required to reach ZZZ.")



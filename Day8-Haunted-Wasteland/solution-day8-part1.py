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


result = 0
position = "AAA"
# While loop to find ZZZ
while position != "ZZZ":
    # accessing next direction from the cycle object
    direction = next(directions_cycle)
    # if direction is L access left node, if right, right node, update result
    if direction == "L":
        result += 1
        position = network.get(position)[0]
    else:
        result += 1
        position = network.get(position)[1]

print(f"{result} steps are required to reach ZZZ.")



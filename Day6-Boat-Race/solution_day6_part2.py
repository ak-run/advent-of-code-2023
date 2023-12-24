time_values = [41667266]
distance_values = [244104712281040]

# Zip the two lists
zipped_data = zip(time_values, distance_values)

# Convert the result to a list
record_races_list = list(zipped_data)


def win_race(record_holding_race):
    """Function that takes a tuple with time and distance and calculates number of ways to break a record"""
    time_value, distance_value = record_holding_race
    ways_to_break_record = 0
    # Loop from the front to find starting position
    for first_record_breaking_pos in range(1, time_value):
        if (time_value - first_record_breaking_pos) * first_record_breaking_pos > distance_value:
            break  # Break the loop when the first match is found
    # Loop from the back to find finishing position
    for last_record_breaking_pos in range(time_value - 1, 0, -1):
        if (time_value - last_record_breaking_pos) * last_record_breaking_pos > distance_value:
            break  # Break the loop when the first match is found
    return last_record_breaking_pos - first_record_breaking_pos + 1


result = 1
for record_race in record_races_list:
    result *= win_race(record_race)

print(f"Result of multiplying number of ways you can beat the record is {result}")

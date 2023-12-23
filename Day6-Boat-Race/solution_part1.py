time_values = [41, 66, 72, 66]
distance_values = [244, 1047, 1228, 1040]

# Zip the two lists
zipped_data = zip(time_values, distance_values)

# Convert the result to a list (optional, for visualization purposes)
record_races_list = list(zipped_data)


def win_race(record_holding_race):
    """Function that takes a tuple with time and distance and calculates number of ways to break a record"""
    time_value, distance_value = record_holding_race
    ways_to_break_record = 0
    for num in range(1, time_value):
        if (time_value - num) * num > distance_value:
            ways_to_break_record += 1
    return ways_to_break_record


result = 1
for record_race in record_races_list:
    result *= win_race(record_race)

print(f"Result of multiplying number of ways you can beat the record is {result}")

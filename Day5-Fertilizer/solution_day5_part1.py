# INPUT: file with maps and seeds
# Convert input into lists for each map and for the seeds we have
# Save attributes in the class:
# Based on each array save arrays with ranges of source and destination category
# Iterate over the seeds and find if the number is in the source, save the corresponding fertiliser
# Methods to get to the next category
# Save all locations
# sort that list
# return lowest number
# OUTPUT: lowest location for any of the seeds


class SeedsSystem:
    def __init__(self, input_file):

        # save create attributes from an input file
        with open(input_file, "r") as file:
            content = file.read()
            maps = content.split("\n\n")

            seeds = maps[0][7:]
            self.seed_list = SeedsSystem.split_input(seeds)

            # Skip the first line (header)
            arr1 = maps[1].splitlines()[1:]
            self.seeds_to_soil_map = SeedsSystem.split_items_in_array_add_to_new_list(arr1)

            arr2 = maps[2].splitlines()[1:]
            self.soil_to_fertiliser_map = SeedsSystem.split_items_in_array_add_to_new_list(arr2)

            arr3 = maps[3].splitlines()[1:]
            self.fertiliser_to_water_map = SeedsSystem.split_items_in_array_add_to_new_list(arr3)

            arr4 = maps[4].splitlines()[1:]
            self.water_to_light_map = SeedsSystem.split_items_in_array_add_to_new_list(arr4)

            arr5 = maps[5].splitlines()[1:]
            self.light_to_temperature_map = SeedsSystem.split_items_in_array_add_to_new_list(arr5)

            arr6 = maps[6].splitlines()[1:]
            self.temperature_to_humidity_map = SeedsSystem.split_items_in_array_add_to_new_list(arr6)

            arr7 = maps[7].splitlines()[1:]
            self.humidity_to_location_map = SeedsSystem.split_items_in_array_add_to_new_list(arr7)

    @staticmethod
    def split_items_in_array_add_to_new_list(array):
        new_array = []
        for item in array:
            lst = SeedsSystem.split_input(item)
            new_array.append(lst)
        return new_array

    @staticmethod
    def split_input(string):
        arr = string.strip().split()  # Strip leading/trailing whitespace and split
        int_arr = [int(x) for x in arr if x]  # Convert to integers, filter out empty strings
        return int_arr


seed_system = SeedsSystem("input_day5.txt")
print(seed_system.temperature_to_humidity_map)


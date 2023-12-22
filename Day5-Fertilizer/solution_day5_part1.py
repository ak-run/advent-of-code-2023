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
            self.seeds_to_soil_source = SeedsSystem.category_range(self.seeds_to_soil_map, "source")
            self.seeds_to_soil_destination = SeedsSystem.category_range(self.seeds_to_soil_map, "destination")

            arr2 = maps[2].splitlines()[1:]
            self.soil_to_fertiliser_map = SeedsSystem.split_items_in_array_add_to_new_list(arr2)
            self.soil_to_fertiliser_source = SeedsSystem.category_range(self.soil_to_fertiliser_map, "source")
            self.soil_to_fertiliser_destination = SeedsSystem.category_range(self.soil_to_fertiliser_map, "destination")

            arr3 = maps[3].splitlines()[1:]
            self.fertiliser_to_water_map = SeedsSystem.split_items_in_array_add_to_new_list(arr3)
            self.fertiliser_to_water_source = SeedsSystem.category_range(self.fertiliser_to_water_map, "source")
            self.fertiliser_to_water_destination = SeedsSystem.category_range(self.fertiliser_to_water_map, "destination")

            arr4 = maps[4].splitlines()[1:]
            self.water_to_light_map = SeedsSystem.split_items_in_array_add_to_new_list(arr4)
            self.water_to_light_source = SeedsSystem.category_range(self.water_to_light_map, "source")
            self.water_to_light_destination = SeedsSystem.category_range(self.water_to_light_map, "destination")

            arr5 = maps[5].splitlines()[1:]
            self.light_to_temperature_map = SeedsSystem.split_items_in_array_add_to_new_list(arr5)
            self.light_to_temperature_source = SeedsSystem.category_range(self.light_to_temperature_map, "source")
            self.light_to_temperature_destination = SeedsSystem.category_range(self.light_to_temperature_map, "destination")

            arr6 = maps[6].splitlines()[1:]
            self.temperature_to_humidity_map = SeedsSystem.split_items_in_array_add_to_new_list(arr6)
            self.temperature_to_humidity_source = SeedsSystem.category_range(self.temperature_to_humidity_map, "source")
            self.temperature_to_humidity_destination = SeedsSystem.category_range(self.temperature_to_humidity_map, "destination")

            arr7 = maps[7].splitlines()[1:]
            self.humidity_to_location_map = SeedsSystem.split_items_in_array_add_to_new_list(arr7)
            self.humidity_to_location_source = SeedsSystem.category_range(self.humidity_to_location_map, "source")
            self.humidity_to_location_destination = SeedsSystem.category_range(self.humidity_to_location_map,
                                                                               "destination")

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

    @staticmethod
    def category_range(arr, cat_type):
        range_arr = []
        for sub_arr in arr:

            if cat_type == "source":
                source_arr = [num for num in range(sub_arr[1], sub_arr[1]+sub_arr[2])]
                range_arr.append(source_arr)
            else:
                destination_arr = [num for num in range(sub_arr[0], sub_arr[0] + sub_arr[2])]
                range_arr.append(destination_arr)

        return range_arr


seed_system = SeedsSystem("input_day5.txt")
# print(seed_system.seeds_to_soil_source)
# print(seed_system.seeds_to_soil_destination)
# print(seed_system.soil_to_fertiliser_source)
# print(seed_system.soil_to_fertiliser_destination)
# print(seed_system.fertiliser_to_water_source)
# print(seed_system.fertiliser_to_water_destination)
# print(seed_system.water_to_light_source)
# print(seed_system.water_to_light_destination)
# print(seed_system.light_to_temperature_source)
# print(seed_system.light_to_temperature_destination)
# print(seed_system.temperature_to_humidity_source)
# print(seed_system.temperature_to_humidity_destination)
# print(seed_system.humidity_to_location_source)
# print(seed_system.humidity_to_location_destination)


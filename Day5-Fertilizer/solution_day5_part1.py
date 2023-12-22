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
    """Class to convert seeds to locations using various maps.
    Attributes:
        seed_list (list): List of seed numbers.
        seeds_to_soil_map (list): Map for seed to soil conversion.
        soil_to_fertiliser_map (list): Map for soil to fertiliser conversion.
        fertiliser_to_water_map (list): Map for fertiliser to water conversion.
        water_to_light_map (list): Map for water to light conversion.
        light_to_temperature_map (list): Map for light to temperature conversion.
        temperature_to_humidity_map (list): Map for temperature to humidity conversion.
        humidity_to_location_map (list): Map for humidity to location conversion.

    Methods:
        split_items_in_array_add_to_new_list(array): Splits items in an array and adds them to a new list.
        split_input(string): Splits input string into a list of integers.
        source_to_destination(mappings, source_id): Converts a source id to its corresponding destination id.
        seed_to_location_conversion(): Converts seed numbers to location numbers based on maps.
    """
    def __init__(self, input_file):
        """Initialise the SeedsSystem object and load conversion maps from an input file."""

        # Save conversion maps as attributes of the class
        with open(input_file, "r") as file:
            content = file.read()
            maps = content.split("\n\n")

            seeds = maps[0][7:]
            self.seed_list = SeedsSystem.split_input_into_int(seeds)

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
        """Splits items in an array and adds them to a new list.
        Args:
            array (list): Input array containing items to be split.
        Returns:
            list: New list with items split into sublists.
        """
        new_array = []
        for item in array:
            lst = SeedsSystem.split_input_into_int(item)
            new_array.append(lst)
        return new_array

    @staticmethod
    def split_input_into_int(string):
        """Splits input string into a list of integers.
          Args:
              string (str): Input string to be split.
          Returns:
              list: List of integers obtained from the input string.
          """
        arr = string.strip().split()  # Strip leading/trailing whitespace and split
        int_arr = [int(x) for x in arr if x]  # Convert to integers, filter out empty strings
        return int_arr

    @staticmethod
    def source_to_destination(mappings, source_id):
        """Converts a source id to its corresponding destination id.
        Args:
            mappings (list): List of arrays representing conversion maps.
            source_id (int): Source id to be converted.
        Returns:
            int: Corresponding destination id.
        """
        for mapping in mappings:
            destination_start, source_start, length = mapping
            if source_id in range(source_start, source_start + length):
                return destination_start + (source_id - source_start)
        # If source_id is not in any range, return source_id itself
        return source_id

    def seed_to_location_conversion(self):
        """Converts seed numbers to location numbers based on maps.
        Returns:
            lst: List of locations
        """
        locations = []
        for seed in self.seed_list:
            soil_num = SeedsSystem.source_to_destination(self.seeds_to_soil_map, seed)
            fertilizer_num = SeedsSystem.source_to_destination(self.soil_to_fertiliser_map, soil_num)
            water_num = SeedsSystem.source_to_destination(self.fertiliser_to_water_map, fertilizer_num)
            light_num = SeedsSystem.source_to_destination(self.water_to_light_map, water_num)
            temperature_num = SeedsSystem.source_to_destination(self.light_to_temperature_map, light_num)
            humidity_num = SeedsSystem.source_to_destination(self.temperature_to_humidity_map, temperature_num)
            location = SeedsSystem.source_to_destination(self.humidity_to_location_map, humidity_num)
            locations.append(location)
        return locations


seed_system = SeedsSystem("input_day5.txt")
print(f"The lowest location number is {min(seed_system.seed_to_location_conversion())}")

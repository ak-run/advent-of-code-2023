"""
DAY 1 Part 2 https://adventofcode.com/2023/day/1
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""
import re

result = 0
all_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

number_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# using RegEx to find all numbers in the strings
pattern = r'(?:' + '|'.join(all_numbers) + r')'

number_words_mapping = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9"
}


with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    new_lines = []
    # iterating over lines to add extra last letter to each numeral
    # this will mean the numbers like eightwo will be recongnised by the programme as two digits: 8 and 2
    for line in lines:
        for word in number_words:
            line = line.replace(word, word + word[-1])
        new_lines.append(line)
    for line in new_lines:
        numbers = re.findall(pattern, line, flags=re.IGNORECASE)

        first_digit = numbers[0]
        if first_digit in number_words_mapping:
            new_first_digit = number_words_mapping[first_digit]
        else:
            new_first_digit = first_digit

        last_digit = numbers[-1] if len(numbers) > 1 else numbers[0]
        if last_digit in number_words_mapping:
            new_last_digit = number_words_mapping[last_digit]
        else:
            new_last_digit = last_digit

        # adding first and second digit as a string and turning into integer
        final_number = int(new_first_digit + new_last_digit)
        result += final_number

print(f"The sum of all of the calibration values is {result}")

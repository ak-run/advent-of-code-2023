"""
DAY 1 Part 1 https://adventofcode.com/2023/day/1
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""
import re

result = 0

with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        # using redux to get only numbers
        numbers = re.findall(r'\d+', line)
        numbers_str = "".join(numbers)
        if len(numbers_str) > 1:
            final_number = int(numbers_str[0] + numbers_str[-1])
            result += final_number
        else:
            final_number = int(numbers_str[0] + numbers_str[0])
            result += final_number

print(f"The sum of all of the calibration values is {result}")

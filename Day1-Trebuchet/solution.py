import re

result = 0

with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    print(lines)
    for line in lines:
        # using redux to get only numbers
        numbers = re.findall(r'\d+', line)
        numbers_str = "".join(numbers)
        print(numbers_str)
        if len(numbers_str) > 1:
            final_number = int(numbers_str[0] + numbers_str[-1])
            result += final_number
        else:
            final_number = int(numbers_str[0] + numbers_str[0])
            result += final_number

print(result)


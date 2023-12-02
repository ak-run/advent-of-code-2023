import re

result = 0
number_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

pattern = r'(?:' + '|'.join(number_words) + r')'

number_words_mapping = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10"
}


with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        numbers = re.findall(pattern, line, flags=re.IGNORECASE)
        print(numbers)
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
        final_number = int(new_first_digit + new_last_digit)
        print(final_number)
        result += final_number
        print(result)



print(result)


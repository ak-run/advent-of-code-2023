with open("input_day4.txt", "r") as input_file:
    lines = input_file.readlines()
    lines = [line.split(':', 1)[1].strip() for line in lines]
    print(lines)

scratchcards = []

# def get_scratchcards_list
for line in lines:
    cards = line.split("|")
    card_list = [list(map(int, card.strip().split())) for card in cards]
    scratchcards.append(card_list)


matches = []

for cards in scratchcards:
    filtered_list = [num for num in cards[1] if num in cards[0]]
    matches.append(filtered_list)

print(matches)


def calculate_points(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return 2 ** (number - 1)


result = 0
for match in matches:
    length = len(match)
    points = calculate_points(length)
    result += points

print(result)

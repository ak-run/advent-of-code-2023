def get_scratchcards_list(input_lines):
    """Return a list of input lines with card number removed"""
    scratchcards_list = []
    for line in input_lines:
        cards = line.split("|")
        card_list = [list(map(int, card.strip().split())) for card in cards]
        scratchcards_list.append(card_list)
    return scratchcards_list


def get_list_of_matches(scratchcard_list):
    """Return list of matches between the scratchcards"""
    matches_list = []
    for cards in scratchcard_list:
        filtered_list = [num for num in cards[1] if num in cards[0]]
        matches_list.append(filtered_list)
    return matches_list


def calculate_points(number):
    """Calculate points based on number of matches"""
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return 2 ** (number - 1)


def add_points_from_scratchcards(matches_list):
    """Return the total points for scratchcard pile"""
    points = 0
    for match in matches_list:
        length = len(match)
        points_from_scratchcard = calculate_points(length)
        points += points_from_scratchcard
    return points


with open("input_day4.txt", "r") as input_file:
    lines = input_file.readlines()
    lines = [line.split(':', 1)[1].strip() for line in lines]


scratchcards = get_scratchcards_list(lines)
matches = get_list_of_matches(scratchcards)
result = add_points_from_scratchcards(matches)

print(f"Elf's pile of scratchcards is worth {result} points")

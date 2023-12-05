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


def get_all_scratchcards(matches_list):
    """Return the total number of scratchcards won"""
    scratchcards_count = [1] * len(matches_list)

    for i in range(len(matches_list)):
        match = matches_list[i]
        length = len(match)

        if length > 0:
            for j in range(i + 1, i + length + 1):
                scratchcards_count[j] += scratchcards_count[i]

    return sum(scratchcards_count)


with open("input_day4.txt", "r") as input_file:
    lines = input_file.readlines()
    lines = [line.split(':', 1)[1].strip() for line in lines]


scratchcards = get_scratchcards_list(lines)
matches = get_list_of_matches(scratchcards)
all_scratchcards = get_all_scratchcards(matches)


print(f"Elf has {all_scratchcards} scratchcards.")

# # Get the input data
# with open("input_day7.txt", "r") as file:
#     data = []
#     for line in file.readlines():
#         data.append(line.strip().split(" "))

data = [['32TJK', '765'], ['T55J5', '684'], ['KK677', '28'], ['KTJJT', '220'], ['QQQJA', '483']]


# Sorting function for hands
def hand_sort(hand):
    card_order = "AKQJT98765432"
    return [card_order.index(card) for card in hand[0]]


# Function to categorise hands based on character counts and sort each list
def categorise_and_sort(data):
    categorised_hands = {
        'Five of a kind': [],
        'Four of a kind': [],
        'Full house': [],
        'Three of a kind': [],
        'Two pair': [],
        'One pair': [],
        'High card': []
    }

    for hand in data:
        # Determine hand category based on character counts
        category = None
        char_counts = {card: hand[0].count(card) for card in set(hand[0])}

        if 5 in char_counts.values():
            category = 'Five of a kind'
        elif 4 in char_counts.values():
            category = 'Four of a kind'
        elif 3 in char_counts.values() and 2 in char_counts.values():
            category = 'Full house'
        elif 3 in char_counts.values():
            category = 'Three of a kind'
        elif list(char_counts.values()).count(2) == 2:
            category = 'Two pair'
        elif 2 in char_counts.values():
            category = 'One pair'
        else:
            if 'J' in char_counts:
                category = 'One pair'
            else:
                category = 'High card'

        # Append the hand to the categorised hands
        categorised_hands[category].append(hand)

    # Sort each list based on the sorting function
    for category, hands in categorised_hands.items():
        categorised_hands[category] = sorted(hands, key=hand_sort)

    return categorised_hands


# Categorise the hands based on character counts and sort each list
categorised_data = categorise_and_sort(data)

number_of_hands = len(data)
result = 0

# # Calculate the result
# for category, hands in categorised_data.items():
#     for hand in hands:
#         result += int(hand[1]) * number_of_hands
#         number_of_hands -= 1
#
#
# print(f"The total winnings of Camel Cards are {result}")

# Print the categorized and sorted hands
for category, hands in categorised_data.items():
    print(f'{category}: {hands}')

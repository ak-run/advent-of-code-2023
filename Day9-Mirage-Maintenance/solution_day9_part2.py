with open("input_day9.txt", "r") as file:
    """Read the input file and save lines as lists of integers"""
    lines = file.readlines()
    sequences = []
    for line in lines:
        sequences.append([int(num) for num in line.strip().split(" ")])


def get_next_sequence(sequence):
    """Build a sequence of differences between integers in the input sequence"""
    next_sequence = []
    for idx in range(1, len(sequence)):
        next_sequence.append(sequence[idx] - sequence[idx-1])
    return next_sequence


def all_sequences(sequence):
    """Add all sequences up to sequence with just zeros to a list and return that list"""
    list_of_sequences = [sequence]
    while any(value != 0 for value in sequence):
        sequence = get_next_sequence(sequence)
        list_of_sequences.append(sequence)
    return list_of_sequences


def get_prev_num_in_seq(sequences):
    """Get previous number in a sequence. Input is a list of sequences up to just zeros"""
    for idx in range(1, len(sequences)):
        prev_num = sequences[idx][0] - sequences[idx-1][0]
        sequences[idx].insert(0, prev_num)
    result = sequences[len(sequences)-1][0]
    return result


result = 0
for sequence in sequences:
    # iterate over input sequences and add next numbers in a sequence to result
    list_of_sequences = all_sequences(sequence)
    list_of_sequences.reverse()
    result += get_prev_num_in_seq(list_of_sequences)

print(f"Sum of extrapolated values is {result}.")
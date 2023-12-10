import re

from utils.file_utils import read_lines

if __name__ == "__main__":
    sequences = [[int(item) for item in re.findall(r"-*\d+", line)] for line in read_lines()]
    extrapolated_sequences = []
    for sequence in sequences:
        sequence_sequences = [sequence]
        next_sequence = sequence
        while set(sequence_sequences[-1]) != {0}:
            next_sequence = [next_sequence[i + 1] - next_sequence[i] for i in range(len(next_sequence) - 1)]
            sequence_sequences.append(next_sequence)

        sequence_sequences = sequence_sequences[::-1]
        for i in range(len(sequence_sequences) - 1):
            addition = sequence_sequences[i][-1]
            subtraction = sequence_sequences[i][0]
            prev_sequence = sequence_sequences[i + 1]
            sequence_sequences[i + 1] = [prev_sequence[0] - subtraction, *prev_sequence, prev_sequence[-1] + addition]

        extrapolated_sequences.append(sequence_sequences[-1])

    print(sum([sequence[-1] for sequence in extrapolated_sequences]))
    print(sum([sequence[0] for sequence in extrapolated_sequences]))

import re
from typing import List

from utils.file_utils import read_lines


def difference_sequence(sequence: List[int]) -> List[int]:
    return [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]


def part_one():
    extrapolated_sequences = []
    for sequence in sequences:
        sequence_sequences = [sequence]
        next_sequence = sequence
        while set(sequence_sequences[-1]) != {0}:
            next_sequence = difference_sequence(next_sequence)
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


if __name__ == "__main__":
    sequences = [[int(item) for item in re.findall(r"-*\d+", line)] for line in read_lines()]
    part_one()

import functools
from math import prod

from utils.file_utils import empty_line_separated_group_to_string_lists


def compare_packets(first, second) -> int:
    if isinstance(first, list) and isinstance(second, list):
        for a, b in zip(first, second):
            a_b_comparison = compare_packets(a, b)
            if a_b_comparison != 0:
                return a_b_comparison

        return compare_packets(len(first), len(second))
    if isinstance(first, int) and isinstance(second, int):
        return first - second
    if isinstance(first, int) and isinstance(second, list):
        return compare_packets([first], second)
    if isinstance(first, list) and isinstance(second, int):
        return compare_packets(first, [second])


def part_one():
    pairs = [[eval(packet) for packet in packet_pair] for packet_pair in empty_line_separated_group_to_string_lists()]
    print(sum([idx for idx, (first, second) in enumerate(pairs, 1) if compare_packets(first, second) <= -1]))


def part_two():
    pairs = [[eval(packet) for packet in packet_pair] for packet_pair in empty_line_separated_group_to_string_lists()]

    all_packets = [packet for pair in [*pairs, [[[2]], [[6]]]] for packet in pair]
    sorted_packets = sorted(all_packets, key=functools.cmp_to_key(compare_packets))
    print(prod([idx for idx, packet in enumerate(sorted_packets, 1) if packet == [[2]] or packet == [[6]]]))


if __name__ == "__main__":
    part_one()
    part_two()

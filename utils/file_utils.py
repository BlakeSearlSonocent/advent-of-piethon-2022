from typing import List, Tuple


def read_input() -> str:
    return open("input.txt").read().strip()


def read_lines() -> List[str]:
    with open("input.txt") as f:
        return [line.rstrip() for line in f]


def empty_line_separated_group_to_int_lists() -> List[List[int]]:
    string_lists = empty_line_separated_group_to_string_lists()
    return [[int(item) for item in string_list] for string_list in string_lists]


def empty_line_separated_group_to_string_lists() -> List[List[str]]:
    return [x.split("\n") for x in read_input().split("\n\n")]


def file_to_string_pairs(separator=" ") -> List[Tuple[str, str]]:
    lines = read_lines()
    return [(x, y) for x, y in [line.split(separator) for line in lines]]

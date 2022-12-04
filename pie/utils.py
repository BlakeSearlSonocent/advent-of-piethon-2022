import os
from typing import List, Tuple


def file_path(filename: str) -> str:
    return f"{os.getcwd()}/pie/{filename}"


def file_to_string_list(filename: str) -> List[str]:
    with open(file_path(filename)) as f:
        return [line.rstrip() for line in f]


def empty_line_separated_group_to_int_lists(filename: str) -> List[List[int]]:
    string_lists = empty_line_separated_group_to_string_lists(filename)
    return [[int(item) for item in string_list] for string_list in string_lists]


def empty_line_separated_group_to_string_lists(filename: str) -> List[List[str]]:
    return [x.split("\n") for x in open(file_path(filename)).read().strip().split("\n\n")]


def file_to_string_pairs(filename: str, separator=" ") -> List[Tuple[str, str]]:
    lines = file_to_string_list(filename)
    return [(x, y) for x, y in [line.split(separator) for line in lines]]

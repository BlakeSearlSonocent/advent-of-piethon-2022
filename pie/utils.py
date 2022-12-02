import os
from typing import List


def file_to_string_list(filename: str) -> List[str]:
    with open(f'{os.getcwd()}/pie/{filename}') as f:
        return [line.rstrip() for line in f]


def empty_line_separated_group_to_int_lists(filename: str) -> List[List[int]]:
    string_lists = empty_line_separated_group_to_string_lists(filename)
    return [[int(item) for item in string_list] for string_list in string_lists]


def empty_line_separated_group_to_string_lists(filename: str) -> List[List[str]]:
    string_list = file_to_string_list(filename)

    groups = []
    current_group = []
    for item in string_list:
        if item == "":
            groups.append(current_group)
            current_group = []
        else:
            current_group.append(item)

    groups.append(current_group)
    return groups

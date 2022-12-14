import re
from copy import deepcopy
from typing import List, Tuple

from pie.file_utils import read_lines

stacks_input = {
    1: list("QFMRLWCV"),
    2: list("DQL"),
    3: list("PSRGWCNB"),
    4: list("LCDHBQG"),
    5: list("VGLFZS"),
    6: list("DGNP"),
    7: list("DZPVFCW"),
    8: list("CPDMS"),
    9: list("ZNWTVMPC"),
}


def reorder_crates(reverse: bool) -> dict[int, list[str]]:
    commands = get_commands()
    stacks = deepcopy(stacks_input)
    for qty, old, new in commands:
        old_stack = stacks[old]
        new_stack = stacks[new]
        removed_crates = old_stack[-qty:]
        new_stack.extend(reversed(removed_crates) if reverse else removed_crates)
        del old_stack[-qty:]

    return stacks


def print_top_of_stacks(stacks: dict[int, list[str]]):
    top_of_stacks = [stacks[stack_index][-1] for stack_index in stacks]
    print("".join(top_of_stacks))


def get_commands() -> List[Tuple[int, int, int]]:
    lines = read_lines("five/input.txt")
    commands = []
    for line in lines:
        qty, old, new = re.findall(r"\d+", line)
        commands.append((int(qty), int(old), int(new)))

    return commands


def part_one():
    stacks = reorder_crates(reverse=True)
    print_top_of_stacks(stacks)


def part_two():
    stacks = reorder_crates(reverse=False)
    print_top_of_stacks(stacks)


if __name__ == "__main__":
    part_one()
    part_two()

from typing import List

from pie.utils import empty_line_separated_group_to_int_lists


def get_elf_calories() -> List[int]:
    elf_pockets = empty_line_separated_group_to_int_lists(f'one/input.txt')
    return [sum(pocket) for pocket in elf_pockets]


def part_one():
    most_calorific_elf = max(get_elf_calories())
    print(most_calorific_elf)


def part_two():
    descending_calories = sorted(get_elf_calories(), reverse=True)
    three_most_calorific_elves = descending_calories[:3]
    print(sum(three_most_calorific_elves))


if __name__ == '__main__':
    part_one()
    part_two()

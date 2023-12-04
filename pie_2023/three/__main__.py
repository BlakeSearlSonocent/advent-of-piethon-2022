from typing import Tuple, Set

from utils.file_utils import read_lines

checked = set()
symbol_locations = set()
potential_gear_locations = set()


class PartNumber:
    def __init__(self, value: int, bound_box: Set[Tuple[int, int]]):
        self.bound_box = bound_box
        self.value = value


def get_part_value(x: int, y: int, grid) -> int:
    line = grid[y]
    part_value = ""
    i = 0
    while x + i < len(line) and line[x + i].isdigit():
        checked.add((x + i, y))
        part_value += line[x + i]
        i += 1
    return int(part_value)


def get_part_adjacents(x: int, y: int, part_value: int, grid) -> Set[Tuple[int, int]]:
    part_length = len(str(part_value))
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1
    part_box = set()
    for dx in range(-1, part_length + 1):
        for dy in (-1, 0, 1):
            if 0 <= y + dy <= max_y and 0 <= x + dx <= max_x:
                part_box.add((x + dx, y + dy))

    return part_box


def build_potential_part_number(x, y, grid) -> PartNumber:
    part_value = get_part_value(x, y, grid)
    boxes = get_part_adjacents(x, y, part_value, grid)
    return PartNumber(part_value, boxes)


def part_one():
    grid = read_lines()
    potential_part_numbers = get_potential_part_numbers(grid)
    part_numbers = filter_non_part_numbers(potential_part_numbers)
    print(sum(part_number.value for part_number in part_numbers))

    total_gear_ratio = 0
    for potential_gear_location in potential_gear_locations:
        adjacent_part_numbers = []
        for potential_part_number in part_numbers:
            if potential_gear_location in potential_part_number.bound_box:
                adjacent_part_numbers.append(potential_part_number)
        if len(adjacent_part_numbers) == 2:
            gear_ratio = adjacent_part_numbers[0].value * adjacent_part_numbers[1].value
            total_gear_ratio += gear_ratio

    print(total_gear_ratio)


def filter_non_part_numbers(potential_part_numbers):
    part_numbers = set()
    for potential_part_number in potential_part_numbers:
        if len(potential_part_number.bound_box & symbol_locations) > 0:
            part_numbers.add(potential_part_number)
    return part_numbers


def get_potential_part_numbers(grid):
    potential_part_numbers = set()
    for y, line in enumerate(grid):
        for x, val in enumerate(line):
            if val in "0123456789.":
                if val.isdigit() and (x, y) not in checked:
                    potential_part_number = build_potential_part_number(x, y, grid)
                    potential_part_numbers.add(potential_part_number)
            elif val == "*":
                symbol_locations.add((x, y))
                potential_gear_locations.add((x, y))
            else:
                symbol_locations.add((x, y))

            checked.add((x, y))

    return potential_part_numbers


if __name__ == "__main__":
    part_one()

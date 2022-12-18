from typing import Tuple, Set

from pie.file_utils import read_lines


def get_neighbours(cube: Tuple[int, int, int]) -> Set[Tuple[int, int, int]]:
    x, y, z = cube
    return {(x + 1, y, z), (x - 1, y, z), (x, y, z - 1), (x, y, z + 1), (x, y + 1, z), (x, y - 1, z)}


def part_one():
    cubes = {tuple(map(int, line.split(","))) for line in read_lines("eighteen/input.txt")}
    print(sum([len(get_neighbours(cube) - cubes) for cube in cubes]))


def part_two():
    cubes = {tuple(map(int, line.split(","))) for line in read_lines("eighteen/input.txt")}
    min_x, max_x = min(x for x, _, _ in cubes), max(x for x, _, _ in cubes)
    min_y, max_y = min(y for _, y, _ in cubes), max(y for _, y, _ in cubes)
    min_z, max_z = min(z for _, _, z in cubes), max(z for _, _, z in cubes)

    possible_x = range(min_x - 1, max_x + 2)
    possible_y = range(min_y - 1, max_y + 2)
    possible_z = range(min_z - 1, max_z + 2)

    start_point = (min_x - 1, min_y - 1, min_z - 1)
    surrounding_air = {start_point}
    needs_checking = [start_point]

    while len(needs_checking) > 0:
        x, y, z = cube_to_check = needs_checking.pop()
        if x in possible_x and y in possible_y and z in possible_z:
            new_air = get_neighbours(cube_to_check) - surrounding_air - cubes
            surrounding_air.update(new_air)
            needs_checking.extend(new_air)

    print(sum([len(get_neighbours(cube) & surrounding_air - cubes) for cube in cubes]))


if __name__ == "__main__":
    part_one()
    part_two()

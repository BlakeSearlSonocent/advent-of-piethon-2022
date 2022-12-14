import re

from numpy import subtract, sign

from pie.file_utils import read_lines


def solve(part_two=False):
    cave = build_initial_cave()
    cave_bound_bottom = max([y for _, y in cave.keys()])

    sand = 500, 0
    while (500, 0) not in cave:
        _, new_sand_y = new_sand = get_new_sand(cave, sand)
        if new_sand_y == cave_bound_bottom and not part_two:
            break

        if new_sand == sand or new_sand_y == cave_bound_bottom + 1:
            cave[new_sand] = "o"
            new_sand = 500, 0

        sand = new_sand

    print(sum([1 for val in cave.values() if val == "o"]))


def get_new_sand(cave, sand):
    sand_x, sand_y = sand
    if (sand_x, sand_y + 1) not in cave:
        return sand_x, sand_y + 1
    elif (sand_x - 1, sand_y + 1) not in cave:
        return sand_x - 1, sand_y + 1
    elif (sand_x + 1, sand_y + 1) not in cave:
        return sand_x + 1, sand_y + 1

    return sand


def build_initial_cave():
    coords = [
        [tuple(map(int, coord.split(","))) for coord in re.findall("[0-9]+,[0-9]+", line)]
        for line in read_lines("fourteen/input.txt")
    ]
    cave = {}
    for coord_list in coords:
        pairs = zip(coord_list, coord_list[1:])
        for first, second in pairs:
            start_x, start_y = first
            dx, dy = subtract(second, first)
            direction_x, direction_y = sign(dx), sign(dy)

            for i in range(abs(dx) + 1):
                for j in range(abs(dy) + 1):
                    cave[start_x + (direction_x * i), start_y + (direction_y * j)] = "#"

    return cave


if __name__ == "__main__":
    solve()
    solve(part_two=True)

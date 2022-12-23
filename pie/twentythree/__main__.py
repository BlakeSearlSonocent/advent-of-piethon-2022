import collections
from numbers import Complex
from typing import Set, Tuple

from pie.file_utils import read_lines

north = -1j
north_east = 1 + -1j
north_west = -1 + -1j
west = -1
south_west = -1 + 1j
south = 1j
south_east = 1 + 1j
east = 1
dirs = [east, south_east, south, south_west, west, north_west, north, north_east]


def get_suggested_move(round: int, elf: Complex, elves: Set[Complex]) -> Tuple[Complex, Complex]:
    north_elf, south_elf, east_elf, west_elf = elf + north, elf + south, elf + east, elf + west

    north_free = (elf + north) not in elves
    north_east_free = (elf + north_east) not in elves
    east_free = (elf + east) not in elves
    south_east_free = (elf + south_east) not in elves
    south_free = (elf + south) not in elves
    south_west_free = (elf + south_west) not in elves
    west_free = (elf + west) not in elves
    north_west_free = (elf + north_west) not in elves

    can_move_north = north_east_free and north_free and north_west_free
    can_move_south = south_east_free and south_free and south_west_free
    can_move_west = south_west_free and west_free and north_west_free
    can_move_east = south_east_free and east_free and north_east_free

    modded_round = round % 4
    moves = collections.deque(
        [(can_move_north, north_elf), (can_move_south, south_elf), (can_move_west, west_elf), (can_move_east, east_elf)]
    )
    moves.rotate(-modded_round)
    proposed_location = next((move for possible, move in moves if possible), elf)
    return elf, proposed_location


if __name__ == "__main__":
    elves = {
        complex(x, y)
        for y, row in enumerate(read_lines("twentythree/input.txt"))
        for x, val in enumerate(row)
        if val == "#"
    }

    for i in range(10_000_000_000):
        suggested_moves = set()
        elf_needs_moving = False
        for elf in elves:
            neighbours = {elf + neighbour for neighbour in dirs}
            can_move = len(neighbours & elves) > 0
            if can_move:
                elf_needs_moving = True
                suggested_moves.add(get_suggested_move(i, elf, elves))

        if not elf_needs_moving:
            print(i)
            break

        suggested_end_locations = {end for _, end in suggested_moves}
        actual_moves = [
            (start, end)
            for start, end in suggested_moves
            if sum(1 for _, other_end in suggested_moves if other_end == end) == 1
        ]

        for start, end in actual_moves:
            elves.remove(start)
            elves.add(end)

    print(
        (max(elf.real for elf in elves) - min(elf.real for elf in elves) + 1)
        * (max(elf.imag for elf in elves) - min(elf.imag for elf in elves) + 1)
        - len(elves)
    )

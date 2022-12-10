from typing import Tuple

from numpy import sign, subtract

from pie.file_utils import file_to_string_pairs

moves = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}


def knot_delta(lead_knot: Tuple[int, int], follow_knot: Tuple[int, int]) -> Tuple[int, int]:
    dx, dy = subtract(lead_knot, follow_knot)
    if abs(dx) > 1 or abs(dy) > 1:
        return sign(dx), sign(dy)
    else:
        return 0, 0


def count_tail_positions(knot_count: int):
    cmds = [cmd for cmd, qty in file_to_string_pairs("nine/input.txt") for _ in range(int(qty))]

    knots = [(0, 0) for _ in range(knot_count)]
    tail_positions = {(0, 0)}
    for cmd in cmds:
        head_x, head_y = knots[0]
        head_dx, head_dy = moves[cmd]
        knots[0] = (head_x + head_dx, head_y + head_dy)

        for i in range(1, knot_count):
            knot_x, knot_y = knots[i]
            knot_dx, knot_dy = knot_delta(knots[i - 1], knots[i])
            knots[i] = (knot_x + knot_dx, knot_y + knot_dy)

        tail_positions.add(knots[-1])
    print(len(tail_positions))


if __name__ == "__main__":
    count_tail_positions(2)
    count_tail_positions(10)

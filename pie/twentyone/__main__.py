from typing import List

from numpy import sign

from pie.file_utils import read_lines


def find_error_for_equations(replaced_equations: List[str]) -> int:
    root = calc_root_from_equations(replaced_equations)
    return sign(root)


def calc_root_from_equations(replaced_equations):
    loc = {}
    substitutions_remaining = True
    while substitutions_remaining:
        substitutions_remaining = False
        for equation in replaced_equations:
            try:
                exec(equation, None, loc)
            except NameError:
                substitutions_remaining = True
    return loc["root"]


def part_one():
    equations = [line.replace(": ", " = ") for line in read_lines("twentyone/input.txt")]
    print(calc_root_from_equations(equations))


def part_two():
    equations = [line.replace(": ", " = ") for line in read_lines("twentyone/input.txt")]
    without_humn = [
        line.replace("+", "-") if "root" in line else line for line in equations if not line.startswith("humn")
    ]
    estimate, humn_range = 0, (0, 9_999_999_999_999)
    located = False
    while not located:
        humn_range_low, humn_range_high = humn_range
        estimate = (humn_range_low + humn_range_high) // 2
        estimate_equations = [*without_humn, f"humn = {estimate}"]
        error = find_error_for_equations(estimate_equations)
        if error == 0:
            located = True
        elif error < 0:
            humn_range = (humn_range_low, estimate)
        else:
            humn_range = (estimate, humn_range_high)

    print(estimate)


if __name__ == "__main__":
    part_one()
    part_two()

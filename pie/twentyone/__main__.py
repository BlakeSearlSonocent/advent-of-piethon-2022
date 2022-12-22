from typing import List

from numpy import sign

from pie.file_utils import read_lines


def find_error_for_equations(replaced_equations: List[str]) -> int:
    loc = {}
    finished = False
    while not finished:
        finished = True
        for equation in replaced_equations:
            try:
                exec(equation, None, loc)
            except NameError:
                finished = False

    return sign(loc["root"])


def part_two():
    equations = [line.replace(": ", " = ") for line in read_lines("twentyone/input.txt")]
    without_humn = [
        line.replace("+", "-") if "root" in line else line for line in equations if not line.startswith("humn")
    ]
    humn_range = (0, 9_999_999_999_999)
    located = False
    while not located:
        humn_range_low, humn_range_high = humn_range
        estimate = (humn_range_low + humn_range_high) // 2
        estimate_equations = [*without_humn, f"humn = {estimate}"]
        error = find_error_for_equations(estimate_equations)
        if error == 0:
            print(estimate)
            break
        elif error < 0:
            humn_range = (humn_range_low, estimate)
        elif error > 0:
            humn_range = (estimate, humn_range_high)


if __name__ == "__main__":
    part_two()

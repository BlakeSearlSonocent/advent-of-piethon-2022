import math
from collections import defaultdict

from utils.file_utils import read_lines

if __name__ == "__main__":
    lines = read_lines()
    pt_1 = 0
    pt_2 = 0
    for i, line in enumerate(lines):
        draws = line.replace(";", ",").split(":")[1].strip().split(", ")

        valid = True
        maximums = defaultdict(int)
        for draw in draws:
            count_str, colour = draw.split(" ")
            count = int(count_str)
            if (
                (colour == "red" and count > 12)
                or (colour == "green" and count > 13)
                or (colour == "blue" and count > 14)
            ):
                valid = False

            maximums[colour] = max(maximums[colour], count)

        if valid:
            pt_1 += i + 1

        power = math.prod(maximums.values())
        pt_2 += power

    print(pt_1)
    print(pt_2)

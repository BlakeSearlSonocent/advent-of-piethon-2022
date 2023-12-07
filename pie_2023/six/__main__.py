import math

from utils.file_utils import read_lines


def quadratic_roots(a: int, b: int, c: int):
    return (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a), (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)


if __name__ == "__main__":
    times, distances = [[int(entry) for entry in line.split()[1:]] for line in read_lines()]
    time_with_distance = list(zip(times, distances))

    # d < (T - t)t
    # d < Tt - t^2
    # t^2 - Tt + d < 0
    # t < (T +- sqrt(T^2 - 4d)) / 2

    possibles = []
    for time, distance in time_with_distance:
        first, second = quadratic_roots(1, -time, distance)
        possibles.append(math.ceil(max(first, second)) - math.floor(min(first, second)) - 1)

    print(math.prod(possibles))

    time, distance = [int(entry.replace(" ", "")) for line in read_lines() for entry in line.split(":")[1:]]
    first, second = quadratic_roots(1, -time, distance)
    print(math.ceil(max(first, second)) - math.floor(min(first, second)) - 1)

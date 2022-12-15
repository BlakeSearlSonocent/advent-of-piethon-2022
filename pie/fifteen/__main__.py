import re
from typing import Tuple

from pie.file_utils import read_lines


def manhattan_distance(first: Tuple[int, int], second: Tuple[int, int]) -> int:
    first_x, first_y = first
    second_x, second_y = second

    return abs(second_x - first_x) + abs(second_y - first_y)


if __name__ == "__main__":
    lines = read_lines("fifteen/input.txt")
    sensors_and_beacons = [
        [tuple(map(int, coord.split(", y="))) for coord in re.findall("x=(-?[0-9]+, y=-?[0-9]+)", line)]
        for line in lines
    ]

    sensor_and_manhattan = [(sensor, manhattan_distance(sensor, beacon)) for sensor, beacon in sensors_and_beacons]

    positive_gradient_coefficients, negative_gradient_coefficients = set(), set()
    for sensor, manhattan in sensor_and_manhattan:
        sensor_x, sensor_y = sensor
        upper_left_coefficient = sensor_y - sensor_x + manhattan + 1
        upper_right_coefficient = sensor_x + sensor_y + manhattan + 1
        lower_right_coefficient = sensor_y - sensor_x - manhattan - 1
        lower_left_coefficient = sensor_x + sensor_y - manhattan - 1

        positive_gradient_coefficients.add(upper_left_coefficient)
        positive_gradient_coefficients.add(lower_right_coefficient)
        negative_gradient_coefficients.add(upper_right_coefficient)
        negative_gradient_coefficients.add(lower_left_coefficient)

    intersections = set()
    for positive_coefficient in positive_gradient_coefficients:
        for negative_coefficient in negative_gradient_coefficients:
            intersection = (
                (negative_coefficient - positive_coefficient) // 2,
                (positive_coefficient + negative_coefficient) // 2,
            )
            intersections.add(intersection)

    for intersection in intersections:
        intersection_x, intersection_y = intersection
        if 0 <= intersection_x <= 4_000_000 and 0 <= intersection_y <= 4_000_000:
            if all(
                [manhattan_distance(sensor, intersection) > manhattan for sensor, manhattan in sensor_and_manhattan]
            ):
                print((intersection_x * 4_000_000) + intersection_y)

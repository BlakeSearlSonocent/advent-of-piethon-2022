from typing import Set, List, Tuple

from pie.file_utils import file_to_string_pairs


def assignment_set(assignment: str) -> Set[int]:
    start, end = [int(x) for x in assignment.split("-")]
    return set(range(start, end + 1))


def build_assignment_pairs() -> List[Tuple[Set[int], Set[int]]]:
    assignment_strings = file_to_string_pairs("four/input.txt", ",")
    return [
        (assignment_set(first_assignment), assignment_set(second_assignment))
        for first_assignment, second_assignment in assignment_strings
    ]


def part_one():
    assignment_pairs = build_assignment_pairs()
    print(sum([1 for first, second in assignment_pairs if first <= second or second <= first]))


def part_two():
    assignment_pairs = build_assignment_pairs()
    print(sum([1 for first, second in assignment_pairs if len(first & second) > 0]))


if __name__ == "__main__":
    part_one()
    part_two()

from typing import List

from pie.file_utils import read_line
from pie.list_utils import windowed


def no_repeats(subroutine: List[str]) -> bool:
    return len(set(subroutine)) == len(subroutine)


def first_packet_marker_index(subroutine_size: int):
    datastream = read_line("six/input.txt")
    subroutines = windowed(list(datastream), subroutine_size)
    print(next(idx for idx, subroutine in enumerate(subroutines) if no_repeats(subroutine)) + subroutine_size)


if __name__ == "__main__":
    first_packet_marker_index(4)
    first_packet_marker_index(14)

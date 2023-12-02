from more_itertools import windowed

from utils.file_utils import read_input

if __name__ == "__main__":
    print(
        [
            next(
                idx
                for idx, subroutine in enumerate(windowed(read_input(), size))
                if len(set(subroutine)) == len(subroutine)
            )
            + size
            for size in [4, 14]
        ]
    )

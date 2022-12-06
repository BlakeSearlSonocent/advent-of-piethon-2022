from typing import TypeVar, List

T = TypeVar("T")


def windowed(windowable: List[T], window_size: int) -> List[List[T]]:
    return [windowable[i : i + window_size] for i in range(0, len(windowable) - (window_size - 1))]

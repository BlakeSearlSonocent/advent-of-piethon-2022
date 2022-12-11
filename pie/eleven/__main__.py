import math
import operator
import re
from typing import Callable

from pie.file_utils import read_input


def get_handler(op_str: str) -> Callable[[int], int]:
    _, mid, right = op_str.split()

    def handler(x: int) -> int:
        operation = operator.add if mid == "+" else operator.mul
        rhs = int(right) if right.isdigit() else x

        return operation(x, rhs)

    return handler


def get_monkeys():
    question = read_input("eleven/input.txt").split("\n\n")
    monkeys = []
    for group in question:
        _, inventory, op, *test = group.split("\n")
        inventory = [int(x) for x in re.findall("[0-9]+", inventory)]
        handler = get_handler(op.split(" = ")[-1])

        check, if_true, if_false = [int(x) for rule in test for x in re.findall("[0-9]+", rule)]
        monkeys.append((inventory, handler, check, if_true, if_false))

    return monkeys


def exec_rounds(part_two: bool):
    monkeys = get_monkeys()
    inspections = {idx: 0 for idx, _ in enumerate(monkeys)}
    lcm = math.lcm(*[monkey[2] for monkey in monkeys])
    for _ in range(10000 if part_two else 20):
        for idx, monkey in enumerate(monkeys):
            inventory, handler, check, if_true, if_false = monkey
            while len(inventory) > 0:
                item = handler(inventory.pop(0)) % lcm
                if not part_two:
                    item //= 3
                inspections[idx] += 1
                monkeys[if_true if item % check == 0 else if_false][0].append(item)

    inspection_counts = sorted(inspections.values(), reverse=True)
    print(inspection_counts[0] * inspection_counts[1])


if __name__ == "__main__":
    exec_rounds(False)
    exec_rounds(True)

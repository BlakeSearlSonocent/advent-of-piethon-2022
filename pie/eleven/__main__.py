import math
import operator
import re
from typing import Callable, List, Tuple

from utils.file_utils import read_input


class Monkey:
    def __init__(self, inventory: List[int], handler: Callable[[int], int], modulo: int, if_true: int, if_false: int):
        self.inventory = inventory
        self.handler = handler
        self.modulo = modulo
        self.if_true = if_true
        self.if_false = if_false
        self.inspections = 0

    @classmethod
    def from_story(cls, story: str):
        _, inv, op, *test = story.split("\n")
        inventory = [int(x) for x in re.findall("[0-9]+", inv)]
        handler = cls.get_handler(op)
        modulo, if_true, if_false = [int(x) for rule in test for x in re.findall("[0-9]+", rule)]

        return cls(inventory, handler, modulo, if_true, if_false)

    @classmethod
    def get_handler(cls, op):
        _, mid, right = op.split(" = ")[-1].split()

        def handler(x: int) -> int:
            operation = operator.add if mid == "+" else operator.mul
            rhs = int(right) if right.isdigit() else x
            return operation(x, rhs)

        return handler

    def inspect(self, lcm: int, reduce_stress=True) -> Tuple[int, int]:
        item = self.handler(self.inventory.pop(0)) % lcm
        if reduce_stress:
            item //= 3
        self.inspections += 1
        target_monkey = self.if_true if item % self.modulo == 0 else self.if_false
        return item, target_monkey


def exec_rounds(part_two: bool):
    monkeys = [Monkey.from_story(story) for story in read_input().split("\n\n")]
    lcm = math.lcm(*[monkey.modulo for monkey in monkeys])
    for _ in range(10000 if part_two else 20):
        for monkey in monkeys:
            while len(monkey.inventory) > 0:
                item, target_monkey = monkey.inspect(lcm, not part_two)
                monkeys[target_monkey].inventory.append(item)

    inspection_counts = sorted([monkey.inspections for monkey in monkeys])
    print(inspection_counts[-1] * inspection_counts[-2])


if __name__ == "__main__":
    exec_rounds(False)
    exec_rounds(True)

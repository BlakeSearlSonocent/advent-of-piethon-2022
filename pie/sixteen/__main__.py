import re
from typing import Tuple

from pie.file_utils import read_lines


def max_flow(current: str, opened: Tuple, t: int) -> Tuple[int, Tuple]:
    if (current, opened, t) in max_flow_cache:
        return max_flow_cache[(current, opened, t)]

    if t == 30:
        return 0, opened

    best = 0
    # takes one minute to turn the valve on
    total_valve_flow = (29 - t) * flows[current]
    cur_opened = tuple(sorted([*opened, current]))
    for neighbour in neighbours[current]:
        # always open the valve if it's not already opened and has a non-zero total flow
        if current not in opened and total_valve_flow != 0:
            best = max(best, total_valve_flow + max_flow(neighbour, cur_opened, t + 2))
        else:
            best = max(best, max_flow(neighbour, opened, t + 1))

    max_flow_cache[(current, opened, t)] = best
    return best, opened


if __name__ == "__main__":
    flows = {}
    neighbours = {}
    for line in read_lines("sixteen/input.txt"):
        valve = line[6:8]
        flow = int(re.findall("[0-9]+", line)[0])
        _, neighbour_str = line.split(";")
        neighbour_str = neighbour_str.replace("valves", "valve")[len(" tunnels lead to valve ") :]
        neighbours[valve] = neighbour_str.split(", ")
        flows[valve] = flow

    max_flow_cache = {}
    print(max_flow("AA", (), 0))

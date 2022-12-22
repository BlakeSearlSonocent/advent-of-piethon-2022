import os
import re

if __name__ == "__main__":
    puzzle, cmds = [x.split("\n") for x in open(f"{os.getcwd()}/pie/twentytwo/input.txt").read().split("\n\n")]
    cols = len(puzzle[0])
    puzzle = [line.ljust(cols) for line in puzzle]
    rows = len(puzzle)

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    commands = re.findall("[0-9]+|[RL]", cmds[0])

    position = (min(i for i, val in enumerate(puzzle[0]) if val == "."), 0)
    direction = 0

    for cmd in commands:
        if cmd == "R":
            direction += 1
        elif cmd == "L":
            direction -= 1
        else:
            count = int(cmd)
            direction_x, direction_y = directions[direction % len(directions)]

            for _ in range(count):
                position_x, position_y = position
                potential_x, potential_y = (position_x + direction_x) % cols, (position_y + direction_y) % rows

                if puzzle[potential_y][potential_x] == " ":
                    if (direction_x, direction_y) == (1, 0):
                        potential_x = min(i for i, val in enumerate(puzzle[potential_y]) if val != " ")
                    if (direction_x, direction_y) == (-1, 0):
                        potential_x = max(i for i, val in enumerate(puzzle[potential_y]) if val != " ")
                    if (direction_x, direction_y) == (0, 1):
                        column = [val for y in range(rows) for val in puzzle[y][potential_x]]
                        potential_y = min(j for j, val in enumerate(column) if val != " ")
                    if (direction_x, direction_y) == (0, -1):
                        column = [val for y in range(rows) for val in puzzle[y][potential_x]]
                        potential_y = max(j for j, val in enumerate(column) if val != " ")

                if puzzle[potential_y][potential_x] == "#":
                    break

                position = (potential_x, potential_y)

    final_direction = directions[direction % len(directions)]
    direction_score = direction % len(directions)
    print(((position[1] + 1) * 1000) + ((position[0] + 1) * 4) + direction_score)

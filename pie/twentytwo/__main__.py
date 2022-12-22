import os
import re

if __name__ == "__main__":
    puzzle_input, commands_input = [
        x.split("\n") for x in open(f"{os.getcwd()}/pie/twentytwo/input.txt").read().split("\n\n")
    ]
    puzzle = {complex(x, y): val for y, row in enumerate(puzzle_input) for x, val in enumerate(row) if val in ".#"}
    commands = re.findall("[0-9]+|[RL]", commands_input[0])

    position = puzzle_input[0].index(".")
    direction = 1

    for command in commands:
        if command == "R":
            direction *= 1j
        elif command == "L":
            direction *= -1j
        else:
            count = int(command)
            for _ in range(count):
                potential_position = position + direction
                if potential_position not in puzzle:
                    # reverse across the row or column
                    while potential_position - direction in puzzle:
                        potential_position = potential_position - direction

                if puzzle[potential_position] == "#":
                    break

                position = potential_position

    print(int(((position.imag + 1) * 1000) + ((position.real + 1) * 4) + [1, 1j, -1, -1j].index(direction)))

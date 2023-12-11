from utils.file_utils import read_lines


def start_position():
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "S":
                return [x, y]


if __name__ == "__main__":
    grid = read_lines()
    height = len(grid)
    width = len(grid[0])

    start_position = start_position()
    print(start_position)

    last_move = [-1, 0]
    length = 1
    current_position = [start_position[0] - 1, start_position[1]]

    while grid[current_position[1]][current_position[0]] != "S":
        next_tile = grid[current_position[1]][current_position[0]]
        print(f"current_position is {current_position}")
        print(f"next_tile is {next_tile}")
        print(f"last_move is {last_move}")
        if next_tile == "|":
            if last_move == [0, 1]:
                current_position[1] += 1
            elif last_move == [0, -1]:
                current_position[1] -= 1
        if next_tile == "-":
            if last_move == [1, 0]:
                current_position[0] += 1
            elif last_move == [-1, 0]:
                current_position[0] -= 1
        if next_tile == "L":
            if last_move == [0, 1]:
                current_position[0] += 1
                last_move = [1, 0]
            elif last_move == [-1, 0]:
                current_position[1] -= 1
                last_move = [0, -1]
        if next_tile == "J":
            if last_move == [0, 1]:
                current_position[0] -= 1
                last_move = [-1, 0]
            elif last_move == [1, 0]:
                current_position[1] -= 1
                last_move = [0, -1]
        if next_tile == "7":
            if last_move == [0, -1]:
                current_position[0] -= 1
                last_move = [-1, 0]
            elif last_move == [1, 0]:
                current_position[1] += 1
                last_move = [0, 1]
        if next_tile == "F":
            if last_move == [0, -1]:
                current_position[0] += 1
                last_move = [1, 0]
            elif last_move == [-1, 0]:
                current_position[1] += 1
                last_move = [0, 1]

        length += 1
    print(length / 2)

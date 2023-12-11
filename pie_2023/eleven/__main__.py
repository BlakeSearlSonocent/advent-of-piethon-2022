from itertools import combinations

from utils.file_utils import read_lines

if __name__ == "__main__":
    grid = read_lines()
    empty_rows = [i for i, row in enumerate(grid) if all([char == "." for char in row])]
    empty_columns = [i for i in range(len(grid[0])) if all([row[i] == "." for row in grid])]

    galaxies = [[x, y] for x in range(len(grid[0])) for y in range(len(grid)) if grid[y][x] == "#"]
    galaxy_combinations = list(combinations(galaxies, 2))
    distances = []
    for combination in galaxy_combinations:
        x_1, x_2, y_1, y_2 = combination[0][0], combination[1][0], combination[0][1], combination[1][1]
        max_x, max_y, min_x, min_y = max(x_1, x_2), max(y_1, y_2), min(x_1, x_2), min(y_1, y_2)
        additional_columns = sum([999_999 for x in range(min_x, max_x + 1) if x in empty_columns])
        additional_rows = sum([999_999 for y in range(min_y, max_y + 1) if y in empty_rows])
        distance = max_x - min_x + max_y - min_y + additional_columns + additional_rows
        distances.append(distance)
    print(sum(distances))

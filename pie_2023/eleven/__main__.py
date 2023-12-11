from itertools import combinations

from utils.file_utils import read_lines

if __name__ == "__main__":
    grid = read_lines()
    empty_rows = set(i for i, row in enumerate(grid) if set(row) == {"."})
    empty_columns = set(i for i in range(len(grid[0])) if set([row[i] for row in grid]) == {"."})

    galaxies = [[x, y] for x in range(len(grid[0])) for y in range(len(grid)) if grid[y][x] == "#"]
    galaxy_combinations = combinations(galaxies, 2)
    total_distance = 0
    for (x_1, x_2), (y_1, y_2) in galaxy_combinations:
        max_x, max_y, min_x, min_y = max(x_1, x_2), max(y_1, y_2), min(x_1, x_2), min(y_1, y_2)
        additional_columns = len(set(range(min_x, max_x + 1)) & empty_columns) * 999_999
        additional_rows = len(set(range(min_y, max_y + 1)) & empty_rows) * 999_999
        total_distance += max_x - min_x + max_y - min_y + additional_columns + additional_rows

    print(total_distance)

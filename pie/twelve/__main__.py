from string import ascii_letters

from pie.file_utils import file_to_string_list


def solve(with_start=True):
    grid, col_count, row_count, start, target = setup_problem()
    distances = {target: 0}
    visited_non_optimised = [target]
    vecs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while True:
        current_x, current_y = current = visited_non_optimised.pop(0)
        current_height = grid[current_y][current_x]
        current_distance = distances[current]

        if current_height == 0:
            if not with_start or current == start:
                print(current_distance)
                break

        for dx, dy in vecs:
            neighbour_x, neighbour_y = neighbour = current_x + dx, current_y + dy
            neighbour_in_grid = neighbour_x in range(col_count) and neighbour_y in range(row_count)
            valid_neighbour = neighbour_in_grid and current_height - grid[neighbour_y][neighbour_x] <= 1
            neighbour_improved = neighbour not in distances or current_distance + 1 < distances[neighbour]
            if valid_neighbour and neighbour_improved:
                distances[neighbour] = current_distance + 1
                visited_non_optimised.append(neighbour)


def setup_problem():
    grid = [list(line) for line in file_to_string_list("twelve/input.txt")]
    row_count = len(grid)
    col_count = len(grid[0])
    start_x, start_y = start = [(i, j) for j in range(row_count) for i in range(col_count) if grid[j][i] == "S"][0]
    target_x, target_y = target = [(i, j) for j in range(row_count) for i in range(col_count) if grid[j][i] == "E"][0]
    grid[start_y][start_x] = "a"
    grid[target_y][target_x] = "z"
    grid = [[ascii_letters.index(val) for val in row] for row in grid]
    return grid, col_count, row_count, start, target


if __name__ == "__main__":
    solve()
    solve(False)

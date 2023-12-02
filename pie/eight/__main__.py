from functools import reduce
from typing import List

from utils.file_utils import read_lines


def solve():
    lines = read_lines()
    forest = [[int(tree) for tree in line] for line in lines]

    visible_trees = 0
    scenic_scores = []
    column_count = len(forest[0])
    row_count = len(forest)
    for i in range(1, column_count - 1):
        for j in range(1, row_count - 1):
            tree = forest[j][i]
            lines_of_sight = get_lines_of_sight(forest, i, j)

            # part one
            max_heights = [max(sight_line) for sight_line in lines_of_sight]
            if len([1 for maximum in max_heights if tree > maximum]) > 0:
                visible_trees += 1

            # part two
            viewing_distances = [get_viewing_distance(tree, line_of_sight) for line_of_sight in lines_of_sight]
            scenic_score = reduce(lambda x, y: x * y, viewing_distances)
            scenic_scores.append(scenic_score)

    print(visible_trees + (2 * column_count) + (2 * row_count) - 4)
    print(max(scenic_scores))


def get_viewing_distance(tree: int, line_of_sight: List[int]) -> int:
    viewing_distance = 0
    for other_tree in line_of_sight:
        if tree > other_tree:
            viewing_distance += 1
        else:
            return viewing_distance + 1

    return viewing_distance


def get_lines_of_sight(forest: List[List[int]], i: int, j: int) -> List[List[int]]:
    tree_row = forest[j]

    trees_to_left = tree_row[:i][::-1]
    trees_to_right = tree_row[i + 1 :]

    tree_column = [forest[y][i] for y in range(len(forest))]
    trees_up = tree_column[:j][::-1]
    trees_down = tree_column[j + 1 :]

    return [trees_to_left, trees_up, trees_to_right, trees_down]


if __name__ == "__main__":
    solve()

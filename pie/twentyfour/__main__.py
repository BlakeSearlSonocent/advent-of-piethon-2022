from pie.file_utils import read_lines

if __name__ == "__main__":
    lines = read_lines("twentyfour/input.txt")
    walls = set()
    blizzards = set()

    for y, row in enumerate(lines):
        for x, val in enumerate(row):
            pos = complex(x - 1, y - 1)
            if val == "#":
                walls.add(pos)
            elif val == ">":
                blizzards.add((pos, 1))
            elif val == "v":
                blizzards.add((pos, 1j))
            elif val == "<":
                blizzards.add((pos, -1))
            elif val == "^":
                blizzards.add((pos, -1j))

    max_x, max_y = int(max(wall.real for wall in walls)), max(wall.imag for wall in walls)
    walls.add(-2j)
    walls.add(complex(max_x - 1, max_y + 1))

    start = 0 - 1j
    end = (max_x - 1) + 1j * max_y
    t = 0
    points = {start}
    targets = [end, start, end]
    while len(targets) > 0:
        t += 1
        blizzards = {
            (complex((pos.real + direction.real) % max_x, (pos.imag + direction.imag) % max_y), direction)
            for pos, direction in blizzards
        }
        blizzard_locs = {pos for pos, _ in blizzards}
        points = {point + direction for direction in [1, -1j, -1, 1j, 0] for point in points} - blizzard_locs - walls

        # print(f"blizzards are {blizzards}")
        # print(f"points are: {points}")

        if targets[0] in points:
            points = {targets[0]}
            targets.pop(0)
            print(t)

    # print(walls)
    # print(blizzards)

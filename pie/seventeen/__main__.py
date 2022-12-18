from pie.file_utils import read_input

horizontal = [(2, 0), (3, 0), (4, 0), (5, 0)]
cross = [(2, 1), (3, 0), (3, 1), (3, 2), (4, 1)]
l_shape = [(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)]
vertical = [(2, 0), (2, 1), (2, 2), (2, 3)]
square = [(2, 0), (2, 1), (3, 0), (3, 1)]
shapes = [horizontal, cross, l_shape, vertical, square]

if __name__ == "__main__":
    jets = [1 if jet == ">" else -1 for jet in read_input("seventeen/input.txt")]
    print(jets)

    tetris = {(x, 0) for x in range(7)}

    jet_index = 0
    for i in range(1_000_000_000_000):
        current_top = max([y for _, y in tetris])
        shape = [(x, current_top + y + 4) for x, y in shapes[i % 5]]
        if i == 2:
            print(shape)

        came_to_rest = False
        if i == 2:
            print(f"The {i} rock begins falling")
        while True:
            jet = jets[jet_index % len(jets)]
            jet_index += 1

            direction = "right" if jet == 1 else "left"
            jet_adjusted_shape = [(x + jet, y) for x, y in shape]
            if all([(0 <= x <= 6) and (x, y) not in tetris for x, y in jet_adjusted_shape]):
                shape = [(x + jet, y) for x, y in shape]
                if i == 2:
                    print(f"Jet of gas pushes rock {direction}")
            else:
                if i == 2:
                    print(f"Jet of gas pushes rock {direction}, but nothing happens")

            if any([(x, y - 1) in tetris for x, y in shape]):
                if i == 2:
                    print("Rock falls 1 unit, causing it to come to rest")
                    print(f"tetris before settling: {tetris}")
                    print(shape)
                tetris.update(shape)
                if i == 2:
                    print(tetris)
                break

            shape = [(x, y - 1) for x, y in shape]
            if i == 2:
                print("Rock falls 1 unit")

    print(max([y for _, y in tetris]))

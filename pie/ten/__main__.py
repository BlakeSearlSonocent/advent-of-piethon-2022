from pie.file_utils import file_to_string_list

if __name__ == "__main__":
    cmds = [x for c in file_to_string_list("ten/input.txt") for x in ([0] if c == "noop" else [0, int(c.split()[1])])]
    signal, x = 0, 1
    for cycle, cmd in enumerate(cmds):
        print("#" if cycle % 40 in range(x - 1, x + 2) else " ", end="\n" if (cycle + 1) % 40 == 0 else "")
        signal += (cycle + 1) * x if (cycle - 19) % 40 == 0 else 0
        x += cmd
    print(signal)

import time

from pie.file_utils import file_to_string_list

if __name__ == "__main__":
    cmds = [x for c in file_to_string_list("ten/input.txt") for x in ([0] if c == "noop" else [0, int(c.split()[1])])]
    signal, x = 0, 1
    for cycle, cmd in enumerate(cmds, 1):
        time.sleep(0.025)
        print("#" if (cycle - 1) % 40 in {x - 1, x, x + 1} else " ", end="\n" if cycle % 40 == 0 else "", flush=True)
        signal += cycle * x if (cycle - 20) % 40 == 0 else 0
        x += cmd
    print(signal)

from utils.file_utils import read_lines

if __name__ == "__main__":
    cmds = [line.split(" ") for line in read_lines()]

    path, dirs = [], {}
    for cmd in cmds:
        if cmd[0] == "$":
            if cmd[1] == "cd":
                if cmd[2] == "..":
                    path.pop()
                else:
                    path.append(cmd[2])
        elif cmd[0] != "dir":
            for i in range(len(path)):
                file_bytes = int(cmd[0])
                sub_path = tuple(path[: i + 1])
                dirs[sub_path] = dirs.get(sub_path, 0) + file_bytes

    print(sum([dir_size for directory in dirs if (dir_size := dirs[directory]) <= 100000]))

    disk_space = 70000000
    used_space = dirs[tuple("/")]
    current_free_space = disk_space - used_space
    required_free_space = 30000000
    extra_required = required_free_space - current_free_space
    print(min([dir_size for directory in dirs if (dir_size := dirs[directory]) >= extra_required]))

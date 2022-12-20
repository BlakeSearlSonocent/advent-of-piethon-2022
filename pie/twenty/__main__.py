from pie.file_utils import read_lines

if __name__ == "__main__":
    encrypted_file = [int(line.strip()) * 811589153 for line in read_lines("twenty/input.txt")]
    mixing = [(idx, x) for idx, x in enumerate(encrypted_file)]

    for _ in range(10):
        for idx, num in enumerate(encrypted_file):
            mixing.pop(current_index := mixing.index((idx, num)))
            mixing.insert((current_index + num) % len(mixing), (idx, num))

    zero_index = next(i for i, v in enumerate(mixing) if v[1] == 0)
    print(sum([mixing[(zero_index + x) % len(encrypted_file)][1] for x in [1000, 2000, 3000]]))

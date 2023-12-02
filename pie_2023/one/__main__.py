from utils.file_utils import read_lines

string_to_digit = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def part_two():
    lines = read_lines()
    total = 0
    for line in lines:
        digits = []
        for i, char in enumerate(line):
            if char.isdigit():
                digits.append(int(char))

            for string, digit in string_to_digit.items():
                if line[i:].startswith(string):
                    digits.append(digit)

        total += 10 * digits[0] + digits[-1]

    print(total)


def part_one():
    lines = read_lines()
    digits = [[int(i) for i in line if i.isdigit()] for line in lines]
    print(sum([10 * digit[0] + digit[-1] for digit in digits]))


if __name__ == "__main__":
    part_one()
    part_two()

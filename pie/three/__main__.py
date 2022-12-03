from string import ascii_letters

from pie.utils import file_to_string_list


def sum_character_values(characters: list[str]) -> int:
    return sum([ascii_letters.index(char) + 1 for char in characters])


def part_one():
    rucksacks = file_to_string_list("three/input.txt")
    naughty_items = [
        (set(rucksack[0 : len(rucksack) // 2]) & set(rucksack[len(rucksack) // 2 :])).pop() for rucksack in rucksacks
    ]
    print(sum_character_values(naughty_items))


def part_two():
    rucksacks = file_to_string_list("three/input.txt")
    groups = [rucksacks[i : i + 3] for i in range(len(rucksacks)) if i % 3 == 0]
    badges = [(set(a) & set(b) & set(c)).pop() for a, b, c in groups]
    print(sum_character_values(badges))


if __name__ == "__main__":
    part_one()
    part_two()

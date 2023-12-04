import re

from utils.file_utils import read_lines

if __name__ == "__main__":
    lines = read_lines()
    numbers_and_winners = [
        (re.findall(r"\d+", thing.split("|")[0]), re.findall(r"\d+", thing.split("|")[1]))
        for card in lines
        for thing in card.split(":")[1:]
    ]

    pt_1 = 0
    cards = [1 for _ in numbers_and_winners]
    for i in range(len(numbers_and_winners)):
        numbers, winners = numbers_and_winners[i]
        numbers_set = {number for number in numbers}
        winners_set = {winner for winner in winners}
        winners_count = len(numbers_set & winners_set)
        if winners_count > 0:
            pt_1 += 2 ** (winners_count - 1)

        for j in range(winners_count):
            cards[i + j + 1] += cards[i]
    print(pt_1)

    print(sum(cards))

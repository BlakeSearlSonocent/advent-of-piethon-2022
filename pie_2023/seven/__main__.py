from collections import Counter

from utils.file_utils import read_lines

face_card_values = {"T": "H", "J": "F", "Q": "D", "K": "B", "A": "A"}


def hand_strength(hand):
    hand_replaced = ["23456789TJQKA".index(card) for card in hand]
    counter = Counter(hand_replaced)
    sorted_counts = sorted(counter.values())

    if sorted_counts == [1, 1, 1, 1, 1]:
        return 0, hand_replaced
    elif sorted_counts == [1, 1, 1, 2]:
        return 1, hand_replaced
    elif sorted_counts == [1, 2, 2]:
        return 2, hand_replaced
    elif sorted_counts == [1, 1, 3]:
        return 3, hand_replaced
    elif sorted_counts == [2, 3]:
        return 4, hand_replaced
    elif sorted_counts == [1, 4]:
        return 5, hand_replaced
    elif sorted_counts == [5]:
        return 6, hand_replaced


if __name__ == "__main__":
    print(sorted(["abc123", "123"]))

    # [(cards, bid) for cards, bid in line.strip().split(" ")]
    hand_and_bid = [(list(line.split()[0]), line.split()[1]) for line in read_lines()]

    sorted_hand_and_bid = sorted(hand_and_bid, key=lambda x: hand_strength(x[0]))

    total = 0
    for i, (hand, bid) in enumerate(sorted_hand_and_bid):
        total += (int(i) + 1) * int(bid)

    print(total)

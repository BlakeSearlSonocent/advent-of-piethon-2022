from collections import Counter

from utils.file_utils import read_lines


def hand_strength_pt1(hand):
    hand_replaced = ["23456789TJQKA".index(card) for card in hand]
    counter = Counter(hand_replaced)
    sorted_counts = sorted(counter.values())
    strength = [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]].index(sorted_counts)
    return strength, hand_replaced


def hand_strength_pt_2(hand):
    potential_strengths = []
    for replacement in "23456789TQKA":
        new_hand = [replacement if card == "J" else card for card in hand]
        counter = Counter(new_hand)
        sorted_counts = sorted(counter.values())
        strength = [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]].index(sorted_counts)
        potential_strengths.append(strength)

    hand_replaced = ["J23456789TQKA".index(card) for card in hand]
    return max(potential_strengths), hand_replaced


if __name__ == "__main__":
    hand_and_bid = [(h, int(b)) for h, b in (line.split() for line in read_lines())]

    for part_one in [True, False]:
        sorted_hand_and_bid = sorted(
            hand_and_bid, key=lambda x: hand_strength_pt1(x[0]) if part_one else hand_strength_pt_2(x[0])
        )
        print(sum([i * bid + bid for i, (_, bid) in enumerate(sorted_hand_and_bid)]))

from pie.utils import file_to_string_pairs


def map_to_symbol(choice: str) -> str:
    if choice == "A" or choice == "X":
        return "Rock"
    if choice == "B" or choice == "Y":
        return "Paper"
    if choice == "C" or choice == "Z":
        return "Scissors"


def map_to_win_requirement(symbol: str) -> str:
    if symbol == "X":
        return "lose"
    if symbol == "Y":
        return "draw"
    if symbol == "Z":
        return "win"


def get_symbol_score(symbol: str) -> int:
    if symbol == "Rock":
        return 1
    if symbol == "Paper":
        return 2

    return 3


def get_competition_score(opponent: str, my: str) -> int:
    if opponent == "Rock" and my == "Scissors":
        return 0
    if opponent == "Rock" and my == "Paper":
        return 6

    if opponent == "Paper" and my == "Rock":
        return 0
    if opponent == "Paper" and my == "Scissors":
        return 6

    if opponent == "Scissors" and my == "Paper":
        return 0
    if opponent == "Scissors" and my == "Rock":
        return 6

    return 3


def get_score(opponent: str, my: str) -> int:
    return get_symbol_score(my) + get_competition_score(opponent, my)


def get_required_symbol(opponent_choice: str, requirement: str) -> str:
    if requirement == "draw":
        return opponent_choice

    if requirement == "lose":
        if opponent_choice == "Rock":
            return "Scissors"
        if opponent_choice == "Paper":
            return "Rock"
        if opponent_choice == "Scissors":
            return "Paper"

    if requirement == "win":
        if opponent_choice == "Rock":
            return "Paper"
        if opponent_choice == "Paper":
            return "Scissors"
        if opponent_choice == "Scissors":
            return "Rock"


def part_one():
    pairs = file_to_string_pairs('two/input.txt')
    strategy = [(map_to_symbol(first), map_to_symbol(second)) for first, second in pairs]
    print(sum([get_score(opponent, my) for opponent, my in strategy]))


def part_two():
    strategy_input = file_to_string_pairs('two/input.txt')
    mapped_strategy = [(map_to_symbol(x), map_to_win_requirement(y)) for x, y in strategy_input]
    pairs = [(opponent, get_required_symbol(opponent, requirement)) for (opponent, requirement) in mapped_strategy]
    print(sum([get_score(opponent, my) for opponent, my in pairs]))


if __name__ == '__main__':
    part_one()
    part_two()

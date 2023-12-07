from collections import Counter


# NOTE: J is now the lowest scoring card!
CARD_STRENGTH = ("A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J")
CARD_SCORES = {card: i for i, card in enumerate(reversed(CARD_STRENGTH))}


def load_example():
    with open("example_input.txt") as f:
        return f.readlines()


def load_example_extra():
    with open("example_input_extra.txt") as f:
        return f.readlines()


def load_input():
    with open("input.txt") as f:
        return f.readlines()


def total_winnings(lines: list[str]) -> int:
    hands: list[list[str]] = [line.strip().split() for line in lines]
    sorted_hands: list[list[str]] = sorted(hands, key=sort_hand)
    # _ = [print(h) for h in sorted_hands]
    return sum((i + 1) * int(bid) for i, (_, bid) in enumerate(sorted_hands))


def sort_hand(inp: list[str]) -> int:
    C = 14  # len(CARD_SCORES) + 1
    hand, _ = inp
    value_cards: int = sum(
        C**i * CARD_SCORES[card_val] for i, card_val in enumerate(reversed(hand))
    )
    value_type: int = C**C * score_hand_by_type(hand)
    # print(hand, value_cards + value_type, value_type, value_cards, "\n")
    return value_cards + value_type


def score_hand_by_type(hand: str):
    cnts: Counter = Counter(hand)
    if "J" in cnts and len(cnts) != 1:
        n_jokers: int = cnts.pop("J")
        highest_value_card: str = sorted(
            [k for k, v in cnts.items() if v == max(cnts.values())],
            key=lambda x: CARD_SCORES[x],
        )[0]
        cnts[highest_value_card] += n_jokers

    n_cnts: int = len(cnts)
    max_cnt: int = max(cnts.values())
    if n_cnts == 1:  # Five of a kind
        return 7

    if n_cnts == 2:
        if max_cnt == 4:  # Four of a kind
            return 6
        else:  # Full house
            return 5

    if n_cnts == 3:
        if max_cnt == 3:  # Three of a kind
            return 4
        else:  # Two pairs
            return 3

    if n_cnts == 4:  # One pair
        return 2

    return 1


def write_result(result: int) -> None:
    with open("result_B.txt", "w") as f:
        f.write(str(result))


def main():
    n_example: int = total_winnings(load_example())
    msg: str = f"Failed example_input_B: {n_example}!=5905"
    assert n_example == 5905, msg

    n_extra: int = total_winnings(load_example_extra())
    msg: str = f"Failed example_input_extra: {n_extra}!=6839"
    assert n_extra == 6839, msg

    result: int = total_winnings(load_input())
    print("Total winnings:", result)
    write_result(result)


if __name__ == "__main__":
    main()

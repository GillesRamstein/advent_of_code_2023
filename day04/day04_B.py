import re
from collections import defaultdict


def load_example() -> list[str]:
    with open("example_input_B.txt") as f:
        return f.readlines()


def load_input() -> list[str]:
    with open("input.txt") as f:
        return f.readlines()


def count_total_scratchcards(cards: list[str]) -> int:
    n_winners, n_owned = (
        len(re.findall(r"\d+", s)) for s in cards[0].split(":")[-1].split("|")
    )

    total_cards = 0
    copies: dict[int, int] = defaultdict(lambda: 1)
    for i in range(len(cards)):
        _, _, *numbers = cards[i].split()
        winners: set[str] = set(numbers[:n_winners])
        owned: set[str] = set(numbers[-n_owned:])
        n_matches: int = len(winners & owned)
        total_cards += copies[i]
        for j in range(i, i + n_matches):
            copies[j + 1] += copies[i]

    return total_cards


def write_result(result: int) -> None:
    with open("result_B.txt", "w") as f:
        f.write(str(result))


def main():
    total_cards_example: int = count_total_scratchcards(cards=load_example())
    assert total_cards_example == 30, "Failed on example_input_B!"

    total_cards: int = count_total_scratchcards(cards=load_input())
    print("Total cards:", total_cards)
    write_result(total_cards)


if __name__ == "__main__":
    main()

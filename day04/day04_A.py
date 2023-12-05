import re


def load_example() -> list[str]:
    with open("example_input_A.txt") as f:
        return f.readlines()


def load_input() -> list[str]:
    with open("input.txt") as f:
        return f.readlines()


def count_total_points(lines: list[str]) -> int:
    total_points: int = 0

    n_winners, n_owned = (
        len(re.findall(r"\d+", s)) for s in lines[0].split(":")[-1].split("|")
    )

    for line in lines:
        _, _, *numbers = line.split()
        winners: set[str] = set(numbers[:n_winners])
        owned: set[str] = set(numbers[-n_owned:])
        n_matches: int = len(winners & owned)
        points: int = 2 ** (n_matches - 1) if n_matches else 0
        total_points += points
    return total_points


def write_result(result: int) -> None:
    with open("result_A.txt", "w") as f:
        f.write(str(result))


def main():
    assert count_total_points(lines=load_example()) == 13, "Failed on example_input_A!"
    total_points: int = count_total_points(lines=load_input())
    print("Total points:", total_points)
    write_result(total_points)


if __name__ == "__main__":
    main()

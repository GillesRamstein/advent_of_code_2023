import re
from typing import Iterable


def load_example() -> list[str]:
    with open("example_input.txt") as f:
        return f.readlines()


def load_input() -> list[str]:
    with open("input.txt") as f:
        return f.readlines()


def parse_input(lines: list[str]) -> tuple[tuple[int, int], ...]:
    times: Iterable = map(int, re.findall(r"\d+", lines[0]))
    distances: Iterable = map(int, re.findall(r"\d+", lines[1]))
    return tuple((t, d) for t, d in zip(times, distances))


def solution(races: tuple[tuple[int, int], ...]) -> int:
    prod_n: int = 1
    for time, distance in races:
        prod_n *= count_record_breakers(time, distance)
    return prod_n


def count_record_breakers(time: int, record: int) -> int:
    n: int = 0
    for i in range(time):
        if i * (time - i) <= record:
            continue
        n += 1
    return n


def write_result(result: int) -> None:
    with open("result_A.txt", "w") as f:
        f.write(str(result))


def main():
    n_example: int = solution(parse_input(load_example()))
    assert n_example == 288, f"Failed example_input_A: {n_example}!=288"

    n: int = solution(parse_input(load_input()))
    print("Product of record breaker counts:", n)
    write_result(n)


if __name__ == "__main__":
    main()

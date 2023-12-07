import re


def load_example() -> list[str]:
    with open("example_input.txt") as f:
        return f.readlines()


def load_input() -> list[str]:
    with open("input.txt") as f:
        return f.readlines()


def parse_input(lines: list[str]) -> tuple[int, int]:
    time: int = int("".join(re.findall(r"\d+", lines[0])))
    distance: int = int("".join(re.findall(r"\d+", lines[1])))
    return time, distance


def count_record_breakers(time: int, record: int) -> int:
    n: int = 0
    for i in range(time):
        if i * (time - i) <= record:
            continue
        n += 1
    return n


def write_result(result: int) -> None:
    with open("result_B.txt", "w") as f:
        f.write(str(result))


def main():
    n_example: int = count_record_breakers(*parse_input(load_example()))
    assert n_example == 71503, f"Failed example_input_B: {n_example}!=71503"

    n: int = count_record_breakers(*parse_input(load_input()))
    print("Product of record breaker counts:", n)
    write_result(n)


if __name__ == "__main__":
    main()

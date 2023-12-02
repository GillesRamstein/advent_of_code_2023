import re
from pathlib import Path

INPUT_PATH = Path("input.txt")
OUTPUT_PATH = Path("calibration_value_B.txt")

STRING_DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

PATTERN = r"(?=(\d))|(?=(" + "))|(?=(".join(STRING_DIGITS.keys()) + "))"
print("Pattern:", PATTERN)


def read_input(file_path: Path) -> str:
    with open(file_path) as f:
        return f.read()


def find_calibration_values(input: str) -> list[int]:
    result = []
    for line in input.split("\n"):
        if not line:
            continue

        matches = re.findall(PATTERN, line)
        digits = [d for m in matches for d in m if d]
        first = STRING_DIGITS.get(digits[0], digits[0])
        last = STRING_DIGITS.get(digits[-1], digits[-1])
        two_digit_number = int(first + last)
        result.append(two_digit_number)

    return result


def dump_output(magic_number: int, file_path: Path):
    with open(file_path, "w") as f:
        f.write(str(magic_number))


def main():
    input_text = read_input(INPUT_PATH)
    calibration_values = find_calibration_values(input_text)
    result = sum(calibration_values)
    print(result)
    dump_output(result, OUTPUT_PATH)


if __name__ == "__main__":
    main()

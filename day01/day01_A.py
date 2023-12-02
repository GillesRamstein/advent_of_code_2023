import re
from pathlib import Path

INPUT_PATH = Path("input.txt")
OUTPUT_PATH = Path("calibration_value_A.txt")


def read_input(file_path: Path) -> str:
    with open(file_path) as f:
        return f.read()


def find_boundary_digits(string: str) -> int:
    digits = re.findall(r"\d", string)
    assert digits, f"No digits in '{string}'"
    return int(digits[0] + digits[-1])


def find_calibration_values(input: str) -> list[int]:
    result = []
    for line in input.split("\n"):
        if not line:
            continue
        two_digit_number = find_boundary_digits(line)
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

def find_next_number(s: str, offset: int = 0) -> tuple[int, int] | None:
    """Return start and end indices of next number in string s."""
    number_start: int = -1
    number_end: int = -1
    end = len(s)
    for i, c in enumerate(s[offset:]):
        if number_start == -1 and c.isdigit():
            number_start = i
            continue

        if number_start == -1:
            continue

        if not c.isdigit():
            number_end = i
            return (number_start + offset, number_end + offset)

    if number_start != -1:
        return (number_start + offset, end + offset)

    return None


def main() -> int:
    with open("input.txt") as f:
        data = f.read()
    SYMBOLS = set(data) - {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"} - {"."}

    lines = data.split("\n")[:-1]
    symbol_indices = [[i for i, c in enumerate(line) if c in SYMBOLS] for line in lines]
    N = len(symbol_indices)

    result = 0
    for i in range(len(lines)):
        print("\n", "#" * 72, i, "#" * 72, "\n")
        if i > 0:
            print(i - 1, "prev:", lines[i - 1])
        print(i, "curr:", lines[i])
        if i < len(lines) - 1:
            print(i + 1, "next:", lines[i + 1])

        symbol_ids = {
            i for j in symbol_indices[max(0, i - 1) : min(N, i + 2)] for i in j
        }
        print("Relevant Symbol IDs:", sorted(symbol_ids))

        part_numbers = []
        num_start = num_end = 0
        while tmp := find_next_number(lines[i], offset=num_end):
            num_start, num_end = tmp
            for j in range(num_start - 1, num_end + 1):
                if j in symbol_ids:
                    result += int(lines[i][num_start:num_end])
                    part_numbers.append(int(lines[i][num_start:num_end]))
                    break
        print("Part Numbers:", part_numbers)

    return result


if __name__ == "__main__":
    result: int = main()
    with open("result_A.txt", "w") as f:
        f.write(str(result))
    print("\nResult:", result)

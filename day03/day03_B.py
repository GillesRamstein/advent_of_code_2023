from collections import defaultdict
import re


def show_window_no_gear(lines, i, j, n_chars, n_lines) -> None:
    lprev: str = lines[i - 1].strip("\n") if i > 0 else "." * n_chars
    lcurr: str = lines[i].strip("\n")
    lnext: str = lines[i + 1].strip("\n") if i < n_lines - 1 else "." * n_lines
    w_min: int = max(j - 3, 0)
    w_max: int = min(j + 4, n_chars)
    window: str = (
        f"{'-' * 13}\n"
        f"{' '.join(lprev[w_min:w_max])}\n"
        f"{' '.join(lcurr[w_min:w_max])}\n"
        f"{' '.join(lnext[w_min:w_max])}\n"
        f"{'-' * 13}\n"
    )
    print(window)


def show_window_with_gear(lines, i, j, n_chars, n_lines) -> None:
    lprev: str = lines[i - 1].strip("\n") if i > 0 else "." * n_chars
    lcurr: str = lines[i].strip("\n")
    lnext: str = lines[i + 1].strip("\n") if i < n_lines - 1 else "." * n_lines
    w_min: int = max(j - 3, 0)
    w_max: int = min(j + 4, n_chars)
    window: str = (
        f"{'-' * 13}\n"
        f"{' '.join(lprev[w_min:w_max])}\n"
        f"{' '.join(lcurr[w_min:w_max])} <<= GEAR\n"
        f"{' '.join(lnext[w_min:w_max])}\n"
        f"{'-' * 13}\n"
    )
    print(window)


def main() -> int:
    with open("input.txt") as f:
        # Why does this work:
        lines: list[str] = ["..." + line + "..." for line in f.readlines()]
        # but not this ?!:   TODO: investigate
        # lines: list[str] = [line for line in f.readlines()]

    numbers_by_idx: dict[int, int] = dict()
    number_ids_by_coordinate: dict[int, dict[int, int]] = defaultdict(dict)
    for n_line, line in enumerate(lines):
        num_starts_at: int = 0
        num_ends_at: int = 0
        for number in re.findall(r"\d+", line):
            num_id: int = len(numbers_by_idx)
            numbers_by_idx[num_id] = int(number)
            num_starts_at = num_ends_at + line[num_ends_at:].find(number, 1)
            num_ends_at = num_starts_at + len(number)
            for n_char in range(num_starts_at, num_ends_at):
                number_ids_by_coordinate[n_line][n_char] = num_id

    N_LINES: int = len(lines)
    N_CHARS: int = len(lines[0])  # assumption that all lines are equal length!

    sum_gear_ratios: int = 0
    for i in range(N_LINES):
        for j in range(N_CHARS):
            if lines[i][j] != "*":
                continue

            j_prev = max(j - 1, 0)
            j_next = min(j + 1, N_CHARS)
            unique_adjacent_num_ids: set[int] = set()
            for ii, jj in [
                (i - 1, j_prev),
                (i - 1, j),
                (i - 1, j_next),
                (i, j_prev),
                (i, j_next),
                (i + 1, j_prev),
                (i + 1, j),
                (i + 1, j_next),
            ]:
                num_id_or_none: int | None = number_ids_by_coordinate.get(ii, {}).get(
                    jj
                )
                if num_id_or_none is not None:
                    unique_adjacent_num_ids.add(num_id_or_none)

            if len(unique_adjacent_num_ids) != 2:
                show_window_no_gear(lines, i, j, N_CHARS, N_LINES)
                continue

            a = numbers_by_idx[unique_adjacent_num_ids.pop()]
            b = numbers_by_idx[unique_adjacent_num_ids.pop()]
            sum_gear_ratios += a * b
            show_window_with_gear(lines, i, j, N_CHARS, N_LINES)

    return sum_gear_ratios


if __name__ == "__main__":
    result: int = main()
    with open("result_B.txt", "w") as f:
        f.write(str(result))
    print("Sum of gear ratios:", result)

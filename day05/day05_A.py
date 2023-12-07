import re


def load_example():
    with open("example_input.txt") as f:
        return f.readlines()


def load_input():
    with open("input.txt") as f:
        return f.readlines()


def find_best_seed_location(lines: list[str]) -> int:
    lines.append("\n")  # to detect last map ending
    locs: list[int] = [int(seed) for seed in re.findall(r"\d+", lines[0])]

    the_map: dict[int, int] = dict()
    for line in lines[2:]:
        # detect map header
        if line[0].isalpha():
            print(f"Applying {line.strip()}")
            the_map = {loc: loc for loc in locs}

        # consume map data
        if line[0].isdigit():
            dst, src, n = map(int, re.findall(r"\d+", line))
            for loc in locs:
                if src <= loc <= src + n:
                    the_map[loc] = loc - src + dst
                else:
                    continue

        # detect map end
        if line == "\n":
            for k, v in dict(sorted(the_map.items())).items():
                print(k, "->", v)
            print("")
            for i in range(len(locs)):
                locs[i] = the_map.get(locs[i], locs[i])

    return min(locs)


def write_result(result: int) -> None:
    with open("result_A.txt", "w") as f:
        f.write(str(result))


def main():
    best_loc_example: int = find_best_seed_location(lines=load_example())
    assert best_loc_example == 35, "Failed example_input_A!"
    print("Succeeded example_input_A!\n")

    best_loc: int = find_best_seed_location(lines=load_input())
    print("Best seed location:", best_loc)
    write_result(best_loc)


if __name__ == "__main__":
    main()

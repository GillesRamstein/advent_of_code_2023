import re
from collections import deque
from dataclasses import dataclass


@dataclass
class Range:
    left: int
    right: int

    def __repr__(self):
        return f"Range: {[self.left, self.right]}"


@dataclass
class MapRange:
    src: Range
    dst: Range

    def __repr__(self):
        return (
            f"MapRange: {[self.src.left,self.src.right]}"
            f" -> {[self.dst.left, self.dst.right]}"
        )


def load_example() -> str:
    with open("example_input.txt") as f:
        return f.read().strip("\n")


def load_input() -> str:
    with open("input.txt") as f:
        return f.read().strip("\n")


def read_seed_ranges(line):
    numbers: list[int] = [int(seed) for seed in re.findall(r"\d+", line)]
    seed_ranges: list[Range] = [
        Range(numbers[i], numbers[i] + numbers[i + 1] - 1)
        for i in range(0, len(numbers), 2)
    ]
    return seed_ranges


def read_map_range(line: str) -> MapRange:
    dst, src, n = map(int, re.findall(r"\d+", line))
    return MapRange(Range(src, src + n - 1), Range(dst, dst + n - 1))


def get_overlap(
    key_range: Range, map_range: MapRange
) -> tuple[Range | None, list[Range]]:
    """Find overlap of key_range and map_range.src.
    Return overlap, [*rest]
    """
    # no overlap
    if map_range.src.right < key_range.left or map_range.src.left > key_range.right:
        return None, [key_range]

    overlap = Range(
        max(key_range.left, map_range.src.left),
        min(key_range.right, map_range.src.right),
    )

    # complete overlap, r1 is inside r2
    if map_range.src.left <= key_range.left and map_range.src.right >= key_range.right:
        return overlap, []

    # partial overlap, r1 extends to the right of r2
    if map_range.src.left <= key_range.left and map_range.src.right >= key_range.left:
        rightover = Range(map_range.src.right + 1, key_range.right)
        return overlap, [rightover]

    # partial overlap, r1 extends to the left of r2
    if map_range.src.right >= key_range.right and map_range.src.left <= key_range.right:
        leftover = Range(key_range.left, map_range.src.left - 1)
        return overlap, [leftover]

    # complete overlap, r2 is inside r1
    if map_range.src.left >= key_range.left and map_range.src.right <= key_range.right:
        rightover = Range(map_range.src.right + 1, key_range.right)
        leftover = Range(key_range.left, map_range.src.left - 1)
        return overlap, [leftover, rightover]

    assert False, "Unreachable"


def src_to_dst(r: Range, mr: MapRange) -> Range:
    assert r.left >= mr.src.left and r.right <= mr.src.right, "Range not in MapRange!"
    offset_left = r.left - mr.src.left
    offset_right = mr.src.right - r.right
    dst_range = Range(mr.dst.left + offset_left, mr.dst.right - offset_right)
    # print("        src->dst:", r, dst_range, n)
    return dst_range


def find_best_seed_location(data: str) -> int:
    seeds, *maps = data.split("\n\n")
    seed_ranges = read_seed_ranges(seeds)
    # print("Seed Ranges (start, len):", seed_ranges)

    # go over maps
    for _map in maps:
        title, *lines = _map.split("\n")
        map_ranges = list(map(read_map_range, lines))
        # print("\nApplying", title)

        # go over items to be mapped
        next_seed_ranges = []
        for _seed_range in seed_ranges:
            queue = deque([_seed_range])
            while queue:
                seed_range = queue.pop()
                # print("Curr Seed", seed_range)

                mapped = False
                # go over ranges in map
                for map_range in map_ranges:
                    # print("  ", map_range)

                    overlap, rest = get_overlap(seed_range, map_range)
                    if overlap is None:
                        # print("      No Overlap")
                        continue

                    mapped = True
                    # print("      Overlap:", overlap, "   Rest:", rest)
                    next_seed_ranges.append(src_to_dst(overlap, map_range))
                    queue.extend(rest)

                if not mapped:
                    next_seed_ranges.append(seed_range)

        # set input for next map
        # print("SRC:", seed_ranges)
        # print("DST:", next_seed_ranges)
        seed_ranges = next_seed_ranges

    loc_ranges = seed_ranges
    return min(loc_range.left for loc_range in loc_ranges)


def write_result(result: int) -> None:
    with open("result_B.txt", "w") as f:
        f.write(str(result))


def main():
    best_loc_example: int = find_best_seed_location(data=load_example())
    assert best_loc_example == 46, "Failed example_input_B!"
    print("Succeeded example_input_B!\n")

    best_loc: int = find_best_seed_location(data=load_input())
    print("Best seed location:", best_loc)
    write_result(best_loc)


if __name__ == "__main__":
    main()

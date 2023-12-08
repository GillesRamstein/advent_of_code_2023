from collections import defaultdict
from functools import reduce
from pathlib import Path
import math


def load_input() -> list[str]:
    with open(Path(__file__).with_name("input.txt")) as f:
        return f.read().split("\n\n")


def create_node_map(nodes: str) -> dict[str, dict[str, str]]:
    node_map = dict()
    for node in nodes.split("\n"):
        if not node:
            continue

        key = node[:3]
        left = node[7:10]
        right = node[12:15]
        # print(node, key, left, right)
        node_map[key] = {"L": left, "R": right}
    assert len(node_map) == len(nodes.split("\n")) - 1
    return node_map


def cnt_divs_to_1(num: int, n: int) -> int:
    nth = 0
    while num > 1:
        num //= n
        nth += 1
    return nth


def prime_factor_decomp(number: int) -> dict[int, int]:
    decomp: dict[int, int] = defaultdict(int)
    while number % 2 == 0:
        number = number // 2
        decomp[2] += 1

    for i in range(3, int(math.sqrt(number) + 1), 2):
        while number % i == 0:
            number = number // i
            decomp[i] += 1

    if number > 2:
        decomp[number] += 1

    return dict(sorted(decomp.items()))


def lmc(numbers: list[int]) -> int:
    prime_factors: dict[int, int] = defaultdict(int)
    for num in numbers:
        for pf, n in prime_factor_decomp(num).items():
            prime_factors[pf] = max(prime_factors[pf], n)
    lmc: int = reduce(lambda a, b: a * b, [pf**n for pf, n in prime_factors.items()])
    return lmc


def count_steps(instructions: str, nodes_input: str) -> int:
    node_map: dict[str, dict[str, str]] = create_node_map(nodes_input)
    nodes: list[str] = [n for n in node_map if n.endswith("A")]
    print("Starting nodes:", nodes)

    # determine loop lengths of each starting value
    loop_lengths: list[int] = []
    for node in nodes:
        n_steps: int = 0
        _break = False
        while not _break:
            for instr in instructions:
                if node.endswith("Z"):
                    loop_lengths.append(n_steps)
                    _break = True
                    break
                node = node_map[node][instr]
                n_steps += 1

    print("Loop lengths:", loop_lengths)
    least_common_multiple = lmc(loop_lengths)
    return least_common_multiple


def write_result(result: int) -> None:
    with open(Path(__file__).with_name("result_B.txt"), "w") as f:
        f.write(str(result))


def main():
    n_steps: int = count_steps(*load_input())
    print(n_steps)
    write_result(n_steps)


if __name__ == "__main__":
    main()

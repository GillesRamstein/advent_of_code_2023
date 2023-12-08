from pathlib import Path


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


def count_steps(instructions: str, nodes: str) -> int:
    n_steps = 0
    node_map = create_node_map(nodes)
    node = "AAA"
    n_iters = 0
    while True:
        print("Iteration:", n_iters)
        for instr in instructions:
            if node == "ZZZ":
                print(node)
                return n_steps
            print(instr, node, node_map[node], node_map[node][instr])
            node = node_map[node][instr]
            n_steps += 1
        n_iters += 1

    assert False, "Unreachable, Bad Input"


def write_result(result: int) -> None:
    with open(Path(__file__).with_name("result_A.txt"), "w") as f:
        f.write(str(result))


def main():
    n_steps: int = count_steps(*load_input())
    print(n_steps)
    write_result(n_steps)


if __name__ == "__main__":
    main()

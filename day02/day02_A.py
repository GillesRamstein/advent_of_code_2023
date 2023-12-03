def main() -> int:
    MAX: dict[str, int] = {"red": 12, "green": 13, "blue": 14}

    sum_possible_game_ids: int = 0
    with open("input.txt") as f:
        for line in f.readlines():
            game_title, game_sets = line.strip("\n").split(":")
            game_is_possible: bool = True
            for game_set in game_sets.split(";"):
                for cubes in game_set.split(","):
                    cube_num, cube_col = cubes.strip(" ").split(" ")
                    if int(cube_num) > MAX[cube_col]:
                        game_is_possible = False
                        break
                if not game_is_possible:
                    break

            if not game_is_possible:
                continue
            sum_possible_game_ids += int(game_title.split(" ")[-1])

    return sum_possible_game_ids


if __name__ == "__main__":
    result: int = main()
    with open("result_B.txt", "w") as f:
        f.write(str(result))
    print("Summed IDs of possible games:", result)

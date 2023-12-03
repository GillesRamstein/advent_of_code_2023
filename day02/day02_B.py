def main() -> int:
    sum_of_powers = 0
    with open("input.txt") as f:
        for line in f.readlines():
            min_cube_nums: dict[str, int] = {"red": 0, "green": 0, "blue": 0}
            game_title, game_sets = line.strip("\n").split(":")
            for game_set in game_sets.split(";"):
                for cubes in game_set.split(","):
                    cube_num, cube_col = cubes.strip(" ").split(" ")
                    min_cube_nums[cube_col] = max(
                        min_cube_nums[cube_col], int(cube_num)
                    )
            sum_of_powers += (
                min_cube_nums["red"] * min_cube_nums["green"] * min_cube_nums["blue"]
            )

    return sum_of_powers


if __name__ == "__main__":
    result: int = main()
    with open("result_A.txt", "w") as f:
        f.write(str(result))
    print("Summed powers of minimum sets:", result)

from typing import List


def get_puzzle_input() -> List[str]:
    res = []
    with open("puzzle-input-day7.txt") as f:
        for line in f.readlines():
            res.append(line.strip())
    return res


def main() -> None:
    # raw_input = """.......S.......
    # ...............
    # .......^.......
    # ...............
    # ......^.^......
    # ...............
    # .....^.^.^.....
    # ...............
    # ....^.^...^....
    # ...............
    # ...^.^...^.^...
    # ...............
    # ..^...^.....^..
    # ...............
    # .^.^.^.^.^...^.
    # ..............."""
    # lines = [line.strip() for line in raw_input.split("\n")]

    lines = get_puzzle_input()
    beams = ["_"] * len(lines[0])
    path_count: List[int] = [0] * len(lines[0])

    for line in lines:
        for i in range(len(line)):
            char = line[i]

            if char == "S":
                beams[i] = "|"
                path_count[i] = 1
                continue

            if char == ".":
                continue

            if char == "^":
                if beams[i] != "|":
                    continue

                if i - 1 >= 0:
                    beams[i - 1] = "|"
                    path_count[i - 1] = path_count[i - 1] + path_count[i]

                if i + 1 < len(line):
                    beams[i + 1] = "|"
                    path_count[i + 1] = path_count[i + 1] + path_count[i]

                beams[i] = "_"
                path_count[i] = 0

    print(beams)
    print(path_count)
    print(sum(path_count))

from typing import List


def get_puzzle_input() -> List[str]:
    res = []
    with open("puzzle-input-day7.txt") as f:
        for line in f.readlines():
            res.append(line.strip())
    return res


def main() -> None:
    #     raw_input = """.......S.......
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
    count = 0

    for line in lines:
        for i in range(len(line)):
            char = line[i]

            if char == "S":
                beams[i] = "|"
                continue

            if char == ".":
                continue

            if char == "^":
                if beams[i] != "|":
                    continue

                if i - 1 >= 0:
                    beams[i - 1] = "|"

                if i + 1 < len(line):
                    beams[i + 1] = "|"

                count += 1
                beams[i] = "_"

    print(beams)
    print(count)

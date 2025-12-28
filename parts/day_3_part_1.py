"""

12345 (bank with 5 batteries)
->
turn on 2 and 4
->
jolts = 24

Cannot be 42

"""

from typing import List


def get_puzzle_input() -> List[str]:
    res: List[str] = []
    with open("puzzle-input-day3.txt") as f:
        for line in f.readlines():
            res.append(line.strip())
    return res


def main() -> None:
    res: List[int] = []
    banks = get_puzzle_input()

    for bank in banks:
        first_max = ""
        second_max = ""
        count = 0

        for battery in bank:
            count += 1

            if first_max == "":
                first_max = battery
                continue

            if (battery > first_max) and (count < len(bank)):
                first_max, second_max = battery, ""
                continue

            if second_max == "":
                second_max = battery
                continue

            if battery > second_max:
                second_max = battery

        res.append(int("".join([first_max, second_max])))

    print(sum(res))  # 17109

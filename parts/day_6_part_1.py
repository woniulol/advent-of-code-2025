from typing import List
import re


def get_puzzle_input() -> List[str]:
    res: List[str] = []
    with open("puzzle-input-day6.txt") as f:
        for line in f.readlines():
            res.append(line.strip())
    return res


def main() -> None:
    #     raw_input = """123 328  51 64
    #  45 64  387 23
    #   6 98  215 314
    # *   +   *   +  """
    # raw_input = [line.strip() for line in raw_input.split("\n")]

    raw_input = get_puzzle_input()

    for i in range(len(raw_input)):
        raw_input[i] = re.sub(" +", " ", raw_input[i]).split(" ")

    res = []

    for column_index in range(len(raw_input[0])):
        nums = []
        operator = raw_input[-1][column_index]
        for row_index in range(len(raw_input) - 1):
            nums.append(raw_input[row_index][column_index])
        res.append(eval(operator.join(nums)))

    print(sum(res))

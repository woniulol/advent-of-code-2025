from turtle import st
from typing import Tuple, List


def get_puzzle_input() -> List[Tuple[int, int]]:
    fresh_ingredient_ids: List[Tuple[int, int]] = []

    with open("puzzle-input-day5.txt") as f:
        for line in f.readlines():
            string = line.strip()
            if string == "":
                break

            fresh_ingredient_ids.append(
                tuple([int(s) for s in string.split("-") if s != ""])
            )
            continue

    return sorted(fresh_ingredient_ids)


def main() -> None:
    # hmmm..., well, the naive way is range(i,j), append all in between and drop duplicates...
    # Let's use a not that naive way.

    fresh_ingredient_ids = get_puzzle_input()

    # Can be equal but will never be grater than the second value.
    # for i in fresh_ingredient_ids:
    #     if i[0] >= i[1]:
    #         print(i)

    max_id = 0  # This number has been counted
    res = 0

    for i in range(len(fresh_ingredient_ids)):
        start = fresh_ingredient_ids[i][0]
        end = fresh_ingredient_ids[i][1]

        if max_id >= end:
            i += 1
            continue

        if max_id < start:
            res += end - start + 1
            max_id = end
            i += 1
            continue

        if max_id == start:
            res += end - start
            max_id = end
            i += 1
            continue

        res += end - max_id
        max_id = end
        i += 1

    print(res)

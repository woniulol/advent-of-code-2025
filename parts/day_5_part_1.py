from typing import Tuple, List

"""
fresh or spoiled
"""

raw_fresh_id_ranges = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

"""
Inclusive

Overlapping
"""


def get_puzzle_input() -> Tuple[List, List]:
    fresh_ingredient_ids: List[Tuple[int]] = []
    avaliable_ingredient_ids: List[int] = []

    is_fresh_ingredient_ids = True

    # for string in raw_fresh_id_ranges.split("\n"):
    with open("puzzle-input-day5.txt") as f:
        for line in f.readlines():
            string = line.strip()
            if string == "":
                is_fresh_ingredient_ids = False
                continue

            if is_fresh_ingredient_ids:
                fresh_ingredient_ids.append(
                    tuple([int(s) for s in string.split("-") if s != ""])
                )
                continue

            avaliable_ingredient_ids.append(int(string))

    return sorted(fresh_ingredient_ids), sorted(avaliable_ingredient_ids)


def main() -> None:
    fresh_ingredient_ids, avaliable_ingredient_ids = get_puzzle_input()
    res = []

    for i in range(len(avaliable_ingredient_ids)):
        avaliable_ingredient = avaliable_ingredient_ids[i]

        for j in range(len(fresh_ingredient_ids)):
            if avaliable_ingredient_ids[i] < fresh_ingredient_ids[j][0]:
                continue

            if avaliable_ingredient_ids[i] > fresh_ingredient_ids[j][1]:
                continue

            res.append(avaliable_ingredient)

    res = list(set(res))
    print(len(res))

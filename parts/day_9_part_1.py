from curses import raw
from typing import Tuple, List


def get_straight_line_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** (1 / 2)


def get_area(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    x = abs(p2[0] - p1[0]) + 1
    y = abs(p2[1] - p1[1]) + 1
    return x * y


def get_puzzle_input() -> List[str]:
    res = []
    with open("puzzle-input-day9.txt") as f:
        for line in f.readlines():
            res.append(line.strip())
    return res


def main() -> None:
    # raw_input = """7,1
    # 11,1
    # 11,7
    # 9,7
    # 9,5
    # 2,5
    # 2,3
    # 7,3"""
    # lines = [line.split(",") for line in raw_input.split("\n")]

    raw_input = get_puzzle_input()
    lines = [line.split(",") for line in raw_input]

    pointes = [(int(line[0]), int(line[1])) for line in lines]
    full_distance: List[Tuple[Tuple[int, int], Tuple[int, int], int]] = []
    for i in range(len(pointes)):
        for j in range(i + 1, len(pointes)):
            full_distance.append(
                (
                    pointes[i],
                    pointes[j],
                    get_straight_line_distance(pointes[i], pointes[j]),
                )
            )

    # full_distance = sorted(full_distance, key=lambda x: x[2], reverse=True)
    full_distance = sorted(
        full_distance, key=lambda item: get_area(item[0], item[1]), reverse=True
    )

    print(full_distance[0])
    print(get_area(full_distance[0][0], full_distance[0][1]))
    return

from typing import List


def get_puzzle_input() -> List[str]:
    with open("puzzle-input-day2.txt") as f:
        return f.readline().split(",")


def main() -> None:
    res: List[int] = []
    inputs = get_puzzle_input()
    for item in inputs:
        start, end = tuple(int(s) for s in item.split("-"))
        for i in range(start, end + 1):
            s = str(i)
            if len(s) % 2 != 0:
                continue

            mid = int(len(s) / 2)
            print(mid)
            if s[0:mid] == s[mid:]:
                res.append(i)

    print(res)
    print(sum(res))

    # 16793817782

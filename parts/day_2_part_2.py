from typing import List


def get_puzzle_input() -> List[str]:
    with open("puzzle-input-day2.txt") as f:
        return f.readline().split(",")


def main() -> None:
    res: List[int] = []
    inputs = get_puzzle_input()

    # inputs = [
    #     "11-22",
    #     "95-115",
    #     "998-1012",
    #     "1188511880-1188511890",
    #     "222220-222224",
    #     "1698522-1698528",
    #     "446443-446449",
    #     "38593856-38593862",
    #     "565653-565659",
    #     "824824821-824824827",
    #     "2121212118-2121212124",
    # ]

    for item in inputs:
        start, end = tuple(int(s) for s in item.split("-"))
        for i in range(start, end + 1):
            s = str(i)
            for j in range(int(len(s) // 2) + 1):
                check_split = s[0 : j + 1]
                split_res = s.split(check_split)
                if split_res.count("") == len(split_res) and len(split_res) > 2:
                    res.append(i)

    res = list(set(res))
    print(sum(res))

    # 16793817782

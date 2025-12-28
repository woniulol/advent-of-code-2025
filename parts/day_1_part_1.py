from typing import Self

# L -> -
# R -> +

# 50 + L68 = 50 - 68 = -18 -> 100 - 18 = 82
# 0 + L1 = 0 - 1 = -1 -> 100 - 1 = 99


class Rotation:
    def __init__(self, sign: str, num: int) -> None:
        self.sign: str = sign
        self.num: int = num

    @classmethod
    def from_str(cls, str_: str) -> Self:
        return cls(str_[0], int(str_[1:]))

    def debug_print(self) -> None:
        print(f"{self.sign}, {self.num}")

    def add_int(self, other: int) -> int:
        multiplier = 1
        if self.sign == "L":
            multiplier = -1

        num = (multiplier * self.num) + other
        num = abs(num % 100)

        return num


def get_puzzle_input() -> list[Rotation]:
    res = []
    with open("puzzle-input-day1.txt") as f:
        for line in f:
            line = line.strip()
            if line:
                res.append(Rotation.from_str(line))
    return res


def main() -> None:
    node_list = get_puzzle_input()

    password = 0
    res = 50
    for node in node_list:
        res = node.add_int(res)
        if res == 0:
            password += 1

    print(password)


if __name__ == "__main__":
    main()

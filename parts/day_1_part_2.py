from parts.day_1_part_1 import Rotation


class MoreRotation(Rotation):
    def add_int(self, p0: int) -> tuple[int, int]:
        multiplier = 1
        if self.sign == "L":
            multiplier = -1

        num = (multiplier * self.num) + p0
        count_zero = abs(num // 100)
        num = abs(num % 100)

        return num, count_zero


def get_puzzle_input() -> list[MoreRotation]:
    res = []
    with open("puzzle-input.txt") as f:
        for line in f:
            line = line.strip()
            if line:
                res.append(MoreRotation.from_str(line))
    return res


def main() -> None:
    node_list = get_puzzle_input()
    password = 0
    res = 50
    for node in node_list:
        res, zero_count = node.add_int(res)
        if res == 0:
            password += 1
            zero_count -= 1
        password += zero_count

    print(password)

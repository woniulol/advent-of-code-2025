from typing import List


def get_puzzle_input() -> List[str]:
    res: List[str] = []
    with open("puzzle-input-day6.txt") as f:
        for line in f.readlines():
            res.append(line.strip("\n"))
    return res


def main() -> None:
    #     raw_input = """123 328  51 64
    #  45 64  387 23
    #   6 98  215 314
    # *   +   *   +  """
    # lines = []
    # for line in raw_input.split("\n"):
    #     lines.append(line)

    lines = get_puzzle_input()

    row_len = len(lines)
    col_len = len(lines[0])
    res: List[int] = []

    chars: List[str] = []
    nums: List[str] = []
    operator: str = ""

    for i in range(col_len - 1, -1, -1):
        for j in range(row_len):
            char = lines[j][i]
            print(char)

            if j + 1 == row_len:
                if char != " ":
                    operator = char
                    nums.append("".join(chars).strip(" "))
                    print(nums)
                    res.append(eval(operator.join(nums)))

                    chars: List[str] = []
                    nums: List[int] = []
                    operator: str = ""

                    continue

                if len(chars) == 0:
                    continue

                print(chars)
                nums.append("".join(chars).strip(" "))
                chars: List[str] = []

            if char == " ":
                continue

            chars.append(char)

    print(res)
    print(sum(res))

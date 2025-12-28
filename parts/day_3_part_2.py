from typing import List


def get_puzzle_input() -> List[str]:
    res = []
    with open("puzzle-input-day3.txt") as f:
        for line in f.readlines():
            res.append(line.strip())
    return res


def main() -> None:
    banks = get_puzzle_input()
    battery_num = 12
    results = []
    cur_joltage_index = [-1] * battery_num

    for bank in banks:
        i = 0
        while i < len(bank):
            # print("iii", i)
            if i == 0:
                cur_joltage_index = list(range(battery_num))
                i += 1
                continue

            j = 0
            while j < battery_num:
                if (
                    (bank[i] > bank[cur_joltage_index[j]])
                    and (len(bank) - i >= battery_num - j)
                    and (i > cur_joltage_index[j])
                ):
                    cur_joltage_index = cur_joltage_index[0:j] + list(
                        range(i, i + battery_num - j)
                    )
                    break

                j += 1

            i += 1

        res = ""
        for i in cur_joltage_index:
            res += bank[i]

        results.append(int(res))

    print(sum(results))

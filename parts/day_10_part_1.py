from itertools import combinations
from typing import List, Tuple


def get_puzzle_input() -> Tuple[
    List[List[int]],  # expected status
    List[List[Tuple[int, ...]]],  # available keys
]:
    expected_status_lines: List[List[int]] = []
    available_keys_lines: List[List[Tuple[int, ...]]] = []

    with open("puzzle-input-day10.txt") as f:
        for line in f.readlines():
            line = line.strip(" ").split(" ")
            avaliable_keys = []

            for i in range(len(line)):
                if i == 0:
                    expected_status = [
                        0 if c == "." else 1 for c in line[i].strip("[").strip("]")
                    ]
                    expected_status_lines.append(expected_status)
                    continue

                if i != len(line) - 1:
                    avaliable_keys.append(
                        tuple(int(i) for i in line[i].strip("(").strip(")").split(","))
                    )

                if i == len(line) - 1:
                    available_keys_lines.append(avaliable_keys)

    assert len(expected_status_lines) == len(available_keys_lines)

    return expected_status_lines, available_keys_lines


def main() -> None:
    """
    [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}

    Light diagram - wiring schematics - joltage requirements

    . -> off
    # -> on

    [...#.] -> expected result
    All lights are initially off.

    (2,3) -> switch the light on index 2 and 3

    Ignore the {} joltage for the first part.
    """

    # !!! Even though you can but YOU WILL NEVER PRESS THE SAME BUTTON TWICE because it will
    # offset each other leaving no effect and only increasing the count number.

    expected_status_lines, available_keys_lines = get_puzzle_input()

    all_min_press_count: List[int] = []

    for i in range(len(expected_status_lines)):
        expected_status = expected_status_lines[i]
        available_keys = available_keys_lines[i]

        min_press_count = len(available_keys)

        avaliable_key_combinations: List[Tuple[Tuple[int, ...]]] = []
        for r in range(1, len(available_keys) + 1):
            avaliable_key_combinations.extend(combinations(available_keys, r))

        for combination in avaliable_key_combinations:
            init_status = [0] * len(expected_status)
            for key in combination:
                for press in key:
                    init_status[press] = init_status[press] + 1
            final_status = list(map(lambda x: x % 2, init_status))
            if expected_status == final_status:
                if len(combination) < min_press_count:
                    min_press_count = len(combination)

        all_min_press_count.append(min_press_count)

    print(all_min_press_count)
    print(sum(all_min_press_count))

from typing import List, Tuple, Dict


def get_puzzle_input() -> Dict[str, List[str]]:
    node_map: Dict[str, List[str]] = {}
    with open("puzzle-input-day11.txt") as f:
        for line in f.readlines():
            line = line.strip().split(":")
            node_map[line[0]] = line[-1].strip().split(" ")

    return node_map


count_path_cache: Dict[Tuple[str, str], int] = {}
node_map = get_puzzle_input()


def count_path(
    start: str,
    end: str,
) -> int:
    global count_path_cache
    global node_map

    if (start, end) in count_path_cache:
        return count_path_cache[(start, end)]

    if start == end:
        return 1

    if start == "out":
        return 0

    res = 0
    for node in node_map[start]:
        res += count_path(
            start=node,
            end=end,
        )
        count_path_cache[(start, end)] = res

    return res


def main() -> None:
    res = count_path("svr", "dac") * count_path("dac", "fft") * count_path("fft", "out")
    print(res)
    res = count_path("svr", "fft") * count_path("fft", "dac") * count_path("dac", "out")
    print(res)

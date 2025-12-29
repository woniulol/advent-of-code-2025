from typing import List, Tuple, Optional

"""
If there are fewer than four rolls of paper in the eight adjacent positions.

Adjacent means surrounding the positions.
"""


def get_puzzle_input() -> List[str]:
    res = []
    with open("puzzle-input-day4.txt") as f:
        for line in f.readlines():
            res.append(line.strip())
    return res


def get_relative_positions(
    x: int, y: int, xi_bound: int, yi_bound: int
) -> List[Optional[Tuple[int, int]]]:
    res = [
        (x - 1, y - 1),
        (x - 1, y),
        (x - 1, y + 1),
        (x, y - 1),
        (x, y + 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
    ]

    def _is_outbound(position: Tuple[int, int]) -> bool:
        return any(
            (
                position[0] < 0,
                position[0] > xi_bound,
                position[1] < 0,
                position[1] > yi_bound,
            )
        )

    return [position if not _is_outbound(position) else None for position in res]


def main() -> None:

    paper_grids = get_puzzle_input()
    init_res = -1
    res = 0

    while init_res != res:
        init_res = res
        position_to_clear: List[Tuple[int, int]] = []

        for y in range(len(paper_grids)):
            for x in range(len(paper_grids[0])):
                if paper_grids[y][x] != "@":
                    continue

                relative_positions = get_relative_positions(
                    x, y, len(paper_grids[0]) - 1, len(paper_grids) - 1
                )

                position_counter = 0
                for position in relative_positions:
                    if position is None:
                        continue
                    if paper_grids[position[1]][position[0]] == "@":
                        position_counter += 1

                if position_counter < 4:
                    res += 1
                    position_to_clear.append((x, y))

        for position in position_to_clear:
            arr = list(paper_grids[position[1]])
            arr[position[0]] = "."
            paper_grids[position[1]] = "".join(arr)

    print(res)

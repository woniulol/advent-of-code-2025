from typing import List, Tuple


def get_puzzle_input() -> Tuple[List[int], List[int], List[List[int]]]:
    shape_sizes: List[int] = []
    areas: List[int] = []
    shape_count: List[List[int]] = []

    with open("puzzle-input-day12.txt") as f:
        in_shape = False
        shape_size = 0

        for line in f.readlines():
            line = line.strip()

            if len(line) == 2:
                in_shape = True
                shape_size = 0
                continue

            if in_shape:
                if "#" in line:
                    for c in line:
                        if c == "#":
                            shape_size += 1
                else:
                    shape_sizes.append(shape_size)
                    in_shape = False
                    shape_size = 0

            if "x" in line:
                area, counts = line.split(":")
                areas.append(eval(area.replace("x", "*")))
                shape_count.append([int(i) for i in counts.split(" ") if i != ""])

    return shape_sizes, areas, shape_count


def main() -> None:
    shape_sizes, areas, shape_count = get_puzzle_input()

    assert len(areas) == len(shape_count)

    # DAMN, it just works.
    res = 0
    for i in range(len(areas)):
        total_taken_areas = 0
        for j in range(len(shape_count[i])):
            total_taken_areas += shape_sizes[j] * shape_count[i][j]
        if total_taken_areas <= areas[i]:
            res += 1

    print(res)

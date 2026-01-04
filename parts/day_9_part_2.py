from typing import List, Tuple, Optional

type Diagonal = Tuple[Tuple[int, int], Tuple[int, int]]


def get_puzzle_input() -> List[str]:
    res = []
    with open("puzzle-input-day9.txt") as f:
        for line in f.readlines():
            res.append(line.strip())
    return res


def get_area(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    x = abs(p2[0] - p1[0]) + 1
    y = abs(p2[1] - p1[1]) + 1
    return x * y


def is_valide_diagnoal(diagonal: Diagonal, edges: List[Diagonal]) -> bool:
    # Edges will always have the same x or the same y, meaning it can only be
    # horizontal or vertical.

    # Vertical diagonal
    if diagonal[1][0] == diagonal[0][0]:
        for (edge_start_x, edge_start_y), (edge_end_x, edge_end_y) in edges:
            # vertical edges
            if edge_start_x == edge_end_x:
                continue

            # horizontal edges
            if edge_start_y == edge_end_y:
                if (
                    edge_start_y > min(diagonal[0][1], diagonal[1][1])
                    and edge_start_y < max(diagonal[0][1], diagonal[1][1])
                ) and (
                    diagonal[0][0] > min(edge_start_x, edge_end_x)
                    and diagonal[0][0] < max(edge_start_x, edge_end_x)
                ):
                    return False

                continue

            print((edge_start_x, edge_start_y), (edge_end_x, edge_end_y))
            raise Exception("Unexpected edges.")

        return True

    # Other diagonal
    a = (diagonal[1][1] - diagonal[0][1]) / (diagonal[1][0] - diagonal[0][0])
    b = diagonal[1][1] - a * diagonal[1][0]

    for (edge_start_x, edge_start_y), (edge_end_x, edge_end_y) in edges:
        # vertical edges
        if edge_start_x == edge_end_x:
            if edge_start_x > min(
                diagonal[0][0], diagonal[1][0]
            ) and edge_start_x < max(diagonal[0][0], diagonal[1][0]):
                hitting_y = a * edge_start_x + b
                if hitting_y >= min(edge_start_y, edge_end_y) and hitting_y <= max(
                    edge_start_y, edge_end_y
                ):
                    return False
            continue

        # horizontal edges
        if edge_start_y == edge_end_y:
            if edge_start_y > min(
                diagonal[0][1], diagonal[1][1]
            ) and edge_start_y < max(diagonal[0][1], diagonal[1][1]):
                if a != 0:
                    hitting_x = (edge_start_y - b) / a
                    if hitting_x >= min(edge_start_x, edge_end_x) and hitting_x <= max(
                        edge_start_x, edge_end_x
                    ):
                        return False
                    continue
            continue

        print((edge_start_x, edge_start_y), (edge_end_x, edge_end_y))
        raise Exception("Unexpected edges.")

    return True


def get_mirrored_dignoal(diagonal: Diagonal) -> Diagonal:
    return (
        (diagonal[0][0], diagonal[1][1]),
        (diagonal[1][0], diagonal[0][1]),
    )


def main() -> None:
    raw_input = get_puzzle_input()
    lines = [line.split(",") for line in raw_input]
    points = [(int(line[0]), int(line[1])) for line in lines]
    edges: List[Diagonal] = []

    max_diagonal: Optional[Diagonal] = None

    for i in range(len(points)):
        if i == len(points) - 1:
            edges.append((points[i], points[0]))  # ty:ignore[invalid-argument-type]
            continue
        edges.append((points[i], points[i + 1]))  # ty:ignore[invalid-argument-type]

    for i in range(len(points)):
        if i == len(points) - 1:
            continue
        for j in range(i + 1, len(points)):
            diagonal = (points[i], points[j])
            if is_valide_diagnoal(get_mirrored_dignoal(diagonal), edges):
                if max_diagonal is None:
                    max_diagonal = diagonal
                else:
                    if get_area(*max_diagonal) < get_area(*diagonal):
                        max_diagonal = diagonal

    print(max_diagonal)
    print(get_area(*max_diagonal))  # 1654141440

    return

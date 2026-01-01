from typing import Self, List, Dict, Tuple, Set


class Junction:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

        self._hash = int("".join([str(self.x), str(self.y), str(self.z)]))

    @classmethod
    def from_line(cls, line: str) -> Self:
        pos = [int(s) for s in line.strip().split(",")]
        return cls(pos[0], pos[1], pos[2])

    def __hash__(self) -> int:
        return self._hash

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} ( {self.x, self.y, self.z} )"


def get_straight_line_distance(j1: Junction, j2: Junction) -> int:
    return ((j1.x - j2.x) ** 2 + (j1.y - j2.y) ** 2 + (j1.z - j2.z) ** 2) ** (1 / 2)


def get_puzzle_input() -> List[str]:
    res = []
    with open("puzzle-input-day8.txt") as f:
        for line in f.readlines():
            res.append(line.strip())
    return res


def main() -> None:
    #     raw_input = """162,817,812
    # 57,618,57
    # 906,360,560
    # 592,479,940
    # 352,342,300
    # 466,668,158
    # 542,29,236
    # 431,825,988
    # 739,650,466
    # 52,470,668
    # 216,146,977
    # 819,987,18
    # 117,168,530
    # 805,96,715
    # 346,949,466
    # 970,615,88
    # 941,993,340
    # 862,61,35
    # 984,92,344
    # 425,690,689"""
    #     lines = raw_input.split("\n")

    lines = get_puzzle_input()
    junctions = [Junction.from_line(line) for line in lines]
    circuits: List[Set[Junction]] = []

    full_distance: List[Tuple[Junction, Junction, int]] = []
    for i in range(len(junctions)):
        for j in range(i + 1, len(junctions)):
            distance = get_straight_line_distance(junctions[i], junctions[j])
            full_distance.append((junctions[i], junctions[j], distance))

    full_distance = sorted(full_distance, key=lambda x: x[2])

    steps = 0
    for start, end, distance in full_distance:
        steps += 1
        if steps > 1000:
            break

        start_in = -1
        end_in = -1

        for i in range(len(circuits)):
            if start in circuits[i]:
                start_in = i

            if end in circuits[i]:
                end_in = i

        if start_in == -1:
            if end_in == -1:
                circuits.append({start, end})
                continue
            circuits[end_in].add(start)
            continue

        else:
            if end_in == -1:
                circuits[start_in].add(end)
                continue
            else:
                if end_in != start_in:
                    circuits[start_in] = circuits[start_in].union(circuits[end_in])
                    circuits[end_in] = {}

    res = []
    for circuit in sorted(circuits, key=lambda x: len(x), reverse=True)[:3]:
        res.append(len(circuit))

    print(multi := res[0] * res[1] * res[2])

    return

from typing import List, Tuple, Dict, Set


def get_puzzle_input() -> Tuple[List[str], List[List[str]]]:
    parents: List[str] = []
    nodes: List[List[str]] = []
    with open("puzzle-input-day11.txt") as f:
        for line in f.readlines():
            line = line.strip().split(":")
            parents.append(line[0])
            nodes.append(line[-1].strip().split(" "))

    return parents, nodes


def main() -> None:
    parents, nodes = get_puzzle_input()
    assert len(parents) == len(nodes)

    node_cum_count: Dict[str, int] = {}
    nodes_out: Set[str] = set()

    nodes_to_process: List[str] = []

    for i in range(len(parents)):
        if parents[i] == "you":
            for node in nodes[i]:
                if node != "out":
                    node_cum_count[node] = 1
                    nodes_to_process.append(node)

    while nodes_to_process:
        node_to_process = nodes_to_process.pop()
        for i in range(len(parents)):
            if parents[i] == node_to_process:
                for node in nodes[i]:
                    if node == "out":
                        nodes_out.add(node_to_process)
                    node_cum_count[node] = node_cum_count.get(node, 0) + 1
                    nodes_to_process.append(node)
                break

    res = 0
    for node in nodes_out:
        res += node_cum_count[node]

    print(res)

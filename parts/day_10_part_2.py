from typing import List, Tuple
from ortools.linear_solver import pywraplp


def get_puzzle_input() -> Tuple[
    List[List[int]],  # expected status
    List[List[Tuple[int, ...]]],  # available keys
]:
    available_keys_lines: List[List[tuple[int, ...]]] = []
    expected_status_lines: List[List[int]] = []

    with open("puzzle-input-day10.txt") as f:
        for line in f.readlines():
            line = line.strip().split(" ")
            avaliable_keys = []

            for i in range(len(line)):
                if i == 0:
                    continue

                if i != len(line) - 1:
                    avaliable_keys.append(
                        tuple(int(i) for i in line[i].strip("(").strip(")").split(","))
                    )

                if i == len(line) - 1:
                    available_keys_lines.append(avaliable_keys)
                    expected_status_lines.append(
                        list(int(i) for i in line[i].strip("{").strip("}").split(","))
                    )

    return expected_status_lines, available_keys_lines


def main() -> None:
    """
    Solve the equation.
    """

    expected_status_lines, available_keys_lines = get_puzzle_input()
    assert len(expected_status_lines) == len(available_keys_lines)

    len_keys_lines = len(available_keys_lines)
    count = 0

    for i in range(len_keys_lines):
        keys = available_keys_lines[i]
        status = expected_status_lines[i]

        # solver = pywraplp.Solver.CreateSolver("GLOP")
        # "CBC" to ensure int output.
        solver = pywraplp.Solver.CreateSolver("CBC")
        vars = [
            solver.IntVar(0, max(status) + 1, chr(i)) for i in range(97, 97 + len(keys))
        ]

        for j in range(len(status)):
            vars_index = []
            for k in range(len(keys)):
                if j in keys[k]:
                    vars_index.append(k)

            res = 0
            for var_i in vars_index:
                res = res + vars[var_i]

            solver.Add(res == status[j])

        solver.Minimize(sum(vars))

        res = solver.Solve()

        if res == pywraplp.Solver.OPTIMAL:
            count += solver.Objective().Value()
        else:
            print("No optimal solution found.")

    print(count)

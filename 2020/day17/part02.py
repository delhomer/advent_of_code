"""Advent of code 2020, day17, part02
"""

from itertools import product


NEIGHBOURS = [
    (i, j, k, l)
    for i, j, k, l in product(range(-1, 2), repeat=4)
    if (i, j, k, l) != (0, 0, 0, 0)
]


def read_input(filepath):
    with open(filepath, "r") as fobj:
        return [[[list(line.strip()) for line in fobj.readlines()]]]


def extend_scope(grid):
    for x in grid:
        for y in x:
            for z in y:
                z.insert(0, ".")
                z.append(".")
            y.insert(0, ["."] * (len(y) + 2))
            y.append(["."] * (len(y) + 1))
        x.insert(0, [["."] * len(grid[0][0][0])] * len(grid[0][0]))
        x.append([["."] * len(grid[0][0][0])] * len(grid[0][0]))
    grid.insert(0, [[["."] * len(grid[0][0][0])] * len(grid[0][0])] * len(grid[0]))
    grid.append([[["."] * len(grid[0][0][0])] * len(grid[0][0])] * len(grid[0]))
    return grid


def nb_neighbours(configuration, x, y, z, k):
    return sum(
        0 <= x+xx <= len(configuration) - 1
        and 0 <= y+yy <= len(configuration[0]) - 1
        and 0 <= z+zz <= len(configuration[0][0]) - 1
        and 0 <= k+kk <= len(configuration[0][0][0]) - 1
        and configuration[x+xx][y+yy][z+zz][k+kk] == "#"
        for xx, yy, zz, kk in NEIGHBOURS
    )


def run_cycle(configuration):
    configuration = extend_scope(configuration)
    out_configuration = []
    for x in range(len(configuration)):
        new_y = []
        for y in range(len(configuration[x])):
            new_z = []
            for z in range(len(configuration[x][y])):
                new_k = []
                for k in range(len(configuration[x][y][z])):
                    if configuration[x][y][z][k] == "." and nb_neighbours(configuration, x, y, z, k) == 3:
                        new_k.append("#")
                    elif configuration[x][y][z][k] == "#" and not (2 <= nb_neighbours(configuration, x, y, z, k) <= 3):
                        new_k.append(".")
                    else:
                        new_k.append(configuration[x][y][z][k])
                new_z.append(new_k)
            new_y.append(new_z)
        out_configuration.append(new_y)
    return out_configuration


def count_active_cubes(configuration):
    return sum(
        sum(
            sum(
                sum(1 for k in z if k == "#") for z in y
            ) for y in x
        )
        for x in configuration
    )


def initialization(configuration):
    for counter in range(6):
        configuration = run_cycle(configuration)
    return count_active_cubes(configuration)


def run(input_str, expected_result=None):
    configuration = read_input(input_str)
    result = initialization(configuration)
    print(
        "Number of active cubes after six cycles{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", 848)
    run("input")

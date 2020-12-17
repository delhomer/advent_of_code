"""Advent of code 2020, day17, part01
"""

NEIGHBOURS = (
    (0, 0, -1),
    (0, 0, 1),
    (0, -1, -1),
    (0, -1, 0),
    (0, -1, 1),
    (0, 1, -1),
    (0, 1, 0),
    (0, 1, 1),
    (-1, -1, -1),
    (-1, -1, 0),
    (-1, -1, 1),
    (-1, 0, -1),
    (-1, 0, 0),
    (-1, 0, 1),
    (-1, 1, -1),
    (-1, 1, 0),
    (-1, 1, 1),
    (1, -1, -1),
    (1, -1, 0),
    (1, -1, 1),
    (1, 0, -1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, -1),
    (1, 1, 0),
    (1, 1, 1),
)


def read_input(filepath):
    with open(filepath, "r") as fobj:
        return [list(line.strip()) for line in fobj.readlines()]


def extend_scope(grid):
    for x in grid:
        for idx, y in enumerate(x):
            y.insert(0, ".")
            y.append(".")
        x.insert(0, ["."] * (len(x) + 2))
        x.append(["."] * (len(x) + 1))
    grid.insert(0, [["."] * len(grid[0])] * len(grid[0]))
    grid.append([["."] * len(grid[0])] * len(grid[0]))
    return grid


def nb_neighbours(configuration, x, y, z):
    return sum(
        0 <= x+xx <= len(configuration) - 1
        and 0 <= y+yy <= len(configuration[0]) - 1
        and 0 <= z+zz <= len(configuration[0][0]) - 1
        and configuration[x+xx][y+yy][z+zz] == "#"
        for xx, yy, zz in NEIGHBOURS
    )


def run_cycle(configuration):
    configuration = extend_scope(configuration)
    out_configuration = []
    for x in range(len(configuration)):
        new_y = []
        for y in range(len(configuration[x])):
            new_z = []
            for z in range(len(configuration[x][y])):
                if configuration[x][y][z] == "." and nb_neighbours(configuration, x, y, z) == 3:
                    new_z.append("#")
                elif not (2 <= nb_neighbours(configuration, x, y, z) <= 3):
                    new_z.append(".")
                else:
                    new_z.append(configuration[x][y][z])
            new_y.append(new_z)
        out_configuration.append(new_y)
    return out_configuration


def count_active_cubes(configuration):
    return sum(
        sum(
            sum(1 for z in y if z == "#") for y in x
        )
        for x in configuration
    )


def initialization(configuration):
    for counter in range(6):
        configuration = run_cycle(configuration)
    return count_active_cubes(configuration)


def run(input_str, expected_result=None):
    configuration = read_input(input_str)
    result = initialization([configuration])
    print(
        "Number of active cubes after six cycles{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", 112)
    run("input")

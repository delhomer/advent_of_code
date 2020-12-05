INPUT_FILEPATH = "2020/day03/input"


def toboggan(lines, right, down):
    tree_counter = 0
    marker = 0
    for line in lines[::down]:
        line = line.strip()
        tree_counter += line[marker % len(line)] == "#"
        marker += right
    print("{} trees encountered for slope ({},{}).".format(tree_counter, right, down))
    return tree_counter


if __name__ == "__main__":

    with open(INPUT_FILEPATH, "r") as fobj:
        lines = fobj.readlines()
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        res = 1
        for right, down in slopes:
            res *= toboggan(lines, right, down)
        print("Final result: {}".format(res))

INPUT_FILEPATH = "2020/day03/input"


if __name__ == "__main__":

    with open(INPUT_FILEPATH, "r") as fobj:
        lines = fobj.readlines()
        tree_counter = 0
        marker = 0
        for line in lines:
            line = line.strip()
            tree_counter += line[marker % len(line)] == "#"
            marker += 3
        print("{} trees encountered.".format(tree_counter))

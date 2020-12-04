INPUT_FILE = "2020/day01/input"


if __name__ == "__main__":

    with open(INPUT_FILE, "r") as fobj:

        lines = fobj.readlines()
        for l1 in lines:
            for l2 in lines:
                if int(l1) + int(l2) == 2020:
                    print(l1, l2)
                    print("l1 * l2 = ", int(l1) * int(l2))
                    break

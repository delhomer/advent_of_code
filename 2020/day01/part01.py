"""Advent of code 2020, day01, part01
"""

if __name__ == "__main__":

    with open("input", "r") as fobj:

        lines = fobj.readlines()
        for l1 in lines:
            for l2 in lines:
                if int(l1) + int(l2) == 2020:
                    print(l1, l2)
                    print("l1 * l2 = ", int(l1) * int(l2))
                    break

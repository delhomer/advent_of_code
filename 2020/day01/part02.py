"""Advent of code 2020, day01, part02
"""

def find_2020_terms(items):
    for l1 in items:
        for l2 in items:
            for l3 in items:
                if int(l1) + int(l2) + int(l3) == 2020:
                    return [l1, l2, l3, int(l1) * int(l2) * int(l3)]
    

if __name__ == "__main__":

    with open("input", "r") as fobj:

        lines = fobj.readlines()
        l1, l2, l3, mult = find_2020_terms(lines)
        print(l1, l2, l3)
        print("l1 * l2 * l3 = ", mult)
        

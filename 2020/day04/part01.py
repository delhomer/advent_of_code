"""Advent of code 2020, day04, part01
"""

REQUIRED_SECTIONS = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")


def read_input():
    with open("input", "r") as fobj:
        return fobj.readlines()


def preprocess_passport(lines):
    return "".join(lines).split("\n\n")


def is_valid(passport):
    passport_dict = {
        x: y for x, y in [item.split(":") for item in passport.split()]
    }
    return all(rs in passport_dict for rs in REQUIRED_SECTIONS)


if __name__ == "__main__":

    lines = read_input()
    passports = preprocess_passport(lines)
    valid_passport_counter = 0
    for passport in passports:
        valid_passport_counter += is_valid(passport)
    print("Number of valid passports: {}".format(valid_passport_counter))

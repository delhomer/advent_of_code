import re


INPUT_FILEPATH = "2020/day04/input"

REQUIRED_SECTIONS = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")


def read_input():
    with open(INPUT_FILEPATH, "r") as fobj:
        return fobj.readlines()


def preprocess_passport(lines):
    return "".join(lines).split("\n\n")


def valid_birth_year(year):
    return 1920 <= year <= 2002


def valid_issue_year(year):
    return 2010 <= year <= 2020


def valid_expiration_year(year):
    return 2020 <= year <= 2030


def valid_height(height):
    if len(height) < 3:
        return False
    if height[-2:] == "in":
        return 59 <= int(height[:-2]) <= 76
    elif height[-2:] == "cm":
        return 150 <= int(height[:-2]) <= 193
    else:
        return False

    
def valid_hair_color(color):
    p = re.compile(r"^#[0-9a-f]{6}$")
    return p.match(color) is not None


def valid_eye_color(color):
    return color in ("amb", "blu", "brn", "gry", "grn" ,"hzl", "oth")


def valid_id(pid):
    p = re.compile(r"^[0-9]{9}$")
    return p.match(pid) is not None


def is_valid(passport):
    passport_dict = {
        x: y for x, y in [item.split(":") for item in passport.split()]
    }
    return (
        all(rs in passport_dict for rs in REQUIRED_SECTIONS)
        and valid_birth_year(int(passport_dict["byr"]))
        and valid_issue_year(int(passport_dict["iyr"]))
        and valid_expiration_year(int(passport_dict["eyr"]))
        and valid_height(passport_dict["hgt"])
        and valid_hair_color(passport_dict["hcl"])
        and valid_eye_color(passport_dict["ecl"])
        and valid_id(passport_dict["pid"])
    )


if __name__ == "__main__":

    lines = read_input()
    passports = preprocess_passport(lines)
    valid_passport_counter = 0
    for passport in passports:
        valid_passport_counter += is_valid(passport)
    print("Number of valid passports: {}".format(valid_passport_counter))

INPUT_FILEPATH = "2020/day02/input"


def is_valid(password, key, min_occurrence, max_occurrence):
    return min_occurrence <= password.count(key) <= max_occurrence


if __name__ == "__main__":

    with open(INPUT_FILEPATH, "r") as fobj:
        lines = fobj.readlines()
        valid_counter = 0
        for line in lines:
            occurrences, key, password = line.split()
            min_occ, max_occ = occurrences.split("-")
            key = key[0]
            valid_counter += is_valid(password, key, int(min_occ), int(max_occ))
        print("{} valid passwords over {}.".format(valid_counter, len(lines)))

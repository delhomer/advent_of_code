INPUT_FILEPATH = "2020/day02/input"


def is_valid(password, key, first_occurrence, last_occurrence):
    assert 1 <= first_occurrence <= len(password)
    assert 1 <= last_occurrence <= len(password)
    return (password[first_occurrence - 1] == key) ^ (password[last_occurrence - 1] == key)


if __name__ == "__main__":

    with open(INPUT_FILEPATH, "r") as fobj:
        lines = fobj.readlines()
        valid_counter = 0
        for line in lines:
            occurrences, key, password = line.split()
            first_occ, last_occ = occurrences.split("-")
            key = key[0]
            valid_counter += is_valid(password, key, int(first_occ), int(last_occ))
        print("{} valid passwords over {}.".format(valid_counter, len(lines)))

INPUT_FILEPATH = "2020/day06/input"
TEST_INPUT_FILEPATH = "2020/day06/test_input"

ALPHABET = "".join(map(chr, range(ord("a"), ord("a") + 26)))


def read_input(filepath):
    groups = []
    with open(filepath, "r") as fobj:
        new_group = []
        for line in fobj:
            if line == "\n":
                groups.append(new_group)
                new_group = []
            else:
                new_group.append(line.strip())
        groups.append(new_group)
    return groups


def sum_count_any(group, alphabet=ALPHABET):
    return sum(any(letter in item for item in group) for letter in alphabet)


if __name__ == "__main__":

    test_groups = read_input(TEST_INPUT_FILEPATH)
    test_count_sum = sum(sum_count_any(item) for item in test_groups)
    print("Sum of 'yes' answer counts (test set): {}".format(test_count_sum))
    assert test_count_sum == 11

    groups = read_input(INPUT_FILEPATH)
    count_sum = sum(sum_count_any(item) for item in groups)
    print("Sum of 'yes' answer counts: {}".format(count_sum))

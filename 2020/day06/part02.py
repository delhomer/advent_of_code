"""Advent of code 2020, day06, part02
"""

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


def sum_count_all(group, alphabet=ALPHABET):
    return sum(all(letter in item for item in group) for letter in alphabet)


def run(input_filepath, expected_result=None):
    groups = read_input(input_filepath)
    count_sum = sum(sum_count_all(item) for item in groups)
    print(
        "Sum of 'yes' answer counts{}: {}".format(
            "" if expected_result is None else " (test set)", count_sum
        )
    )
    if expected_result is not None:
        assert count_sum == expected_result


if __name__ == "__main__":

    run("test_input", 6)
    run("input")

"""Advent of code 2020, day14, part01
"""


def read_input(filepath):
    with open(filepath, "r") as fobj:
        return fobj.readlines()


def mask_value(v, mask):
    bin_value = int(v)
    for key, value in enumerate(mask):
        cur_mask = 1 << (len(mask) - 1) - key
        if value == "1":
            bin_value |= cur_mask
        elif value == "0":
            bin_value &= ~cur_mask
    return bin_value


def initialize(program):
    mask = ["X"] * 36
    mem = {}
    for instruction in program:
        key, value = instruction.strip().split(" = ")
        if key == "mask":
            mask = value
        else:
            mem[int(key[4:-1])] = mask_value(value, mask)
    return sum(mem.values())


def run(input_filepath, expected_result=None):
    program = read_input(input_filepath)
    result = initialize(program)
    print(
        "Sum of values in memory after initialization{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", 165)
    # run("test_input2")
    run("input")

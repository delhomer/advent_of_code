"""Advent of code 2020, day14, part02
"""


def read_input(filepath):
    with open(filepath, "r") as fobj:
        return fobj.readlines()


def mask_value_2(v, mask):
    addresses = [int(v)]
    for key, value in enumerate(mask):
        cur_mask = 1 << (len(mask) - 1) - key
        if value == "1":
            addresses = [bin_value | cur_mask for bin_value in addresses]
        elif value == "X":
            addresses = [bin_value | cur_mask for bin_value in addresses]
            new_addresses = []
            for bin_value in addresses:
                new_addresses.append(bin_value & ~cur_mask)
            addresses += new_addresses
    return addresses


def initialize(program):
    mask = ["X"] * 36
    mem = {}
    for instruction in program:
        key, value = instruction.strip().split(" = ")
        if key == "mask":
            mask = value
        else:
            for address in mask_value_2(int(key[4:-1]), mask):
                mem[address] = int(value)
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

    run("test_input2", 208)
    run("input")

"""Advent of code 2020, day08, part01
"""

def read_input(filepath):
    with open(filepath, "r") as fobj:
        return fobj.readlines()

def read_instruction(instruction):
    op, arg = instruction.strip().split()
    return op, int(arg)

def play_game(instructions):
    cur_idx = 0
    already_visited_instructions = []
    acc = 0
    while(cur_idx not in already_visited_instructions):
        operation, argument = read_instruction(instructions[cur_idx])
        if operation == "acc":
            acc += argument
        already_visited_instructions.append(cur_idx)
        if operation in ("acc", "nop"):
            cur_idx += 1
        else:  # operation == "jmp"
            cur_idx += argument
        assert 0 <= cur_idx <= len(instructions)
    return acc


def run(input_filepath, expected_result=None):
    instructions = read_input(input_filepath)
    accumulator = play_game(instructions)
    print(
        "Accumulator value before second execution{}: {}".format(
            "" if expected_result is None else " (test set)", accumulator
        )
    )
    if expected_result:
        assert accumulator == expected_result

if __name__ == "__main__":

    run("test_input", 5)
    run("input")

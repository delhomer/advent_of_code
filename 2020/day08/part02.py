"""Advent of code 2020, day08, part02
"""

def read_input(filepath):
    with open(filepath, "r") as fobj:
        instructions = []
        for line in fobj:
            operation, argument = line.strip().split()
            instructions.append([operation, int(argument)])
        return instructions


def try_playing(instructions):
    cur_idx = 0
    already_visited_instructions = []
    acc = 0
    while(cur_idx != len(instructions)):
        operation, argument = instructions[cur_idx]
        if operation == "acc":
            acc += argument
        already_visited_instructions.append(cur_idx)
        if operation in ("acc", "nop"):
            cur_idx += 1
        else:  # operation == "jmp"
            cur_idx += argument
        # Loopy behavior, the list of instructions is wrong.
        if cur_idx in already_visited_instructions:
            return None
        assert 0 <= cur_idx <= len(instructions)
    return acc


def play_game(instructions):
    for idx, instruction in enumerate(instructions):
        if instruction[0] == "acc" or (instruction[0] == "nop" and instruction[1] == 0):
            continue
        # Try a fix on the current instruction
        instructions[idx][0] = "jmp" if instructions[idx][0] == "nop" else "nop"
        acc = try_playing(instructions)
        if acc is not None:
            return acc
        # The fix is not good, restore the previous instruction
        instructions[idx][0] = "jmp" if instructions[idx][0] == "nop" else "nop"


def run(input_filepath, expected_result=None):
    instructions = read_input(input_filepath)
    accumulator = play_game(instructions)
    print(
        "Accumulator value at the end of the play{}: {}".format(
            "" if expected_result is None else " (test set)", accumulator
        )
    )
    if expected_result:
        assert accumulator == expected_result

if __name__ == "__main__":

    run("test_input", 8)
    run("input")

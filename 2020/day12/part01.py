"""Advent of code 2020, day12, part01
"""


directions = ["E", "S", "W", "N"]


def read_input(filepath):
    with open(filepath, "r") as fobj:
        return [[line[0], int(line[1:])] for line in fobj]


def process(instructions):
    to_east = 0
    to_north = 0
    direction_idx = 0  # Starting towards east
    for instruction in instructions:
        if instruction[0] in directions:
            direction = instruction[0]
        elif instruction[0] == "F":
            direction = directions[direction_idx]
        else:  # instruction is "R" or "L":
            direction_change = instruction[1] // 90
            direction_change *= -1 if instruction[0] == "L" else 1 
            direction_idx = (direction_idx + direction_change) % len(directions)
            continue
        if direction == "E":
            to_east += instruction[1]
        elif direction == "W":
            to_east -= instruction[1]
        elif direction == "N":
            to_north += instruction[1]
        elif direction == "S":
            to_north-= instruction[1]
    return abs(to_east) + abs(to_north)


def run(input_filepath, expected_result=None):
    instructions = read_input(input_filepath)
    result = process(instructions)
    print(
        "Manhattan distance between start and end positions{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", 25)
    run("input")

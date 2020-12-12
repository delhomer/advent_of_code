"""Advent of code 2020, day12, part02
"""


directions = ["E", "S", "W", "N"]


def read_input(filepath):
    with open(filepath, "r") as fobj:
        return [[line[0], int(line[1:])] for line in fobj]


def compass(waypoint_east, waypoint_north, move, degree):
    if degree == 180:
        return -waypoint_east, -waypoint_north
    elif (move == "R" and degree == 90) or (move == "L" and degree == 270):
        return waypoint_north, -waypoint_east
    elif (move == "R" and degree == 270) or (move == "L" and degree == 90):
        return -waypoint_north, waypoint_east
    else:
        raise ValueError("Unknown instruction.")

    
def process(instructions):
    waypoint_east = 10
    waypoint_north = 1
    to_east = 0
    to_north = 0
    for instruction in instructions:
        if instruction[0] == "E":
            waypoint_east += instruction[1]
        elif instruction[0] == "W":
            waypoint_east -= instruction[1]
        elif instruction[0] == "N":
            waypoint_north += instruction[1]
        elif instruction[0] == "S":
            waypoint_north-= instruction[1]
        elif instruction[0] == "F":
            to_east = to_east + instruction[1] * waypoint_east
            to_north = to_north + instruction[1] * waypoint_north
        else:  # instruction is "R" or "L":
            waypoint_east, waypoint_north = compass(
                waypoint_east, waypoint_north, instruction[0], instruction[1]
            )
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

    run("test_input", 286)
    run("input")

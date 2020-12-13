"""Advent of code 2020, day13, part01
"""


def read_input(filepath):
    with open(filepath, "r") as fobj:
        start = int(fobj.readline())
        lines = [int(l) for l in fobj.readline().split(",") if l != "x"]
        return start, lines


def plan_trip(start, lines):
    trips = {m * (1 + start // m) - start: m for m in lines}
    return min(trips) * trips[min(trips)]


def run(input_filepath, expected_result=None):
    start, lines = read_input(input_filepath)
    result = plan_trip(start, lines)
    print(
        "Bus ID multiplied by waiting minutes{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", 295)
    run("input")

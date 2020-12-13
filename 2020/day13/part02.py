"""Advent of code 2020, day13, part02
"""


def read_input(filepath):
    with open(filepath, "r") as fobj:
        fobj.readline()
        return {idx: int(l) for idx, l in enumerate(fobj.readline().split(",")) if l != "x"}


def solve(a, i, start, step):
    """Bezout-like solver, that returns the value of following equation, by kind of iterating of x:

    ```
    t = start + step * x = a * y - i
    ```

    """
    t = start
    while(True):
        if (t + i) % a == 0:
            return t
        t += step


def find_special_timestamp(lines):
    """Fancy solution, which makes me think: "I should've continued hard maths because I love that
    (even if it blows my mind on Sunday...)"

    Starting from GCD/LCM, to congruences, by paying attention to Bezout theorem, we can define
    first two lines equivalence as:

    ```
    timestamp = line_0 * x = line_1 * y - 1
    ```

    Actually the above equation accepts several solutions like:

    ```
    timestamp_i = line_0 * (x0 + line_1 * i) = line_1 * (y0 + line_0 * i) - 1
    ```

    with (x0, y0) the first solution to the first equation, for i=0 (which is the solution of part02's
    problem with only two bus line...).

    Hence we have to find how to iterate over lines. The key is found when considering that the
    second solution (i=1) is found after incrementing timestamp_0 by line_0 * line_1. Generalizing
    this approch for each subsequent line from the input, we can apply a smart solver which
    considers solution of the previous iteration as its starting point and accumulated products of
    line IDs to smartly jump over candidate solution.

    """
    timestamp = 1
    acc = 1
    for idx, line in lines.items():
        timestamp = solve(line, idx, timestamp, acc)
        acc *= line
    return timestamp


def find_special_timestamp_greedy_version(lines, lower_bound=0):
    """Warning: very greedy method!
    It takes a loooooong time before getting the solution for large numbers
    even by using the trick in the wording:
    "surely the actual earliest timestamp will be larger than 100000000000000"
    """
    max_line_idx = max(lines, key=lines.get)
    timestamp = lines[max_line_idx] * (1 + lower_bound // lines[max_line_idx]) - max_line_idx
    while True:
        for idx, l in lines.items():
            if not (timestamp + idx) % l == 0:
                break
        else:
            return timestamp
        timestamp += lines[max_line_idx]


def run(input_filepath, expected_result=None):
    lines = read_input(input_filepath)
    result = find_special_timestamp(lines)
    print(
        "Timestamp from which bus IDs depart at good offset{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", 1068781)
    run("test_input2", 3417)
    run("test_input3", 754018)
    run("test_input4", 779210)
    run("test_input5", 1261476)
    run("test_input6", 1202161486)
    run("input")

"""Advent of code 2020, day15, part01
"""


def play(numbers):
    while(len(numbers) < 2020):
        for idx, n in enumerate(reversed(numbers[:-1])):
            if n == numbers[-1]:
                numbers.append(len(numbers) - ((len(numbers) - 1) - idx))
                break
        else:
            numbers.append(0)
    return numbers[-1]


def run(input_str, expected_result=None):
    starting_number = [int(item) for item in input_str.split(",")]
    result = play(starting_number)
    print(
        "2020th number spoken durint the memory game{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("0,3,6", 436)
    run("1,3,2", 1)
    run("2,1,3", 10)
    run("1,2,3", 27)
    run("2,3,1", 78)
    run("3,2,1", 438)
    run("3,1,2", 1836)
    run("0,14,1,3,7,9")

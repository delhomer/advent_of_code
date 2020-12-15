"""Advent of code 2020, day15, part02
"""

def play_faster(numbers):
    target = 30000000
    res = {n: idx + 1 for idx, n in enumerate(numbers)}
    cur_figure = 0
    counter = len(res)
    while(counter < target - 1):
        counter += 1
        next_figure = counter - res[cur_figure] if cur_figure in res else 0
        res[cur_figure] = counter
        cur_figure = next_figure
    return cur_figure


def run(input_str, expected_result=None):
    starting_number = [int(item) for item in input_str.split(",")]
    result = play_faster(starting_number)
    print(
        "30000000th number spoken durint the memory game{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("0,3,6", 175594)
    run("1,3,2", 2578)
    run("2,1,3", 3544142)
    run("1,2,3", 261214)
    run("2,3,1", 6895259)
    run("3,2,1", 18)
    run("3,1,2", 362)
    run("0,14,1,3,7,9")

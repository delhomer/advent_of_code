"""Advent of code 2020, day10, part01
"""

def read_input(filepath):
    with open(filepath, "r") as fobj:
        adapter_ratings = []
        for line in fobj:
            adapter_ratings.append(int(line.strip()))
        return sorted(adapter_ratings)


def extract_jolt_differences(adapter_ratings):
    one_jolt_diff = adapter_ratings[0] == 1
    three_jolt_diff = adapter_ratings[0] == 3
    for rating_idx in range(len(adapter_ratings) - 1):
        jolt_diff = adapter_ratings[rating_idx + 1] - adapter_ratings[rating_idx]
        one_jolt_diff += jolt_diff == 1
        three_jolt_diff += jolt_diff == 3
    three_jolt_diff += 1  # Represent the gap between highest rating and device built-in adapter rating
    return one_jolt_diff * three_jolt_diff


def run(input_filepath, expected_result=None):
    adapter_ratings = read_input(input_filepath)
    result = extract_jolt_differences(adapter_ratings)
    print(
        "Number of 1-jolt differences multiplied by number of 3-jolt differences{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", 35)
    run("test_input2", 220)
    run("input")

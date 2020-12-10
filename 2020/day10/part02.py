"""Advent of code 2020, day10, part02
"""


def read_input(filepath):
    with open(filepath, "r") as fobj:
        adapter_ratings = []
        for line in fobj:
            adapter_ratings.append(int(line.strip()))
        return sorted(adapter_ratings)


def reset_cache():
    global arrangement_cache
    arrangement_cache = {}


def count_arrangements(adapter_ratings, rating):
    if rating in arrangement_cache:
        return arrangement_cache[rating]
    candidate_ratings = [r for r in adapter_ratings if rating < r <= rating + 3]
    if len(candidate_ratings) == 0:
        return 1
    arrangement_amount = 0
    for cr in candidate_ratings:
        arrangement_amount += count_arrangements(adapter_ratings, cr)
    arrangement_cache[rating] = arrangement_amount
    return arrangement_amount


def run(input_filepath, expected_result=None):
    reset_cache()
    adapter_ratings = read_input(input_filepath)
    result = count_arrangements(adapter_ratings, 0)
    print(
        "Number of arrangements with given adapters{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", 8)
    run("test_input2", 19208)
    run("input")

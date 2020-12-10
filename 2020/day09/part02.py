"""Advent of code 2020, day09, part02
"""

def read_input(filepath, buffer_size):
    with open(filepath, "r") as fobj:
        numbers = []
        buffered_numbers = []
        for line in fobj:
            candidate_number = int(line.strip())
            numbers.append(candidate_number)
            if len(buffered_numbers) < buffer_size:
                buffered_numbers.append(candidate_number)
                continue
            else:
                valid_candidate = False
                for idx1, b1 in enumerate(buffered_numbers):
                    for b2 in buffered_numbers[idx1:]:
                        if b1 + b2 == candidate_number:
                            buffered_numbers.append(candidate_number)
                            valid_candidate = True
                            break
                    if valid_candidate:
                        break
                if len(buffered_numbers) > buffer_size:
                    buffered_numbers.pop(0)
                else:
                    return candidate_number, numbers


def identify_continuous_range(unvalid_number, numbers):
    start_index = 0
    for idx in range(len(numbers)):
        start_index = idx
        for idx, n in enumerate(numbers[start_index:]):
            candidate_range = numbers[start_index:(start_index + idx + 1)]
            candidate_sum = sum(candidate_range)
            if candidate_sum == unvalid_number:
                return min(candidate_range) + max(candidate_range)
            elif candidate_sum > unvalid_number:
                break
        

def run(input_filepath, expected_result=None, buffer_size=None):
    unvalid_number, numbers = read_input(input_filepath, buffer_size)
    result = identify_continuous_range(unvalid_number, numbers)
    print(
        "First unvalid number regarding XMAS encoding{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", 62, buffer_size=5)
    run("input", buffer_size=25)
